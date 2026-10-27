#!/usr/bin/env python3
"""Relay phase diagrams for the IMprecision 1♣ structure.

Each relay node maps the shapes still possible at that node to a bid.  This
script states that map as ordered rules, checks that every shape gets exactly
one bid, and draws the map as hexagonal lattices (one per length of an indexing
suit; of the other three, the highest ranking points up, the next down-left and
the lowest down-right; a lattice on one line is turned flat) into
src/1C/relay/*.svg, which the 1♣ chapters include.
Nodes are named by the auction after 1♣, ending with the relay the node answers.
Borders are drawn where the bid changes; a hatched cell is a hole or a clash.

The generic tables (one-suited, two-suited, 5-5, three-suited, balanced) are
written once, relative to an entry step, and instantiated per node.  Where the
source leaves an orientation unresolved (7321, 5-5 shapes with 7 cards), the
shapes share a bid; that is not a clash.

Run it by hand after editing the rules.  Exit code 1 on any hole or clash.
"""
from math import atan2, cos, degrees, radians, sin, sqrt
import os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src/1C/relay')
# ponytail: 8+ card suits omitted; extend the range if a rule ever needs them
SHAPES = [(s, h, d, c) for s in range(8) for h in range(8) for d in range(8)
          for c in [13 - s - h - d] if 0 <= c <= 7]
STEPS = ['1NT', '2♣', '2♦', '2♥', '2♠', '2NT', '3♣', '3♦', '3♥', '3♠', '3NT',
         '4♣', '4♦', '4♥', '4♠']
S = STEPS.index

def solve(domain, rules):
    """{shape: bid} for shapes in domain; bid is 'a/b' on clash, '?' on hole."""
    out = {}
    for x in SHAPES:
        if domain(*x):
            hits = [bid for bid, p in rules if p(*x)]
            out[x] = '/'.join(hits) or '?'
    return out

CHECKED, FIGURES = {}, {}
def node(name, domain, rules, idx=None):
    """Register a relay node; idx picks the suit whose length indexes the
    lattices, None for a node that is only checked, not drawn."""
    assert name not in CHECKED, name
    CHECKED[name] = m = solve(domain, rules)
    if idx is not None:
        FIGURES[name] = (m, idx)
    return m

def after(name, bid):
    """Domain of the node reached by answering `bid` at node `name`."""
    return lambda *x: CHECKED[name].get(x) == bid

def sub(name, bid):
    """Name of the node after answer `bid` and the next-step relay."""
    return f'{name}-{bid}-{STEPS[S(bid) + 1]}'.replace('♣', 'C').replace('♦', 'D') \
        .replace('♥', 'H').replace('♠', 'S')

def ladder(e, preds):
    """Consecutive steps from STEPS[e], one per predicate."""
    return list(zip(STEPS[e:], preds))

def exact(*shape):
    return lambda *x: x == shape

def listed(e, shapes):
    return ladder(e, [exact(*x) for x in shapes])

def others(*fixed):
    return [i for i in range(4) if i not in fixed]

# ------------------------------------------------------------------ hand types
THREE = lambda *x: sum(v >= 4 for v in x) == 3
BAL = lambda s, h, d, c: sorted((s, h, d, c)) in ([3, 3, 3, 4], [2, 3, 4, 4]) \
    or sorted((s, h, d, c)) == [2, 3, 3, 5] and max(s, h) <= 4
ONE = lambda m: lambda *x: x[m] >= 5 and max(x[:m] + x[m + 1:]) <= 3
TWO = lambda a, b: lambda *x: x[a] >= 4 and x[b] >= 4 and x[a] + x[b] >= 9 and not THREE(*x)

# ------------------------------------------------------------- generic tables
def uneven(name, dom, p, q, e, extra=(), idx=None):
    """5+ in suit p and exactly 4 in q; STEPS[e] is high shortage.  Also
    registers the node after high shortage."""
    hi, lo = others(p, q)
    G = lambda f: (lambda *x: x[p] >= 5 and x[q] == 4 and not THREE(*x) and f(*x))
    L = lambda n, a, b: G(lambda *x: x[p] == n and x[hi] == a and x[lo] == b)
    node(name, dom, list(extra) + ladder(e, [
        G(lambda *x: x[hi] < x[lo] or x[hi] == x[lo] == 1),
        L(5, 2, 2), L(5, 3, 1), L(6, 2, 1), L(6, 3, 0), L(7, 2, 0)]), idx)
    node(sub(name, STEPS[e]), after(name, STEPS[e]), ladder(e + 2, [
        L(5, 1, 3), L(6, 1, 2), L(6, 0, 3), L(7, 1, 1), L(7, 0, 2)]))

