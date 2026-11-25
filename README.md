# Tell a Whole Story in 32 Characters

[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/itzalisha99/whole-story-32-chars/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/itzalisha99/whole-story-32-chars/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

A make.fun bounty entry: one Wi-Fi network name of at most 32 characters that
lands a joke and hints at a whole story.

## The entry

```
SheLeftMeForTheITGuyNextDoor
```

28 characters. She left me for the IT guy next door — the network name is the
revenge: the neighbour who fixes the Wi-Fi took the narrator's partner, and
now the whole street reads about it in their network list. Situation, character
and event in one line, no stock Wi-Fi joke in sight.

## How it works

`main.py` (Python standard library only) writes the entry to
`/output/entry.txt`. Before writing, a `validate()` gate mirrors the bounty
gate exactly: 1–32 characters of UTF-8 text, not only whitespace, a single
line. A bad entry raises an error instead of being written silently.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
