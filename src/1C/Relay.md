# Relay structure

The relays are based in parts on symmetric relay.  Describer resolves shape by
hand type:

1. **One-suited:** 5+ cards in one suit and no side 4-card suit
2. **Two-suited:** 4+ cards in two suits, and 9+ together
3. **Three-suited:** 4+ cards in three suits
4. **Balanced:** 4333, 4432, or 5332 with a 5-card minor

Each hand type has a default entry point, where the answers start.  A sequence
is *on track* if it starts there.  It *loses a step* if it starts one step
higher.

The same bids show the same relative shape.  For example, 3♦ always shows some
5431 in two-suited sequences.  Generally, cheaper bids show high shortage or
low length, and shapes are resolved by decreasing frequency.

## One-suited hands

The default entry point is 2♠.

| Step | Shape |
|-----|---|
| 2♠  | High shortage, or 6322 with 2 cards in the high suit
| 2NT | Middle shortage
| 3♣  | Equal shortage; if reached directly, 7222 or 6322 with 3 cards in the high suit
| 3♦  | 5332; if reached directly, low shortage
| 3♥  | 6331
| 3♠  | 7321
| 3NT | 7330, 2--3 RP
| 4♣+ | 7330, 4 RP and so on

For example, one-suited ♠ after [1♣ - 1♥ - 1♠ - 2♦ - 2♥](1H.md):