def fivefive(name, dom, a, b, e, extra=(), idx=None):
    """5-5 or longer in suits a (higher) and b; STEPS[e] is high shortage.
    7-5 and 6-6 are outside the table and excluded from the domain."""
    hi, lo = others(a, b)
    G = lambda f: (lambda *x: x[a] >= 5 and x[b] >= 5 and f(*x))
    L = lambda n, m, u, v: (lambda *x: x == tuple(
        {a: n, b: m, hi: u, lo: v}[i] for i in range(4)))
    dom2 = lambda *x: dom(*x) and x[a] + x[b] <= 11
    node(name, dom2, list(extra) + ladder(e, [
        G(lambda *x: x[hi] < x[lo]), G(lambda *x: x[hi] == x[lo] == 1),
        L(5, 5, 2, 1), L(5, 5, 3, 0), L(5, 6, 2, 0), L(6, 5, 2, 0)]), idx)
    node(sub(name, STEPS[e]), after(name, STEPS[e]), ladder(e + 2, [
        L(5, 5, 1, 2), L(5, 5, 0, 3), L(5, 6, 0, 2), L(6, 5, 0, 2)]))
    node(sub(name, STEPS[e + 1]), after(name, STEPS[e + 1]), ladder(e + 3, [
        L(5, 6, 1, 1), L(6, 5, 1, 1)]))

def two(name, dom, a, b, e, extra=(), idx=None, reverser=True, long=True):
    """Two-suited table in suits a (higher) and b, STEPS[e] the entry step:
    reverser (4 in a, 5+ in b), 5-5, then the uneven table with 5+ in a."""
    rules = list(extra)
    if reverser:
        rules.append((STEPS[e], lambda *x: x[a] == 4 and x[b] >= 5 and not THREE(*x))); e += 1
    if long:
        rules.append((STEPS[e], lambda *x: x[a] >= 5 and x[b] >= 5)); e += 1
    uneven(name, dom, a, b, e, rules, idx)
    if reverser:
        uneven(sub(name, STEPS[e - 1 - long]), after(name, STEPS[e - 1 - long]), b, a, e + 1 - long)
    if long:
        fivefive(sub(name, STEPS[e - 1]), after(name, STEPS[e - 1]), a, b, e + 1)

def one(name, dom, m, e, skip=False, extra=(), idx=None):
    """One-suited table in suit m, STEPS[e] the entry step (high shortage).
    skip drops 5332.  Low shortage runs straight on to the shape (Kerr);
    IMprecision sends 6322 with a high doubleton to the first step and 7222
    to the equal-shortage step."""
    hi, mid, lo = others(m)
    side = lambda x: (x[hi], x[mid], x[lo])
    G = lambda f: (lambda *x: ONE(m)(*x) and (x[m] >= 6 or not skip) and f(*x))
    P = lambda n, t: (lambda *x: x[m] == n and side(x) == t)
    low = [P(5, (3, 3, 2)), P(6, (3, 3, 1)),
           G(lambda *x: x[m] == 7 and x[lo] == 1 and x[hi] != x[mid]), P(7, (3, 3, 0))]
    high = [G(lambda *x: x[m] == 6 and x[hi] == 2), P(5, (2, 3, 3)), P(6, (1, 3, 3)),
            G(lambda *x: x[m] == 7 and x[hi] == 1 and x[mid] != x[lo]), P(7, (0, 3, 3))]
    midl = [P(5, (3, 2, 3)), P(6, (3, 1, 3)),
            G(lambda *x: x[m] == 7 and x[mid] == 1 and x[hi] != x[lo]), P(7, (3, 0, 3))]
    if skip:
        del low[0], high[1], midl[0]
    node(name, dom, list(extra) + ladder(e, [
        G(lambda *x: x[hi] == min(side(x)) and not x[hi] == x[mid] == x[lo] and not x[mid] == x[lo] < x[hi]),
        G(lambda *x: x[mid] < x[hi] and x[mid] < x[lo]),
        G(lambda *x: x[m] in (6, 7) and x[hi] >= x[mid] == x[lo])] + low), idx)
    h = sub(name, STEPS[e])
    node(h, after(name, STEPS[e]), ladder(e + 2, high))
    node(sub(h, STEPS[e + 2]), after(h, STEPS[e + 2]), ladder(e + 4, [P(6, (2, 2, 3)), P(6, (2, 3, 2))]))
    node(sub(name, STEPS[e + 1]), after(name, STEPS[e + 1]), ladder(e + 3, midl))
    node(sub(name, STEPS[e + 2]), after(name, STEPS[e + 2]), ladder(e + 4, [P(6, (3, 2, 2)), P(7, (2, 2, 2))]))

