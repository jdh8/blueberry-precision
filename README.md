Chen-Pang He (jdh8)'s bridge bidding systems
============================================

**Note:** This project is undergoing [transition to mdBook][book].  It becomes
default when complete.

This repository contains my bidding systems.  These documents are in the Bridge
Bidding Markup Language (BML).  Please use [my fork][fork] for now until
gpaulissen/bml#21 gets fixes.

[book]: https://jdh8.github.io/bridge-systems/book/
[fork]: https://github.com/jdh8/bml
[mdBook]: https://github.com/rust-lang/mdBook

The below are my pet forcing club bidding systems.  I believe bidding 1♣ for
all strong hands is a superior treatment.

- [Strawberry Polish Club](https://jdh8.github.io/bridge-systems/wj.htm)
- [Blueberry Club](https://jdh8.github.io/bridge-systems/blue.htm)
- [Defensive bidding system](https://jdh8.github.io/bridge-systems/defense.htm)

The [distribution syntax and abbreviations][syntax] are provided by WBF.

[syntax]: http://www.worldbridge.org/wp-content/uploads/2017/04/Guidetocompletion.pdf

Building HTML and BSS files
---------------------------

First, install the BML converters.

```sh
git clone https://github.com/jdh8/bml.git
pip install .
```

Then, `make` whenever you want to generate or update files.

```sh
make -j8
```
