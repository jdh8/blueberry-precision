#!/usr/bin/env python3
"""Relay phase diagrams.

Each relay node maps the shapes still possible at that node to a bid.  This
script states that map as ordered rules, checks that every shape gets exactly
one bid, and draws the map as hexagonal lattices (one per length of an indexing suit;
of the other three, the highest ranking points up, the next down-left and
the lowest down-right; a lattice on one line is turned flat) into
src/1C/relay/*.svg, which the 1♣ chapters include.
Nodes are named by the auction after 1♣.
Borders are drawn where the bid changes; a hatched cell is a hole or a clash.

Run it by hand after editing the rules.  Exit code 1 on any hole or clash.
"""
from math import atan2, cos, degrees, radians, sin, sqrt
import os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src/1C/relay')
# ponytail: 8+ card suits omitted; extend the range if a rule ever needs them
SHAPES = [(s, h, d, c) for s in range(8) for h in range(8) for d in range(8)
          for c in [13 - s - h - d] if 0 <= c <= 7]
BAL = lambda s, h, d, c: sorted((s, h, d, c)) in ([2, 3, 3, 5], [2, 3, 4, 4], [3, 3, 3, 4])

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
    CHECKED[name] = m = solve(domain, rules)
    if idx is not None:
        FIGURES[name] = (m, idx)
    return m

def pattern(suit, length, rest):
    """Shape with `length` cards in suit index `suit` and the other three
    lengths `rest` in any order, e.g. (6322)."""
    return lambda *x: x[suit] == length and sorted(x[:suit] + x[suit + 1:]) == sorted(rest)

def exact(*shape):
    return lambda *x: x == shape

# ---------------------------------------------------------------- 1♣-1♦-1♥-1NT
# The tables leave longest-suit precedence implicit; the rules spell it out.
# Responder: FG, 5+ major, no longer minor.
D0 = lambda s, h, d, c: max(s, h) >= 5 and max(s, h) >= max(d, c)
A = node('1D-1H-1NT', D0, [
    ('2♦',  lambda s, h, d, c: s >= 5 and s >= h),
    ('2♥',  lambda s, h, d, c: h >= 5 and (s == 4 or BAL(s, h, d, c))),
    ('2♠',  lambda s, h, d, c: h >= 6 and max(s, d, c) <= 3),
    ('2NT', lambda s, h, d, c: h >= 6 and s <= 3 and max(d, c) == 4),
    ('3♣',  lambda s, h, d, c: h == 5 and s <= 3 and 4 <= c <= 5 and c >= d),
    ('3♦',  lambda s, h, d, c: h == 5 and s <= 3 and 4 <= d <= 5 and d > c),
    ('3♥',  lambda s, h, d, c: h >= 6 and c == 5),
    ('3♠',  lambda s, h, d, c: h >= 6 and d == 5),
    ('3NT', lambda s, h, d, c: h >= 6 and 5 <= s < h),
    ('4♣',  lambda s, h, d, c: h >= 6 and c == 6),
    ('4♦',  lambda s, h, d, c: h >= 6 and d == 6),
])
B = node('1D-1H-1NT-2D', lambda *x: A.get(x) == '2♦', [
    ('2♠',  lambda s, h, d, c: s >= 6 and max(h, d, c) <= 3),
    ('2NT', lambda s, h, d, c: BAL(s, h, d, c) or max(d, c) <= 3 and (h == 4 or s == h == 5)),
    ('3♣',  lambda s, h, d, c: c >= 4 and c >= d and not (s >= 6 and c >= 5)),
    ('3♦',  lambda s, h, d, c: d >= 4 and d > c and not (s >= 6 and d >= 5)),
    ('3♥',  lambda s, h, d, c: s >= 6 and c == 5),
    ('3♠',  lambda s, h, d, c: s >= 6 and d == 5),
    ('3NT', lambda s, h, d, c: s >= 6 and h >= 5),
    ('4♣',  lambda s, h, d, c: s >= 6 and c == 6),
    ('4♦',  lambda s, h, d, c: s >= 6 and d == 6),
])
# 6+ in suit m, no side suit: (6322), (6331), (7321), then 7330/7222/7303/7033
# with the long suit at index m; a minor gets five bids, so (7330) stays grouped.
def ONE(m, bids):
    out = [(bids[0], pattern(m, 6, (2, 2, 3))), (bids[1], pattern(m, 6, (1, 3, 3))),
           (bids[2], pattern(m, 7, (1, 2, 3)))]
    if len(bids) == 5:
        return out + [(bids[3], pattern(m, 7, (0, 3, 3))), (bids[4], pattern(m, 7, (2, 2, 2)))]
    seven = [[3, 3, 0], [2, 2, 2], [3, 0, 3], [0, 3, 3]]
    return out + [(b, exact(*r[:m], 7, *r[m:])) for b, r in zip(bids[3:], seven)]