def three(name, dom, short, e, extra=()):
    """Three-suited with shortness in suit `short`: 4441, then 5440 with the
    5-card suit from the lowest to the highest."""
    lo, mid, hi = reversed(others(short))
    G = lambda f: (lambda *x: THREE(*x) and x[short] <= 1 and f(*x))
    return node(name, dom, list(extra) + ladder(e, [
        G(lambda *x: x[short] == 1), G(lambda *x: x[lo] == 5), G(lambda *x: x[mid] == 5), G(lambda *x: x[hi] == 5)]))

def balanced4(name, dom, e, idx=None):
    """BAL with 4♠, or three-suited short in a red suit; STEPS[e] shows 0--2♥."""
    node(name, dom, ladder(e, [
        lambda s, h, d, c: h <= 2, lambda s, h, d, c: THREE(s, h, d, c) and d <= 1,
        lambda *x: x in ((4, 3, 2, 4), (4, 4, 2, 3)), exact(4, 3, 3, 3), exact(4, 3, 4, 2), exact(4, 4, 3, 2)]), idx)
    h = sub(name, STEPS[e])
    node(h, after(name, STEPS[e]), [(STEPS[e + 2], lambda s, h, d, c: h == 2)]
         + listed(e + 3, [(4, 1, 4, 4), (4, 0, 4, 5), (4, 0, 5, 4), (5, 0, 4, 4)]))
    node(sub(h, STEPS[e + 2]), after(h, STEPS[e + 2]), listed(e + 4, [(4, 2, 3, 4), (4, 2, 4, 3)]))
    node(sub(name, STEPS[e + 1]), after(name, STEPS[e + 1]),
         listed(e + 3, [(4, 4, 1, 4), (4, 4, 0, 5), (4, 5, 0, 4), (5, 4, 0, 4)]))
    node(sub(name, STEPS[e + 2]), after(name, STEPS[e + 2]), listed(e + 4, [(4, 3, 2, 4), (4, 4, 2, 3)]))

def balanced3(name, dom, e, idx=None):
    """BAL without 4♠; STEPS[e] shows 2=♠, the rest 3=♠."""
    node(name, dom, ladder(e, [
        lambda s, h, d, c: s == 2, lambda *x: x in ((3, 4, 3, 3), (3, 3, 4, 3), (3, 3, 3, 4)),
        lambda s, h, d, c: s == 3 and c == 5, lambda s, h, d, c: s == 3 and d == 5,
        exact(3, 2, 4, 4), exact(3, 4, 2, 4), exact(3, 4, 4, 2)]), idx)
    for k, shapes in enumerate([[(2, 3, 3, 5), (2, 3, 5, 3), (2, 3, 4, 4), (2, 4, 3, 4), (2, 4, 4, 3)],
                                [(3, 3, 3, 4), (3, 3, 4, 3), (3, 4, 3, 3)],
                                [(3, 2, 3, 5), (3, 3, 2, 5)], [(3, 2, 5, 3), (3, 3, 5, 2)]]):
        node(sub(name, STEPS[e + k]), after(name, STEPS[e + k]), listed(e + k + 2, shapes))

