#!/usr/bin/env python3
"""Relay phase diagrams.

Each relay node maps the shapes still possible at that node to a bid.  This
script states that map as ordered rules, checks that every shape gets exactly
one bid, and draws the map as hexagonal lattices (one per length of an indexing suit;
of the other three, the highest ranking points up, the next down-left and
the lowest down-right) into src/1C/relay/*.svg, which 1D.md includes.
Borders are drawn where the bid changes; a hatched cell is a hole or a clash.

Run it by hand after editing the rules.  Exit code 1 on any hole or clash.
"""
from math import sqrt
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

# ---------------------------------------------------------------- 1♣-1♦-1♥-1NT
# The tables leave longest-suit precedence implicit; the rules spell it out.
# Responder: FG, 5+ major, no longer minor.
D0 = lambda s, h, d, c: max(s, h) >= 5 and max(s, h) >= max(d, c)
A = solve(D0, [
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
B = solve(lambda *x: A.get(x) == '2♦', [
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
C = solve(lambda *x: B.get(x) == '2♠', [
    ('3♣',  lambda s, h, d, c: s == 6 and sorted((h, d, c)) == [2, 2, 3]),
    ('3♦',  lambda s, h, d, c: s == 6 and sorted((h, d, c)) == [1, 3, 3]),
    ('3♥',  lambda s, h, d, c: s == 7 and sorted((h, d, c)) == [1, 2, 3]),
    ('3♠',  lambda s, h, d, c: (s, h, d, c) == (7, 3, 3, 0)),
    ('3NT', lambda s, h, d, c: (s, h, d, c) == (7, 2, 2, 2)),
    ('4♣',  lambda s, h, d, c: (s, h, d, c) == (7, 3, 0, 3)),
    ('4♦',  lambda s, h, d, c: (s, h, d, c) == (7, 0, 3, 3)),
])
D = solve(lambda *x: B.get(x) == '2NT', [
    ('3♦',  lambda s, h, d, c: BAL(s, h, d, c) and h <= 3),
    ('3♥',  lambda s, h, d, c: s >= 6 and h == 4),
    ('3♠',  lambda s, h, d, c: s == h == 5),
    ('3NT', lambda s, h, d, c: (s, h, d, c) == (5, 4, 2, 2)),
    ('4♣',  lambda s, h, d, c: (s, h, d, c) == (5, 4, 1, 3)),
    ('4♦',  lambda s, h, d, c: (s, h, d, c) == (5, 4, 3, 1)),
])
E = solve(lambda *x: A.get(x) == '2♥', [
    ('2NT', lambda s, h, d, c: s <= 3),
    ('3♣',  lambda s, h, d, c: s == 4 and h == 6),
    ('3♦',  lambda s, h, d, c: s == 4 and h == 7),
    ('3♥',  lambda s, h, d, c: (s, h, d, c) == (4, 5, 2, 2)),
    ('3♠',  lambda s, h, d, c: (s, h, d, c) == (4, 5, 1, 3)),
    ('3NT', lambda s, h, d, c: (s, h, d, c) == (4, 5, 3, 1)),
    ('4♣',  lambda s, h, d, c: (s, h, d, c) == (4, 5, 0, 4)),
    ('4♦',  lambda s, h, d, c: (s, h, d, c) == (4, 5, 4, 0)),
])
# figure name -> (mapping, index of the suit that picks the lattice)
# A and B are rule-based and only checked; figures are for nodes that enumerate shapes
FIGURES = {'1NT-2D-2S': (C, 0), '1NT-2D-2NT': (D, 0), '1NT-2H': (E, 0)}
CHECKED = {'1NT': A, '1NT-2D': B, **{k: v[0] for k, v in FIGURES.items()}}

# ---------------------------------------------------------------------- drawing
STEP = 46                      # lattice spacing = cell width
R = STEP / sqrt(3)             # hexagon circumradius (pointy-top)
GAP, MAXW = 28, 720
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
    from math import cos, sin, radians
    return f'{x + R * cos(radians(deg)):.1f},{y - R * sin(radians(deg)):.1f}'

def patch(idx, cells):
    """One lattice for a fixed length of suit idx.  Returns (width, height,
    svg) with the origin at the top-left corner."""
    rest = [i for i in range(4) if i != idx]
    pos = {x: centre(*(x[i] for i in rest)) for x in cells}
    xs = [p[0] for p in pos.values()]; ys = [p[1] for p in pos.values()]
    x0, y0 = min(xs) - R, min(ys) - R - 16
    w, h = max(xs) - min(xs) + 2 * R, max(ys) - min(ys) + 2 * R + 16
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
                hard.append(f'M{vertex(cx, cy, deg - 30)}L{vertex(cx, cy, deg + 30)}')
        labels.append(f'<text x="{cx:.1f}" y="{cy - 1:.1f}">{ent(bid)}</text>'
                      f'<text x="{cx:.1f}" y="{cy + 11:.1f}" font-size="8.5" opacity=".6">'
                      f'{"".join(map(str, x))}</text>')
    svg = (f'<text x="2" y="12" font-size="11" opacity=".6" text-anchor="start">'
           f'{ent(f"{x[idx]}={SUITS[idx]}")}</text>'
           f'<path d="{"".join(faint)}" fill="none" stroke="currentColor" stroke-opacity=".15"/>'
           + (f'<path d="{"".join(hatch)}" fill="url(#hatch)"/>' if hatch else '')
           + f'<path d="{"".join(hard)}" fill="none" stroke="currentColor" stroke-width="1.5"/>'
           + ''.join(labels))
    return w, h, svg

def figure(mapping, idx):
    """Pack one patch per length of suit idx into rows no wider than MAXW."""
    patches = [patch(idx, {x: b for x, b in mapping.items() if x[idx] == v})
               for v in sorted({x[idx] for x in mapping})]
    body, x, y, rowh = [], 0, 0, 0
    for w, h, svg in patches:
        if x and x + w > MAXW:
            x, y, rowh = 0, y + rowh + GAP, 0
        body.append(f'<g transform="translate({x:.1f},{y:.1f})">{svg}</g>')
        x, rowh = x + w + GAP, max(rowh, h)
    W, H = MAXW if y else x - GAP, y + rowh
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" '
            f'style="display:block;margin:1em auto;width:100%;max-width:{W:.0f}px" fill="currentColor" '
            f'font-size="13" text-anchor="middle" dominant-baseline="middle">\n'
            '<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)"><path d="M0 0v6" stroke="currentColor" '
            'stroke-opacity=".35"/></pattern></defs>\n'
            + '\n'.join(body) + '\n</svg>\n')

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
