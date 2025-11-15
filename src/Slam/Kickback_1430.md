# Kickback RKCB 1430

RKCB is a powerful modern tool for slam bidding.  It checks quality of trumps
and controls at the same time.  Nevertheless, its location at 4NT can be
inconvenient when the agreed trump is a minor suit.  As per the useful space
principle, the fix is to move RKCB down to 4X+1.  Sometimes, this treatment
conflicts with an existing natural 4Y.  I propose the following algorithm to
resolve where RKCB is.

1. Try interpreting 4♥♠ as natural and non-forcing.
2. Above 4X, the lowest remaining step 4Y becomes RKCB.
3. If Y is a suit, 4NT **denies** controls in that suit.

- **Key cards** are the 4 aces and the trump king.
- The 10th trump equates to the trump queen.

| 4Y- | RKCB |
|-----|------|
| +1  | 1 or 4 key cards
| +2  | 0 or 3 key cards
| +3  | 2 or 5 key cards without the trump queen
| +4  | 2 or 5 key cards with the trump queen

| Combined key cards | Action |
|--------------------|--------|
| 0--1               | Break up with your partner
| 2--3               | S/O at 5X or 4NT
| 4                  | S/O at 6X or 6NT
| 5                  | Explore for grand slam

## Anti-spiral scan

Spiral scan is a relay scheme that maps lower steps to more important features.
Anti-spiral scan, on the other hand, signs off at a small slam to deny the most
important feature.  In general, for the available steps up to 6X, the higher the
step, the fewer features it indicates.  This treatment uses the fact that grand
slam exploration is slam forcing.  The negative step is almost always followed
by a signoff at a small slam.  Move the negative step up to 6X to sign off
already.

## Asking for the trump queen

## Asking for side kings

## 1430 vs 0314

> If the RKC call is 4T+1, there is no need for 1430 since the queen ask will be
> below 5T after both responses. It is preferable to play 0314 since more
> maneuvering room may be needed after the 0 response. For example, if a minor
> is trumps you may want to play in 4NT rather than 5 of the minor when off 2
> aces.
>
> If 4T+1 is not available and the RKC call is 4T+2, then 1430 is superior. It
> is more likely that you will want to make the queen ask below 5T when partner
> has 1 keycard than when he has 0 key cards, and 1430 caters to that. In fact,
> this is the sole reason 1430 was invented.
>
> The theoretically best approach is to play 0314 when the RKC call is 4T+1, but
> to play 1430 when the RKC call is 4T+2. We don't do this because we believe
> that the danger of forgetting in the heat of battle outweighs the small gain.
>
> ---[Kit Woolsey, 2017](https://bridgewinners.com/article/view/kickback-and-1430/#c509117),
> "Kickback and 1430" on Bridge Winners

I choose 1430 over 0314 right after reading the analysis above.

- 4♦{RKCB in ♣} 4♠-4NT
- 4♥{RKCB in ♦} 4NT-5♣

The only case we need to use 4NT for the queen ask is 4♦{RKCB in ♣} 4♠-4NT.
That is far less common than bypassing natural 4♥♠ for RKCB.