STEPS = ['1NT', '2♣', '2♦', '2♥', '2♠', '2NT', '3♣', '3♦', '3♥', '3♠', '3NT', '4♣', '4♦', '4♥']
def steps(first, n):
    i = STEPS.index(first)
    return STEPS[i:i + n]

C = node('1D-1H-1NT-2D-2S', lambda *x: B.get(x) == '2♠', ONE(0, steps('3♣', 7)), 0)
D = node('1D-1H-1NT-2D-2NT', lambda *x: B.get(x) == '2NT', [
    ('3♦',  lambda s, h, d, c: BAL(s, h, d, c) and h <= 3),
    ('3♥',  lambda s, h, d, c: s >= 6 and h == 4),
    ('3♠',  lambda s, h, d, c: s == h == 5),
    ('3NT', exact(5, 4, 2, 2)),
    ('4♣',  exact(5, 4, 1, 3)),
    ('4♦',  exact(5, 4, 3, 1)),
], 0)
# 5+♥ with 4♠ or balanced: the same answers direct and after 1♣-1♦-1♥
EH = lambda bids, bal: ([(bids[0], lambda s, h, d, c: BAL(s, h, d, c))] if bal else []) + [
    (b, f) for b, f in zip(bids[bal:], [
        lambda s, h, d, c: s == 4 and h == 6, lambda s, h, d, c: s == 4 and h == 7,
        exact(4, 5, 2, 2), exact(4, 5, 1, 3), exact(4, 5, 3, 1), exact(4, 5, 0, 4), exact(4, 5, 4, 0)])]
E = node('1D-1H-1NT-2H', lambda *x: A.get(x) == '2♥', EH(steps('2NT', 8), True), 0)

