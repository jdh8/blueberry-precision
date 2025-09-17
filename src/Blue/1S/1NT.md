# Non-forcing 1NT

Opener passes with balanced minimum.

| 1♠-1NT | CONST--INV, 0--3♠ |
|--------|-------------------|
| 2X     | 4+#, 5+♠
| 2♠     | 11--13, 6+♠.  13--15, 5=♠
| 2NT    | 14--15, 6=♠, at most ♠A9
| 3♣♦    | 14--15, 5+#, 4+♠
| 3♥     | 14--15, 5+♥, 5+♠
| 3♠     | 14--15, 6+♠
| 3NT!   | MAX P/C, 6+♦♣, 4=♠
| 4X     | MAX, 5+#, 6+♠

The threshold of suit quality is based on [Binky Points][binky]:

> ```
> Holding     NT   Suit
>  KQ9xxx  -0.13  -0.08
>  A9xxxx  -0.12  -0.02
>  KQTxxx   0.00   0.02
>  KQT9xx   0.06   0.06
> ```
>
> ---[`holdings.new.txt`](https://bridge.thomasoandrews.com/valuations/data/holdings.new.txt),
> Binky Points computed by Thomas Andrews in 2008

[binky]: https://bridge.thomasoandrews.com/valuations/additive.html
