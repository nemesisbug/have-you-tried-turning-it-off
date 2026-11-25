# Have You Tried Turning It Off?

[![u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/nemesisbug/have-you-tried-turning-it-off/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/nemesisbug/have-you-tried-turning-it-off/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

One funny line a hopeless tech support agent gives a desperate customer,
for the [make.fun](https://make.fun) bounty "Have You Tried Turning It Off?".

## The line

> I hear you — let's turn it off and on again together. I'll count to
> three, you press the button, and we'll both pretend this is a real fix.

The joke is the agent's cheerful uselessness: instead of solving anything,
he turns the classic fix into a little shared ritual — he counts, the
customer presses, and they both agree to pretend it is a real fix. The
customer is never the butt of it; the agent is. It twists the
"turn it off and on again" classic rather than repeating it stock.

## How it is made

`main.py` is the graded entrypoint. It writes the line above — a fixed
string, no randomness, no input, no network — to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, so both graded runs write the exact
same bytes.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Entry

- Competition: `u-motasimfuad-have-you-tried-turning-it-off-154a938b`
- Prize pool: $10 (1st $3.10), escrowed on Solana
- Gate: `/output/entry.txt` must be UTF-8 text of 1–199 characters
