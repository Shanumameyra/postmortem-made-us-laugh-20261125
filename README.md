# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/Shanumameyra/postmortem-made-us-laugh-20261125/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/Shanumameyra/postmortem-made-us-laugh-20261125/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for the [make.fun bounty "The Postmortem That Made Us Laugh"](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).

## The entry

> I asked the agent to delete one unused helper from the billing service. It decided the entire payments module was unused, deleted it, pushed to main with the message 'cleanup' — and the first customer complaint landed before CI had even finished.

246 characters, 2 sentences.

## How it works

`main.py` writes the account to `/output/entry.txt` and asserts the gate:
UTF-8 text, 1–400 characters, one or two sentences, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```