# ------------------------------------------------------------ direct positives
# 1♣-1♥ shows 5+♠ (or BAL 13+, relayed as over 1♣-1NT), 1♣-1♠ shows 5+♥.
# Longest suit first; equal majors go to spades; a major beats an equal minor.
DS = lambda s, h, d, c: s >= 5 and s >= h and s >= d and s >= c
DH = lambda s, h, d, c: h >= 5 and h > s and h >= d and h >= c
def major(m, bal):
    """Shape answers with 5+ in major m (0 or 1): 2♥ takes BAL or 4 in the
    other major.  bal=False is the direct 8--12 table, where 2♦ is 5 + a minor;
    bal=True is the 13+ table after the 2♣ - 2♦ relay.  Spades: 3♣ is 5-5
    with clubs and 3♦ with hearts at 8--12; after the relay 3♣♦ are 5 + a
    minor and 3NT takes 5-5.  Hearts follow Viking: 13+ with 5♦ jumps to 3♣
    (5-5) or 3♠ (6-5), 2NT also takes 6♥ + 5♦ at 8--12, and after the relay
    3♣♦ are 5 + exactly 4 and 3♥♠ take 5♣."""
    if m:
        return [
            ('2♥',  lambda s, h, d, c: s == 4 or BAL(s, h, d, c)),
            ('2♠',  lambda s, h, d, c: h >= 6 and max(s, d, c) <= 3),
            ('2NT', lambda s, h, d, c: h >= 6 and s <= 3 and (max(d, c) == 4 or d == 5)),
            ('3NT', lambda s, h, d, c: h >= 6 and s >= 5),
            ('4♣',  lambda s, h, d, c: h >= 6 and c == 6),
            ('4♦',  lambda s, h, d, c: h >= 6 and d == 6),
        ] + ([
            ('3♣',  lambda s, h, d, c: h == 5 and s <= 3 and c == 4 and d <= 4),
            ('3♦',  lambda s, h, d, c: h == 5 and s <= 3 and d == 4 and c <= 3),
            ('3♥',  lambda s, h, d, c: h == 5 and c == 5),
            ('3♠',  lambda s, h, d, c: h >= 6 and c == 5),
        ] if bal else [
            ('2♦',  lambda s, h, d, c: h == 5 and s <= 3 and max(d, c) >= 4 and c != 5),
            ('3♦',  lambda s, h, d, c: h == 5 and c == 5),
            ('3♥',  lambda s, h, d, c: h >= 6 and c == 5),
        ])
    three = [('3♣', lambda s, h, d, c: s == 5 and c == 5),
             ('3♦', lambda s, h, d, c: s == h == 5)]
    return [
        ('2♥',  lambda s, h, d, c: h == 4 or BAL(s, h, d, c)),
        ('2♠',  lambda s, h, d, c: s >= 6 and max(h, d, c) <= 3),
        ('2NT', lambda s, h, d, c: s >= 6 and h <= 3 and max(d, c) == 4),
        ('3♥',  lambda s, h, d, c: s >= 6 and c == 5),
        ('3♠',  lambda s, h, d, c: s >= 6 and d == 5),
        ('3NT', lambda s, h, d, c: h >= 5 and (bal or s >= 6)),
        ('4♣',  lambda s, h, d, c: s >= 6 and c == 6),
        ('4♦',  lambda s, h, d, c: s >= 6 and d == 6),
    ] + ([
        ('3♣',  lambda s, h, d, c: s == 5 and h <= 3 and c >= 4 and c >= d),
        ('3♦',  lambda s, h, d, c: s == 5 and h <= 3 and d >= 4 and d > c),
    ] if bal else three + [
        ('2♦',  lambda *x: x[0] == 5 and x[1] <= 3 and max(x[2], x[3]) >= 4
                           and not any(p(*x) for _, p in three)),
    ])
def minor2(m, bids):
    """5 in major m + a minor, after 2♦ - 2♥: 4♣, 4♦, 5♣ (hearts only, which
    the direct 3♦ takes first), 5♦, 6♣, 6♦."""
    return list(zip(bids, [lambda *x: x[3] == 4 and x[3] >= x[2], lambda *x: x[2] == 4 and x[2] > x[3]]
        + ([lambda *x: x[3] == 5] if m else []) + [lambda *x: x[2] == 5, lambda *x: x[3] == 6, lambda *x: x[2] == 6]))
def fit(m, bids):
    """BAL or 5+ major m with 4 in the other: BAL, 6-4 and 7-4, then 5422,
    5413, 5431, 5404, 5440."""
    o = 1 - m
    sh = lambda a, b: (lambda *x: x[m] == 5 and x[o] == 4 and x[2] == a and x[3] == b)
    return list(zip(bids, [lambda *x: BAL(*x), lambda *x: x[m] >= 6] + [
        sh(2, 2), sh(1, 3), sh(3, 1), sh(0, 4), sh(4, 0)]))
def minor4(bids):
    """6+ major with a minor: 4 clubs, then diamonds."""
    return [(bids[0], lambda *x: x[3] == 4), (bids[1], lambda *x: x[2] >= 4)]
def doubleton(m, bids):
    """(5332) in major m: the doubleton, cheapest bid for the highest suit."""
    others = [i for i in range(4) if i != m]
    return [(b, lambda *x, i=i: x[m] == 5 and x[i] == 2 and BAL(*x)) for b, i in zip(bids, others)]

