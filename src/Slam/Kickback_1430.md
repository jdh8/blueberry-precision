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

## Anti-spiral scan

Spiral scan[^spiral] is a relay scheme that maps lower steps to more important
features.  Anti-spiral scan, to a slam-forcing asking bid, attempts signing off
at 6X to deny the most important feature.  In general, the higher the step, the
fewer features it indicates.

[^spiral]: Regina Bridge Club.  [Spiral scanning after RKCB](https://reginabridge.com/content/conventions/Spiral%20scanning%20after%20RKCB.txt).  
Neil H. Timm.  [Using Spiral Scan Bids with Jacoby 2NT](https://www.bridgewebs.com/ocala/Spiral%20Scan%20Bids%20after%20Jacoby%202NT.pdf).

## Asking for the trump queen

To ask for the trump queen after 4Y+1 and 4Y+2, bid the cheapest step other than
5X.  If the asking bid is below 5X, we can stop at 5X with neither the trump
queen nor any useful void.

| -                   | Asking bid below 5X |
|---------------------|---------------------|
| 5X                  | No trump Q
| 6X                  | No trump Q but a useful void
| \[5X+1..6X&minus;1] | Trump Q and *this* king
| 5NT                 | Trump Q but no side kings

If the asking bid is above 5X, it is slam-forcing and the anti-spiral scan comes
into play.  The cheapest step catches all unallocated side kings.  This
agreement helps further asking.

| 5Z                  | Asking bid above 5X |
|---------------------|---------------------|
| 6X                  | No trump Q
| 6X&minus;1          | Trump Q but no side kings
| \[5Z+2..6X&minus;2] | Trump Q and *this* king
| 5NT                 | Trump Q and the king of X&minus;1
| 5Z+1                | Trump Q and an unallocated side king

## Asking for side kings

After the queen ask is located (or not needed because the previous response
shows 2 or 5 key cards), the next available step other than 5X asks only for
side kings.

| 5Z                  | Asking bid |
|---------------------|------------|
| 6X                  | No side kings
| \[5Z+2..6X&minus;1] | *This* king
| 5NT                 | The king of Z
| 5Z+1                | An unallocated side king

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
