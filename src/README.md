# Introduction

![&spades; &hearts; &diams; &clubs;](favicon-2169f870.svg)

I have been studying forcing club systems since reading *Good, Better, Best* by
Jan Eric Larsson, whose simulations show that forcing club systems tend to
outperform other systems.  I believe opening 1♣ for all strong hands is a
superior treatment.

Blueberry Precision Club is a modernized mix of Blue Club, Precision Club,
Cottontail Club, and new ideas from BTU.  It is a 4-card major strong club
system.  It is highly experimental and subject to change without notice.

## Hand evaluation

- **HCP:** the well-known Milton Work's 4321 count
- **Total points:** HCP + distribution points (void = 3, singleton = 2, doubleton
  = 1, subtract 1 for each short suit with HCP)
- **Zar:** 6-4-2-1 + Zar distribution points (a + b + a - d, where the
  letters are the number of cards from the longest to the shortest suit)
- [**Fifths**](https://bridge.thomasoandrews.com/valuations/cardvaluesfor3nt.html):
  4.0--2.8--1.8--1.0--0.4, adjusted HCP for notrump contracts especially 3NT
- **BUM-RAP:** 4.5--3--1.5--0.75--0.25, adjusted HCP for suit contracts
- **NLTC:** Count 1.5--1.0--0.5 losers for each missing AKQ

NLTC is a good single hand evaluator but not very additive.  It suits preemptive
initial actions but not for showing supports.  I wrote a [blog article][nltc] on
that topic.

[nltc]: https://jdh8.org/nltc-a-good-single-hand-evaluator/

### Stopper

I evaluate stopper quality as [GIB] does.

- **Partial stop:** length + HCP = 4
- **Likely stop:** length + HCP = 5
- **Stop:** A, QJx, or length + HCP at least 7
- **Two stops:** length + HCP at least 8

[GIB]: https://www.bridgebase.com/doc/gib_descriptions.php

## Punctuations

Descriptions in bidding tables are dense in information.  To make them concise,
I use [abbreviations suggested by WBF][abbr].  Besides, for natural reading
flow, I use usual punctuation marks to connect conditions.  Their meanings are
usually self-explanatory in a bidding table.

[abbr]: http://www.worldbridge.org/wp-content/uploads/2017/04/Guidetocompletion.pdf

- **The comma (,)** works as **AND**.
- **The semicolon (;)** works as **OR**.
- **The colon (:)** follows general description of the call.

A notable example is the 1♣ opening in [Strawberry Polish Club](WJ.md).

## References

### General methods

- Jan Eric Larsson.  *Good, Better, Best: A comparison of bridge bidding
  systems and conventions by computer simulation*.  ISBN 978-1771402415
- Thomas Andrews.  [Thomas's Bridge Fantasia](https://bridge.thomasoandrews.com/valuations/)
- Bridge Base.  [GIB Bid Descriptions][GIB]

### Precision Club

- Daniel Neill.  *Standard Modern Precision: Getting from Here to There*.  ISBN
  978-1771401791
- Edward Piwowar.
  [PC - Meckwell Lite Precision Club](https://sites.google.com/view/bbaenglish/description-of-systems/pc-meckwell-lite-precision-club)

### Other strong clubs

- Arturo Franco, Marco Pancotti, and Daniel J. Neill.
  [Blue Team Club](https://bridgewithdan.com/wp-content/uploads/2019/07/BTC2000_gmeier.pdf)
- Jan Eric Larsson, Anu Uus, and George Wang.
  [Kaninklöver / Cottontail Club: A Cheatsheet (2022)](https://github.com/Egroegw/Kaninklover)
- Bo-Yin Yang.
  [Terrorist's Moscito, or Major-Oriented Strong Club, with Interpid Two Openers](https://bridgewithdan.com/wp-content/uploads/2022/01/terr_mosc.pdf)