# ------------------------------------------------------------------ responses
# Shape only; the jump responses (2NT+) and strength splits are not modelled.
node('1C', lambda *x: True, [
    ('1♥',  lambda s, h, d, c: s >= 4 and not (THREE(s, h, d, c) and c <= 1)),
    ('1♠',  lambda s, h, d, c: s <= 3 and (d >= 5 and h <= 4 and c <= 4 and not THREE(s, h, d, c)
                                           or BAL(s, h, d, c))),
    ('1NT', lambda s, h, d, c: h >= 5 and s <= 3 and c <= 4 and not THREE(s, h, d, c)),
    ('2♣',  lambda s, h, d, c: c >= 5 and s <= 3 and h <= 3 and not BAL(s, h, d, c)),
    ('2♦',  lambda s, h, d, c: c >= 5 and h >= 4 and s <= 3 and d <= 3),
    ('2♥',  lambda s, h, d, c: s <= 1 and THREE(s, h, d, c)),
    ('2♠',  lambda s, h, d, c: c <= 1 and THREE(s, h, d, c)),
])

# 1♥: 4+♠.  The 1♠ relay; 2♥ reverser, 2♠ 5-5, 2NT+ 5+♠ 4=♥ on track.
two('1H-1S', after('1C', '1♥'), 0, 1, S('2♥'), idx=0, extra=[
    ('1NT', lambda *x: BAL(*x) or TWO(0, 2)(*x) or THREE(*x) and min(x[1], x[2]) <= 1),
    ('2♣',  TWO(0, 3)),
    ('2♦',  ONE(0)),
])
two('1H-1S-1NT-2C', after('1H-1S', '1NT'), 0, 2, S('2♥'), idx=0,
    extra=[('2♦', lambda *x: BAL(*x) or THREE(*x))])
balanced4('1H-1S-1NT-2C-2D-2H', after('1H-1S-1NT-2C', '2♦'), S('2♠'), 0)
two('1H-1S-2C-2D', after('1H-1S', '2♣'), 0, 3, S('2♥'), idx=0)
one('1H-1S-2D-2H', after('1H-1S', '2♦'), 0, S('2♠'), idx=0)
# Opener's natural rebids that responder relays over.
one('1H-2H-2S', lambda *x: ONE(1)(*x) and x[1] >= 6, 1, S('2NT'), skip=True, idx=1)
# ponytail: "both minors, any strength" is read as 5-5 like 1♣ - 1♦ - 2♠
fivefive('1H-2S-2NT', lambda s, h, d, c: d >= 5 and c >= 5, 2, 3, S('3♣'), idx=2)

# 1♠: 5+♦ or BAL without 4♠.  The 2♣ relay.
one('1S-2C', after('1C', '1♠'), 2, S('2NT'), skip=True, idx=2, extra=[
    ('2♦',  BAL),
    ('2♥',  lambda s, h, d, c: h == 4 and d >= 5),
    ('2♠',  lambda s, h, d, c: c == 4 and d >= 5),
])
balanced3('1S-2C-2D-2H', after('1S-2C', '2♦'), S('2♠'), 0)
# ponytail: 4=♥ 5+♦ has no continuation in the source; taken as on track
uneven('1S-2C-2H-2S', after('1S-2C', '2♥'), 2, 1, S('2NT'))
uneven('1S-2C-2S-2NT', after('1S-2C', '2♠'), 2, 3, S('3♣'))

# 1NT: 5+♥, no 4♠, no 5+♣.  The 2♣ relay.
one('1NT-2C', after('1C', '1NT'), 1, S('2♠'), idx=1, extra=[
    ('2♦',  lambda s, h, d, c: d >= 4),
    ('2♥',  lambda s, h, d, c: c == 4),
])
two('1NT-2C-2D-2H', after('1NT-2C', '2♦'), 1, 2, S('2♠'), reverser=False)
uneven('1NT-2C-2H-2S', after('1NT-2C', '2♥'), 1, 3, S('2NT'))
fivefive('1NT-2S-2NT', lambda s, h, d, c: d >= 5 and c >= 5, 2, 3, S('3♣'), idx=2)

