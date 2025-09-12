# Notation on suit variables

In competitive and defensive bidding, combinations of calls grow factorially.
It is convenient to replace unknown suits with variables, just like how algebra
brings computation to a higher level.

This book usually follows principles introduced in BML and [CSS][css].

[css]: https://developer.mozilla.org/en-US/docs/Web/CSS

## Ordered suit variables

X, Y, Z are suit variables that satisfy X < Y < Z.  They are also distinct from
the other suits in the same auction.  For example:

- (1Y) 2X matches (1♥) 2♣ but not (1♥) 2♠.
- (1Y) 2Z matches (1♥) 2♠ but not (1♥) 2♣ or (1♥) 2NT.
- (1M) 2X matches (1♥) 2♣ but not (1♥) 2♥.

## Precedence

Multiple rules may match the same auction.  The rule with the highest
precedence applies.

### Precedence of strain symbols

Concrete strain > suit class > suit variable

- Concrete strain: ♣, ♦, ♥, ♠, NT
- Suit class: M, m, <abbr title="red suit">R</abbr>, <abbr title="black suit">B</abbr>
- Suit variable: X, Y, Z

### Juxtaposition of strain symbols

Juxtaposition of strain symbols produces multiple rules, similar to `|` in
regular expression.  For example, 2MNT is a valid expression that matches
2♥, 2♠, and 2NT.

### Specificity of rules

Specificity is determined like CSS [specificity].  The rule with the most concrete
strains wins.  Then we compare the number of suit classes.  Note that juxtaposition
expands to multiple rules instead of one.  For example:

- 1♥-2X > 1R-2B
- Comparing 1MNT-2X and 1X-1R:
    - 1M-2X = 1X-1R
    - 1NT-2X > 1X-1R

[specificity]: https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity

### Precedence of rules

The most specific rule applies.  If there are multiple rules with the same
specificity, compare specificity lexicographically.  For example, 1M-2X > 1X-1R
because 1M is more specific than 1X.  If there are still multiple rules with the
same specificity, the last rule applies, like CSS and laws but not BML.