# 8--12 and 13+ bid 2♥ at the same level and share its relays.
# Over hearts, 13+ with 5♦ jumps to 3♣ or 3♠ instead of bidding 2♣.
for m, top, D, D13 in ((0, '1H-1S', DS, DS),
                       (1, '1S-1NT', DH, lambda s, h, d, c: DH(s, h, d, c) and d != 5)):
    A8 = node(top, D, major(m, False))
    A13 = node(top + '-2C-2D', D13, major(m, True))
    node(top + '-2D-2H', lambda *x, A=A8: A.get(x) == '2♦', minor2(m, steps('2♠', 5 + m)), m)
    # Viking skips 3♦ over hearts.
    FIT = steps('2NT', 7) if m == 0 else ['2NT', '3♣', '3♥', '3♠', '3NT', '4♣', '4♦']
    node(top + '-2H-2S', lambda *x, A=A8: A.get(x) == '2♥', fit(m, FIT), m)
    if m == 0:
        node(top + '-2H-2S-2NT-3C', lambda *x, A=A8: A.get(x) == '2♥' and BAL(*x), doubleton(m, steps('3♦', 3)))
    node(top + '-2C-2D-2H-2S', lambda *x, A=A13: A.get(x) == '2♥', fit(m, FIT))
    node(top + '-2NT-3C', lambda *x, A=A8: A.get(x) == '2NT', minor4(steps('3♦', 2)))
    node(top + '-2S-2NT', lambda *x, A=A8: A.get(x) == '2♠', ONE(m, steps('3♣', 7)), m)

# Balanced: 1♣-1NT (8--12) and 1♣-1♥-1♠-1NT (13+), both relayed with 2♣.
# No 5-card major (those are positives in the major).
DB = lambda s, h, d, c: BAL(s, h, d, c) and max(s, h) <= 4
NT = node('1NT-2C', DB, [
    ('2♦',  lambda s, h, d, c: s == 4),
    ('2♥',  lambda s, h, d, c: h == 4 and s <= 3),
    ('2♠',  lambda s, h, d, c: c == 5),
    ('2NT', lambda s, h, d, c: d == 5),
    ('3♣',  exact(3, 3, 4, 3)),
    ('3♦',  exact(3, 3, 3, 4)),
    ('3♥',  exact(3, 2, 4, 4)),
    ('3♠',  exact(2, 3, 4, 4)),
], 0)
def listed(bids, shapes):
    return [(b, exact(*x)) for b, x in zip(bids, shapes)]
node('1NT-2C-2D-2H', lambda *x: NT.get(x) == '2♦', listed(steps('2♠', 7), [
    (4, 3, 3, 3), (4, 4, 2, 3), (4, 4, 3, 2), (4, 3, 2, 4), (4, 3, 4, 2), (4, 2, 3, 4), (4, 2, 4, 3)]), 0)
node('1NT-2C-2H-2S', lambda *x: NT.get(x) == '2♥', listed(steps('2NT', 5), [
    (3, 4, 3, 3), (3, 4, 2, 4), (3, 4, 4, 2), (2, 4, 3, 4), (2, 4, 4, 3)]), 1)
node('1NT-2C-2S-2NT', lambda *x: NT.get(x) == '2♠', listed(steps('3♣', 3), [
    (3, 3, 2, 5), (3, 2, 3, 5), (2, 3, 3, 5)]), 3)
node('1NT-2C-2NT-3C', lambda *x: NT.get(x) == '2NT', listed(steps('3♦', 3), [
    (3, 3, 5, 2), (3, 2, 5, 3), (2, 3, 5, 3)]), 2)

# Minors: 1♣-2♣ shows 5+♦, 1♣-2♦ shows 5+♣.  A 4-card minor on the side goes
# to 2♥ and (5332) to 1NT, so the one-suiters here are 6+ with no 4-card suit.
# 13+ bids the shape; 8--12 bids the cheapest step and, after the relay, the
# same shape one step higher.
def minor(m, bids):
    """First relay answers over a 5+ minor m (2 or 3): the natural major bid
    takes 4-4, the other major next, else one-suited."""
    first, second = (1, 0) if m == 2 else (0, 1)
    return [(bids[0], lambda *x: x[first] >= 4),
            (bids[1], lambda *x: x[second] >= 4 and x[first] <= 3),
            (bids[2], lambda *x: max(x[0], x[1]) <= 3)]
def fitm(m, o, bids):
    """5+ minor m with 4+ in major o: 6+ in the minor first, then 5-4 shapes
    with the other major's length 2, 1, 3, 4 (and 0 only when the minor is clubs)."""
    om = 1 - o                      # the other major
    sh = lambda a, b: (lambda *x: x[m] == 5 and x[o] == 4 and x[om] == a and x[5 - m] == b)
    return [(bids[0], lambda *x: x[m] >= 6)] + list(zip(bids[1:], [
        sh(2, 2), sh(1, 3), sh(3, 1), sh(4, 0)]))