# 2♣: UNBAL 5+♣, no 4-card major.  2♦: 5+♣ and 4+♥.
one('2C-2D', after('1C', '2♣'), 3, S('2NT'), skip=True, idx=3, extra=[
    ('2♥',  lambda s, h, d, c: d == 4),
    ('2♠',  lambda s, h, d, c: d >= 5),
])
uneven('2C-2D-2H-2S', after('2C-2D', '2♥'), 3, 2, S('2NT'))
fivefive('2C-2D-2S-2NT', after('2C-2D', '2♠'), 2, 3, S('3♣'))
# ponytail: "two-suited table" over the 2♥ relay is taken literally, a step up
two('2D-2H', after('1C', '2♦'), 1, 3, S('2♠'), idx=3)

# Three-suited and the jump responses.
three('2H-2S', after('1C', '2♥'), 0, S('2NT'))
three('2S-3C', after('1C', '2♠'), 3, S('3♦'))
node('2NT-3C', lambda *x: x[3] == 6 and sorted(x[:3]) == [2, 2, 3],
     listed(S('3♦'), [(2, 2, 3, 6), (2, 3, 2, 6), (3, 2, 2, 6)]))   # 3♠ or 3NT by RP
node('3C-3D', lambda *x: sorted(x) == [2, 2, 2, 7] and max(x[:2]) == 2,
     listed(S('3♥'), [(2, 2, 2, 7), (2, 2, 7, 2)]))                 # 3♠ or 3NT by RP

# ------------------------------------------------------------- opener after 1♦
# Shape only: BAL goes 1♥♠ as with 21+, and the strength-based alternatives
# (1NT, 2♥, 2NT, 3♣♦♥♠) are not modelled.
node('1D', lambda *x: True, [
    ('1♥',  lambda s, h, d, c: THREE(s, h, d, c) and min(s, c) <= 1 or BAL(s, h, d, c) and s <= 3
                               or not THREE(s, h, d, c) and not BAL(s, h, d, c)
                               and (h >= 4 and s <= 3 and not (h == 4 and c >= 5) or s == 4 and h >= 5)),
    ('1♠',  lambda s, h, d, c: THREE(s, h, d, c) and min(h, d) <= 1 or BAL(s, h, d, c) and s == 4
                               or not THREE(s, h, d, c) and not BAL(s, h, d, c) and s >= 4 and not (s == 4 and h >= 5)),
    ('2♣',  lambda s, h, d, c: s <= 3 and c >= 5 and h <= 4 and d <= 4 and not THREE(s, h, d, c)
                               and not BAL(s, h, d, c) and (c >= 6 or d == 4 or h == 4)),
    ('2♦',  lambda s, h, d, c: s <= 3 and h <= 3 and c <= 4 and (d >= 6 or d == 5 and c == 4)
                               and not BAL(s, h, d, c)),
    ('2♠',  lambda s, h, d, c: d >= 5 and c >= 5),
])

# 1♥ rebid, 1NT relay: one-suiters on track, everything else up a step.
one('1D-1H-1NT', after('1D', '1♥'), 1, S('2♠'), idx=1, extra=[
    ('2♣',  lambda *x: TWO(1, 2)(*x) or BAL(*x)),
    ('2♦',  lambda s, h, d, c: h >= 5 and c >= 4 and not THREE(s, h, d, c) or THREE(s, h, d, c) and s <= 1),
    ('2♥',  lambda s, h, d, c: h >= 5 and s == 4 and not THREE(s, h, d, c) or THREE(s, h, d, c) and c <= 1),
])
two('1D-1H-1NT-2C-2D', after('1D-1H-1NT', '2♣'), 1, 2, S('2♠'), extra=[('2♥', BAL)])
balanced3('1D-1H-1NT-2C-2D-2H-2S', after('1D-1H-1NT-2C-2D', '2♥'), S('2NT'))
two('1D-1H-1NT-2D-2H', after('1D-1H-1NT', '2♦'), 1, 3, S('2NT'), reverser=False,
    extra=[('2♠', THREE)])
three('1D-1H-1NT-2D-2H-2S-2NT', after('1D-1H-1NT-2D-2H', '2♠'), 0, S('3♣'))
uneven('1D-1H-1NT-2H-2S', after('1D-1H-1NT', '2♥'), 1, 0, S('3♣'), extra=[('2NT', THREE)])
three('1D-1H-1NT-2H-2S-2NT-3C', after('1D-1H-1NT-2H-2S', '2NT'), 3, S('3♦'))

