# Relay-lattice visualization: search for bridge precedents

Research date: 2026-10-26.

## Finding

No matching visualization by another bridge author was found in the sources
searched. The relay manuals inspected present shape-to-bid mappings using
tables, branching columns, and indented auction descriptions. That supports
calling Blueberry's presentation an apparently unusual application to bridge;
it does **not** establish that nobody has drawn it before.

## What would count as a match?

The mechanism in [relay.py](../relay.py), illustrated by
[the 1♣–1NT–2♣ diagram](../src/1C/relay/1NT-2C.svg), has several distinct parts:

1. A relay node defines a map from the exact shapes still possible to the next
   response.
2. One suit's length selects a panel. Within a panel, the other three lengths
   have a fixed sum, `13 - indexing_suit_length`.
3. Those three lengths determine positions on a triangular lattice, drawn as
   hexagonal cells. Neighboring positions transfer one card between two of
   those suits.
4. Cells show their response and sometimes their exact shape; stronger borders
   separate different responses, leaving adjacent same-response cells as one
   region. Holes and conflicting rules can also be marked.

A bidding tree or a table of shapes addresses the same relay information but
does not supply this geometric presentation. Nor does a picture of one bridge
hand constitute a map of possible shapes.

## Bridge-author sources checked

The PDF page references below were checked visually after rendering, as well
as through text extraction. They are representative shape-showing sections,
not a claim to have visually inspected every page of every book.

| Source and date | Relevant presentation inspected | Relationship to Blueberry |
| --- | --- | --- |
| Andrei Sharko, *The Symmetric Relay Contract Bridge Bidding System Made Easy*, ©2004 | Printed/PDF pp. 12–18: Tables 7, 9, 12–14 show single-suiter, two-suiter, three-suiter, and balanced relay structures, with branching columns and auction examples. | A clear earlier presentation of relay shape-to-response mappings, but the positions are organized by auction steps, not suit-length coordinates. No matching lattice in these sections. [Author's text](https://www.pagat.com/it/docs/SymmetricRelay.pdf#page=12). |
| Bo-Yin Yang, with Ruey-Lun Lin, Jessica Y. Lee, and David Morgan, *Terrorist's Moscito*, 28 March 2000 | Chapter 5, printed pp. 37–43 / PDF pp. 39–45: theoretical discussion and Tables 5A–5B for one- and two-suited relay structures. | Explicit discussion of distribution-to-bidding-sequence mappings, Fibonacci capacity, symmetry, and branching; the actual charts are tables and indented sequences, without shape-space geometry. [Author's dated manuscript, archived copy](https://relaysystems.wordpress.com/wp-content/uploads/2021/10/terrorist-moscito.pdf#page=39). |
| Joon Pahk and Leo Zelevinsky, *Transfer Oriented Symmetric Relay Precision*, version 1.0.6, 5 November 2008 | Printed/PDF pp. 8–11: single-, two-, three-suited, and flat-hand relay structures. | Numbered rules and indented lists describe the partition of shapes and the successive bids. No matching geometric plot in these sections. The version and release date are on p. 1. [Author-hosted notes](https://www.bantha.org/~pahk/bridge/tosr/TOSR_1c.pdf#page=8). |
| Paul Marston's *MOSCITO – 2007* notes, as attributed by David Morgan | PDF pp. 2–3, especially §4.1–4.4: one-suit, two-suit, balanced, and Relay Stayman templates. | Compact response tables, including exact shapes in columns. No matching lattice in the four-page document. [Notes](https://relaysystems.wordpress.com/wp-content/uploads/2021/10/moscito-2007.pdf#page=3); [Morgan's attribution and links to the 2004, 2005, and 2007 notes](https://relaysystems.wordpress.com/symmetric-relay-systems/). |

Kurt Schneider's *A Better Symmetric Relay* (10 October 2022) is another
related conceptual example: Charron Relay partitions hand patterns using
unique-length suits and describes tracks and switches. The article uses
prose, lists, tables, and auctions; the material recovered did not provide a
triangular or hexagonal map of those partitions. This is a different relay
design, not evidence of the same visualization. [Schneider's article](https://bridgewinners.com/article/view/a-better-symmetric-relay/).

## The geometry has established precedents outside bridge

Three components with a fixed sum are standard ternary/simplex-plot data.
TernaryPlot.com's own documentation describes these plots as triangular plots
for three components summing to a constant, with points, lines, areas, and
labels. [Official documentation](https://www.ternaryplot.com/docs/intro).

Amit Patel's *Hexagonal Grids* describes cube coordinates constrained by
`q + r + s = 0`, and the resulting planar hexagonal grid. His guide is dated
March 2013–April 2026. [Coordinate explanation](https://www.redblobgames.com/grids/hexagons/#coordinates-cube).
Translating a fixed-sum triple of suit lengths gives that same coordinate
constraint. Thus the underlying geometry is established; the potentially
distinctive feature here is its use to display and inspect a bridge relay's
response regions. This mathematical comparison is an inference from the
local implementation and those descriptions, not evidence that either source
influenced Blueberry or that its bridge application is historically first.

## Search limits

Searches combined bridge/relay/hand-shape terms with lattice, triangular grid,
hexagon, honeycomb, ternary, barycentric, simplex, tetrahedron, diagram, graph,
and visualization. Searches also targeted Symmetric Relay, Moscito, Viking
Precision, Ultimate Club, Fibonacci relay structures, and Suspensor.
Results about electronic relays and ordinary bridge-hand diagrams were
excluded. The search found plenty of relay charts but no demonstrated match
to the criteria above.

The original Jones–Kerr *Symmetric Relay* book was **not directly inspected**.
Sharko's preface dates that book to 1980, but his later exposition cannot
establish what every diagram in the original looked like. [Sharko, preface,
p. 2](https://www.pagat.com/it/docs/SymmetricRelay.pdf#page=2).
Neither the full *Ultimate Club* nor the full *Viking Precision Club* book was
inspected. Nick Hughes's publisher-hosted sample of *Symmetric Relay*
(©2020) was recovered, but its contents place the main relay-structure chapter
at p. 17, beyond the sample's opening chapter; it cannot rule out a diagram
elsewhere in the book. [Publisher's sample, contents and copyright pages](https://ebooksbridge.com/uploads/files/products/samples/776/SAMPLEHONORS_SymmetricRelay.pdf).

Private partnership notes, older print-only material, unindexed images, and
other-language publications remain possible sources of an earlier example.
The defensible answer is **“I have not found another bridge author using this
particular visualization,”** rather than a claim of proven priority.
