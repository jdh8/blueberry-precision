# ![Blueberry Precision Club](favicon-2f8f5d7c.svg)

Blueberry Precision Club is a modernized Precision Club mixing new ideas from
BTU.  It is a 5-card major strong club system.  It is highly experimental and
subject to change without notice.

## Hand evaluation

- **HCP:** the well-known Milton Work's 4321 count
- **Total points:** HCP + distribution points (void = 3, singleton = 2, doubleton
  = 1, subtract 1 for each short suit with HCP)
- [**Fifths**](https://bridge.thomasoandrews.com/bridge/valuations/cardvaluesfor3nt.html):
  4.0--2.8--1.8--1.0--0.4, adjusted HCP for notrump contracts especially 3NT
- **BUM-RAP:** 4.5--3--1.5--0.75--0.25, adjusted HCP for suit contracts
- **NLTC:** Count 1.5--1.0--0.5 losers for each missing AKQ

NLTC is a good single-hand evaluator but not very additive.  It suits preemptive
initial actions but not for showing support.  I wrote a [blog article][nltc] on
that topic.

[nltc]: https://jdh8.org/nltc-a-good-single-hand-evaluator/

### Stopper

I evaluate stopper quality as [GIB] does.

- **Partial stop:** length + HCP = 4
- **Likely stop:** length + HCP = 5
- **Stop:** A or QJx or length + HCP at least 7
- **Two stops:** length + HCP at least 8

[GIB]: https://www.bridgebase.com/doc/gib_descriptions.php

## Punctuation

Descriptions in bidding tables are dense in information.  To make them concise,
I use [abbreviations suggested by WBF][abbr] in tables and words in paragraphs.
Familiar convention names such as RKCB stay abbreviated in paragraphs too.
Strength ranges and suit lengths keep their compact notation.

[abbr]: http://www.worldbridge.org/wp-content/uploads/2017/04/Guidetocompletion.pdf

- **All conditions:** write `A and B` or `A, B`; for longer lists, write
  `A, B, and C` or `A, B, C`.  For example, `INV, 9--11, 6+♣`.
- **Alternatives:** write every `or` explicitly: `A or B or C`.
- **Grouping:** use parentheses when mixing conditions and alternatives.
  `FG, (5+♥ or BAL 13+)` is game-forcing with either hearts or a strong balanced
  hand.  `(5+♦, 4+♣) or 6+♦` describes two cases.
- **Long alternatives:** keep separate lines, with an explicit `or` between
  alternatives.  Colons and semicolons have their ordinary punctuation meanings.

Parentheses within shapes such as `33(43)` still identify suits whose lengths
may swap order.  Compact suit notation and the `(R)` relay tag are unchanged.

A notable example is the [1♣ opening in *Strawberry Polish Club*](https://polish.club/Openings.html).

## References

### General methods

- Jan Eric Larsson.  *Good, Better, Best: A comparison of bridge bidding
  systems and conventions by computer simulation*.  ISBN 978-1771402415
- Thomas Andrews.  [Thomas's Bridge Fantasia](https://bridge.thomasoandrews.com/bridge/valuations/)
- Bridge Base.  [GIB Bid Descriptions][GIB]

### Precision Club

- Daniel Neill.  *Standard Modern Precision: Getting from Here to There*.  ISBN
  978-1771401791
- Edward Piwowar.
  [PC - Meckwell Lite Precision Club](https://sites.google.com/view/bbaenglish/description-of-systems/pc-meckwell-lite-precision-club)

### Other strong clubs

- Arturo Franco, Marco Pancotti, and Daniel J. Neill.
  [*Blue Team Club*](https://bridgewithdan.com/wp-content/uploads/2019/07/BTC2000_gmeier.pdf)
- Jan Eric Larsson, Anu Uus, and George Wang.
  [Kaninklöver / Cottontail Club: A Cheatsheet (2022)](https://github.com/Egroegw/Kaninklover)
- Bo-Yin Yang.
  [*Terrorist's Moscito, or Major-Oriented Strong Club, with Interpid Two Openers*](https://bridgewithdan.com/wp-content/uploads/2022/01/terr_mosc.pdf)