# 1♠ rebid, 1NT relay.
one('1D-1S-1NT', after('1D', '1♠'), 0, S('2♠'), idx=0, extra=[
    ('2♣',  lambda *x: TWO(0, 2)(*x) or BAL(*x) or THREE(*x) and min(x[1], x[2]) <= 1),
    ('2♦',  TWO(0, 3)),
    ('2♥',  lambda s, h, d, c: s >= 5 and h >= 4 and not THREE(s, h, d, c)),
])
two('1D-1S-1NT-2C-2D', after('1D-1S-1NT', '2♣'), 0, 2, S('2♠'),
    extra=[('2♥', lambda *x: BAL(*x) or THREE(*x))])
balanced4('1D-1S-1NT-2C-2D-2H-2S', after('1D-1S-1NT-2C-2D', '2♥'), S('2NT'))
two('1D-1S-1NT-2D-2H', after('1D-1S-1NT', '2♦'), 0, 3, S('2NT'))
two('1D-1S-1NT-2H-2S', after('1D-1S-1NT', '2♥'), 0, 1, S('2NT'), reverser=False)

# Minor-suit rebids and the two-suited 2♥♠.
one('1D-2C-2D', after('1D', '2♣'), 3, S('2NT'), skip=True, idx=3, extra=[
    ('2♥',  lambda s, h, d, c: h == 4),
    ('2♠',  lambda s, h, d, c: d == 4),
])
uneven('1D-2C-2D-2H-2S', after('1D-2C-2D', '2♥'), 3, 1, S('2NT'))
uneven('1D-2C-2D-2S-2NT', after('1D-2C-2D', '2♠'), 3, 2, S('3♣'))
one('1D-2D-2H', after('1D', '2♦'), 2, S('2NT'), skip=True, idx=2, extra=[
    ('2♠',  lambda s, h, d, c: c == 4),
])
uneven('1D-2D-2H-2S-2NT', after('1D-2D-2H', '2♠'), 2, 3, S('3♣'))
uneven('1D-2H-2S', lambda s, h, d, c: h == 4 and c >= 5 and s <= 3 and not THREE(s, h, d, c), 3, 1, S('2NT'), idx=3)
fivefive('1D-2S-2NT', after('1D', '2♠'), 2, 3, S('3♣'), idx=2)

# ---------------------------------------------------------------------- drawing
STEP = 46                      # lattice spacing = cell width
R = STEP / sqrt(3)             # hexagon circumradius (pointy-top)
GAP, MAXW, HEAD = 28, 720, 20   # HEAD: room above a lattice for its legend
SUITS = '♠♥♦♣'
# neighbour offsets in (up, left, right) and the angle each one lies at
NEIGH = [((0, -1, 1), 0), ((1, -1, 0), 60), ((1, 0, -1), 120),
         ((0, 1, -1), 180), ((-1, 1, 0), 240), ((-1, 0, 1), 300)]

def ent(text):
    """Suit symbols as entities, red ones in a coloured tspan, so the replace
    preprocessor cannot inject HTML into the SVG."""
    for ch, code in ('♥', '2665'), ('♦', '2666'):
        text = text.replace(ch, f'<tspan class="&#x{code};">&#x{code};</tspan>')
    return text.replace('♠', '&#x2660;').replace('♣', '&#x2663;')

def centre(up, left, right):
    return (2 * right + up) * STEP / 2, -up * STEP * sqrt(3) / 2

def vertex(x, y, deg):
    return f'{x + R * cos(radians(deg)):.1f},{y - R * sin(radians(deg)):.1f}'