DD = lambda s, h, d, c: d >= 5 and d > s and d > h and c <= 3 and not BAL(s, h, d, c)
DC = lambda s, h, d, c: c >= 5 and c > s and c > h and c > d and d <= 3 and not BAL(s, h, d, c)
AD = node('2C-2D', DD, minor(2, steps('2♥', 3)))
node('2C-2D-2H-2S', lambda *x: AD.get(x) == '2♥', fitm(2, 1, steps('3♣', 5)), 2)
node('2C-2D-2S-2NT', lambda *x: AD.get(x) == '2♠', fitm(2, 0, steps('3♦', 5)), 2)
node('2C-2D-2NT-3C', lambda *x: AD.get(x) == '2NT', ONE(2, steps('3♦', 5)), 2)
AC = node('2D-2H', DC, minor(3, steps('2♠', 3)))
node('2D-2H-2S-2NT', lambda *x: AC.get(x) == '2♠', fitm(3, 0, steps('3♦', 5)), 3)
node('2D-2H-2NT-3C', lambda *x: AC.get(x) == '2NT', fitm(3, 1, steps('3♥', 5)), 3)
node('2D-2H-3C-3D', lambda *x: AC.get(x) == '3♣', ONE(3, steps('3♥', 5)), 3)

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

def arrow(x, y, deg, suit, length=8):
    """An arrow from (x, y) towards deg, where suit grows, labelled at its tip."""
    dx, dy = cos(radians(deg)), -sin(radians(deg))
    return (f'<path d="M{x:.1f},{y:.1f}l{length * dx:.1f},{length * dy:.1f}" '
            f'stroke="currentColor" marker-end="url(#arrow)"/>'
            f'<text x="{x + (length + 8) * dx:.1f}" y="{y + (length + 8) * dy:.1f}">{ent(SUITS[suit])}</text>')

def patch(idx, cells):
    """One lattice for a fixed length of suit idx.  Returns (width, height,
    svg) with the origin at the top-left corner.  A flat lattice marks
    at each end the suit that grows that way."""
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
    pad = 28 if flat and len(cells) > 1 else 0
    x0, y0 = min(xs) - R - pad, min(ys) - R - HEAD
    w, h = max(xs) - min(xs) + 2 * (R + pad), max(ys) - min(ys) + 2 * R + HEAD
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
    if pad:
        lo, hi = sorted(cells, key=lambda x: pos[x][0])[::len(cells) - 1]
        y = pos[lo][1] - y0
        labels.append('<g opacity=".6">'
            + arrow(pos[lo][0] - x0 - STEP / 2 - 2, y, 180, next(i for i in rest if lo[i] > hi[i]))
            + arrow(pos[hi][0] - x0 + STEP / 2 + 2, y, 0, next(i for i in rest if hi[i] > lo[i]))
            + '</g>')
    svg = (f'<text x="2" y="12" font-size="11" opacity=".6" text-anchor="start">'
           f'{ent(f"{x[idx]}={SUITS[idx]}")}</text>'
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
    marker = ('<marker id="arrow" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="6" '
              'markerHeight="6" orient="auto"><path d="M0 0L6 3L0 6Z"/></marker>'
              if 'url(#arrow)' in body else '')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" '
            f'style="display:block;margin:1em auto;width:100%;max-width:{W:.0f}px" fill="currentColor" '
            f'font-size="13" text-anchor="middle" dominant-baseline="middle">\n'
            '<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)"><path d="M0 0v6" stroke="currentColor" '
            f'stroke-opacity=".35"/></pattern>{marker}</defs>\n{body}\n</svg>\n')

if __name__ == '__main__':
    bad = 0
    os.makedirs(OUT, exist_ok=True)
    for name, mapping in CHECKED.items():
        for x, bid in mapping.items():
            if '/' in bid or bid == '?':
                print(f'{name}: {"".join(map(str, x))} -> {bid}', file=sys.stderr); bad += 1
    for name, (mapping, idx) in FIGURES.items():
        open(os.path.join(OUT, name + '.svg'), 'w').write(figure(mapping, idx))
    sys.exit(bool(bad))
