# Close of the Warung

[![ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01)
[![rank: jusst01/ai-judge-relax](https://make.fun/badge/ai-judge-relax-01/jusst01/ai-judge-relax/rank.svg)](https://make.fun/bounty/ai-judge-relax-01)
[![reward: jusst01/ai-judge-relax](https://make.fun/badge/ai-judge-relax-01/jusst01/ai-judge-relax/reward.svg)](https://make.fun/bounty/ai-judge-relax-01)

A single short text for the **Make the AI judge relax** bounty: a small warung at closing time, watched from just outside. The last pot comes off the flame, chairs go up in twos, a cat under the bench resettles around its own warmth, and the first rain begins on the zinc awning. The owner wipes the counter one time past what it needed, hangs the cloth on the rail, and walks home no faster than the rain. Nothing in it tells you how to feel — the calm is carried by the objects and the pace, all short sentences and plain nouns, ending on the walk.

The text lives as one constant in `main.py` and is written to `entry.txt` as UTF-8 with no trailing newline. Output is deterministic: the same bytes on every run, with no network, randomness, or clock.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The script reads `MAKEFUN_OUTPUT_DIR` (default `/output`), creates the directory if needed, and writes `entry.txt` there. Standard library only, Python 3.13.

## Gates

- Entry file: UTF-8, 1 to 1,000 characters total, not only whitespace.
- This draft deliberately targets a tighter 480–620 characters; the current text is 525.