def patch(idx, cells):
    """One lattice for a fixed length of suit idx.  Returns (width, height,
    svg) with the origin at the top-left corner.  A flat lattice also fixes
    one of the other suits, so its legend names that suit too."""
    rest = [i for i in range(4) if i != idx]
    pos = {x: centre(*(x[i] for i in rest)) for x in cells}
    # A lattice on one line is laid flat, its top end on the left.
    a, b = min(pos.values(), key=lambda p: (p[1], p[0])), max(pos.values(), key=lambda p: (p[1], p[0]))
    deg = round(degrees(atan2(a[1] - b[1], b[0] - a[0])))
    flat = all(abs((p[0] - a[0]) * (b[1] - a[1]) - (p[1] - a[1]) * (b[0] - a[0])) < 1e-6
               for p in pos.values())
    rot = -deg % 360 if flat and deg % 60 == 0 else 0
    c, s = cos(radians(rot)), sin(radians(rot))
    pos = {x: (px * c + py * s, py * c - px * s) for x, (px, py) in pos.items()}
    xs = [p[0] for p in pos.values()]; ys = [p[1] for p in pos.values()]
    x0, y0 = min(xs) - R, min(ys) - R - HEAD
    w, h = max(xs) - min(xs) + 2 * R, max(ys) - min(ys) + 2 * R + HEAD
    faint, hard, hatch, labels = [], [], [], []
    for x, bid in cells.items():
        cx, cy = pos[x][0] - x0, pos[x][1] - y0
        hexagon = 'M' + 'L'.join(vertex(cx, cy, 30 + 60 * k) for k in range(6)) + 'Z'
        faint.append(hexagon)
        if '/' in bid or bid == '?':
            hatch.append(hexagon)
        for off, deg in NEIGH:
            n = list(x)
            for i, o in zip(rest, off):
                n[i] += o
            if cells.get(tuple(n)) != bid:
                hard.append(f'M{vertex(cx, cy, deg + rot - 30)}L{vertex(cx, cy, deg + rot + 30)}')
        labels.append(f'<text x="{cx:.1f}" y="{cy - 1:.1f}">{ent(bid)}</text>'
                      f'<text x="{cx:.1f}" y="{cy + 11:.1f}" font-size="8.5" opacity=".6">'
                      f'{"".join(map(str, x))}</text>')
    fixed = [idx] + [i for i in rest if flat and len({x[i] for x in cells}) == 1]
    svg = (f'<text x="2" y="12" font-size="11" opacity=".6" text-anchor="start">'
           f'{ent(", ".join(f"{x[i]}={SUITS[i]}" for i in fixed))}</text>'
           f'<path d="{"".join(faint)}" fill="none" stroke="currentColor" stroke-opacity=".15"/>'
           + (f'<path d="{"".join(hatch)}" fill="url(#hatch)"/>' if hatch else '')
           + f'<path d="{"".join(hard)}" fill="none" stroke="currentColor" stroke-width="1.5"/>'
           + ''.join(labels))
    return w, h, svg

def figure(mapping, idx):
    """Pack one patch per length of suit idx into rows no wider than MAXW.
    A lattice with a single bid says nothing the table does not, so it is left out."""
    groups = [{x: b for x, b in mapping.items() if x[idx] == v}
              for v in sorted({x[idx] for x in mapping})]
    patches = [patch(idx, g) for g in groups if len(set(g.values())) > 1]
    body, x, y, rowh = [], 0, 0, 0
    for w, h, svg in patches:
        if x and x + w > MAXW:
            x, y, rowh = 0, y + rowh + GAP, 0
        body.append(f'<g transform="translate({x:.1f},{y:.1f})">{svg}</g>')
        x, rowh = x + w + GAP, max(rowh, h)
    W, H = MAXW if y else x - GAP, y + rowh
    body = '\n'.join(body)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" '
            f'style="display:block;margin:1em auto;width:100%;max-width:{W:.0f}px" fill="currentColor" '
            f'font-size="13" text-anchor="middle" dominant-baseline="middle">\n'
            '<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)"><path d="M0 0v6" stroke="currentColor" '
            f'stroke-opacity=".35"/></pattern></defs>\n{body}\n</svg>\n')

if __name__ == '__main__':
    bad = 0
    os.makedirs(OUT, exist_ok=True)
    for name, mapping in CHECKED.items():
        for x, bid in mapping.items():
            if '/' in bid or bid == '?':
                print(f'{name}: {"".join(map(str, x))} -> {bid}', file=sys.stderr); bad += 1
    for f in os.listdir(OUT):
        os.remove(os.path.join(OUT, f))
    for name, (mapping, idx) in FIGURES.items():
        if len(set(mapping.values())) > 1:
            open(os.path.join(OUT, name + '.svg'), 'w').write(figure(mapping, idx))
    print(f'{len(CHECKED)} nodes checked, {len(os.listdir(OUT))} figures', file=sys.stderr)
    sys.exit(bool(bad))
