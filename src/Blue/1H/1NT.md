# Non-forcing 1NT

Opener may rebid a 3-card minor due to protection from the impossible 2♠.

| 1♥-1NT | CONST--INV, 0--3♠, 0--3♥ |
|--------|--------------------------|
| 2♣      | 3+♣, 5+♥
| 2♦      | UNBAL 3+♦, 5+♥
| 2♥      | 11--13, 6+♥.  13--15, 5=♥
| 2♠      | 14--15, 4+♠, 5+♥
| 2NT     | 14--15, 6=♥, at most ♥A9
| 3♣♦     | 14--15, 5+#, 4+♥
| 3♥      | 14--15, 6+♥
| 3NT!    | MAX P/C, 6+♦♣, 4=♥
| 3♠, 4♣♦ | MAX, 5+#, 6+♥

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