{{#include relay/1H-1S-2D-2H.svg}}

A one-suited minor rules out 5332, so 3♦ shows 6331 and so on.

## Two-suited hands

The default entry point is 2♥.  However, the entry point is 2NT when the 5+
card suit is known in an uneven two-suiter, namely 5+ cards in one suit and
exactly 4 in the other.  The entry point for a 5-5 two-suiter is 2♠.

| Step | Shape |
|-----|---|
| 2♥  | Reverser, 4 cards in the higher suit and 5+ in the lower
| 2♠  | 5-5 or longer
| 2NT | High shortage
| 3♣  | 5422
| 3♦  | 5431
| 3♥  | 6421
| 3♠  | 6430
| 3NT | 7420, 2--3 RP
| 4♣+ | 7420, 4 RP and so on

For example, 5+♣ and 4=♥ after [1♣ - 1♦ - 2♥ - 2♠](1D.md):

{{#include relay/1D-2H-2S.svg}}

To show 7411, show high shortage first and then bid 3NT.  This shifts 7420 up
one step.

After 2♠ showing 5-5, 2NT is the next relay.

| Step | Shape |
|-----|---|
| 3♣  | High shortage
| 3♦  | 5611 or 6511, resolved in that order
| 3♥  | 5521
| 3♠  | 5530
| 3NT | 5620
| 4♣  | 6520, 2--3 RP
| 4♦+ | 6520, 4 RP and so on

For example, both minors after [1♣ - 1♦ - 2♠ - 2NT](1D.md):

{{#include relay/1D-2S-2NT.svg}}

## Three-suited hands

Show the shortness first, then 4441, then 5440 with the 5-card suit from the
lowest to the highest.  Responder shows shortness as follows:

| Shortness | Responder |
|---|---|
| ♣ | 2♠, then 3♦+ over the 3♣ relay
| ♦ | 1♥, then 1NT, then 2♦, then 2NT, then 3♦+
| ♥ | 1♥, then 1NT, then 2♦, then 2♠, then 3♦+
| ♠ | 2♥, then 2NT+

Opener shows shortness as follows after [1♣ - 1♦](1D.md):

| Shortness | Opener |
|---|---|
| ♣ | 1♥, then 2♥, then 2NT, then 3♦+
| ♦ | 1♠, then 2♣, then 2♥, then 3♣, then 3♥+
| ♥ | 1♠, then 2♣, then 2♥, then 2NT, then 3♥+
| ♠ | 1♥, then 2♦, then 2♠, then 3♣+

## After shape resolves

### Relay points

Once describer has shown complete shape, the cheapest relay asks for the number
of RP.  Of course, 3NT is never a relay.

| Step | Responder  | Opener    | Balanced opener |
|---|------------|-----------|---|
| 1 | 2--3       | 9--10     | 12--13
| 2 | 4          | 11        | 14
| 3 | 5          | 12        | 15
| 4 | 6 and zoom | 13 and on | 16 and on

Generally, we try not to zoom from shape past 3NT without an RP ask.  We make
an exception when opener is describing because we have already lost a step and
these auctions are very slammish.  When 3♠ is the last shape bid, 3♠ may show
step 1 and 3NT all other steps.

### Honors

After RP, describer shows the parity of the top three honors in each suit:
halt on a suit with an even number of them and skip onward on an odd number.
Scan all suits excluding voids but including singletons, from the longest to
the shortest, higher suits first among equal length.  If RP were shown with
step 1, which has two possibilities, halt with the minimum and zoom into parity
otherwise.

After all parities, describer shows the RP in the first suit with only one top
honor, if any: halt if odd (the ace or the queen) and skip a step if even (the
king).  Describer may zoom into this answer but never beyond.  The ask after
that is for jacks.

### The 4♦ end signal

When the relay is below 4♦, 4♦ is an all-purpose signoff.  It puppets to 4♥,
after which relayer signs off in any suit.  Bidding 3NT is always a signoff as
well.

Describer usually respects these signoffs but may pull with substantial extras.
A semi-positive responder needs a full 6 RP and at least 12 HCP to pull, which
is very rare.  Opener needs at least 12 RP.  If shape is fully resolved,
continue as if partner had relayed.  Responder moves on to parity.  Opener
shows RP in steps with the first step being 12.  If shape is not fully
resolved, pulls are essentially natural.

### RKCB

If 4♦ is available as the end signal, other non-relay bids above 3NT are RKCB
with 1430 responses.  The cheapest asks in the longest suit of describer, the
next in the second longest, and so on, with ties broken by game order.  This
sets trumps and frees non-trump bids up as asking bids.  Asker skips a step to
skip the next honor.  The honors are asked in this order: the trump queen, then
kings from the longest suit and the highest among equals, then queens likewise.

## Relay breaks

### Before a game force

These breaks occur immediately after the response to 1♣, or after
[1♣ - 1♥ - 1♠](1H.md) and a rebid below 2♥ by responder.  Most of them are
natural and non-forcing, with a few exceptions particularly after
[1♣ - 1NT](1NT.md).  Responder may then make these non-forcing calls:

- Pass
- Bid notrump at the lowest level
- Raise opener's suit one level
- Rebid the suit already shown at the lowest level

Other bids are generally forcing.

### Keri-style breaks

These breaks apply after describer shows a balanced or three-suited hand via
2♦.  Then 2NT is natural and game-forcing, mostly to right-side notrump.

| 1♣ - 1♠ -<br>2♣ - 2♦ -<br>2NT - | |
|---------------|-|
| 3♣!           | Not 4333
| 3♣ - 3♦       | Ask, 4+♠♥
| 3♣ - 3♦ - 3♥♠ | 4=#
| 3♣ - 3♦ - 3NT | 0--3♠, 0--3♥
| 3♣ - 3♥♠      | 5=#
| 3♦!           | Any 4333
| 3♦ - 3♥♠      | Asks partner to raise with 4=#
| 3♥            | 5=♥, then 3♠ shows 5=♠
| 3♠            | 5=♠, 3=♥
| 3NT           | 5=♠, 2=♥

The same continuations apply in other auctions.  The 5-card major answers
exist only where describer may hold one.

Instead of 2NT, relayer's 3♣♦♥♠ shows a three-suited hand short in the other
suit of the same rank.

### Shortness-showing breaks

These breaks occur in a game-forcing relay sequence unless describer has just
bid 2♦ to show a balanced hand.  The cheapest break shows shortness in the
longest or first-shown suit of describer, the next break in the next suit, and
so on.  Describer then continues to show shape, losing a step or two.  However,

- 3NT by relayer is to play only if describer is strong in the short suit.
- The RP ask excludes the king and queen of the short suit, and every step
  promises 2 RP fewer.
- A subsequent RKCB excludes the short suit.

### Stopper asks

A relay break below 3NT asks for a stopper only when shape is fully resolved,
or when relayer has bypassed a chance to show shortness with a break.  Stopper
asks are only about 2- or 3-card fragments.  A stop is Qxx or Kx or better.
Steps skip 3NT.

| Answer  | Responder  | Opener | Stop |
|---------|------------|-------|---|
| 3NT     | 2 to bad 5 | 9--11 | Yes
| Step 1  | MIN        | MIN   | No
| Step 2  | MAX        | MAX   | No
| Step 3+ | Good 5+    | 12+   | Yes, zooming to RP and then parity

Over 3NT, the cheapest step asks for RP and 4NT invites 6NT.  Over steps 1 and
2, the cheapest step asks for RP outside the unstopped suit and new suits are
natural and non-forcing.

### Signoffs

If the relay would be 4♦ or above, any relay break is a signoff in the suit
bid.

## Interference during relays

Relays stay on as long as the opponents have cost us no more than two steps,
or equivalently less than a whole level, counted over the whole auction.
Relayer's double and redouble are for penalty.

- If they bid in front of relayer, pass is the relay, and describer's double is
  then the first step.
- If they bid in front of describer, pass is the first step, double the second,
  and so on.  Over the pass, relayer doubles to cash in or bids the next step to
  go on relaying.

Over a double of a response from 1♥ up, pass is the relay, redouble is for
penalty, and bids are natural.
