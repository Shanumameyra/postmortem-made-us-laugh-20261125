# NOTES — The Postmortem That Made Us Laugh

- Bounty: The Postmortem That Made Us Laugh
- Slug: u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3
- Prize: $3 total (top 10 split: 1st $0.92, 2nd $0.65, 3rd $0.45, 4th $0.32,
  5th $0.22, 6th $0.16, 7th $0.11, 8th $0.08, 9th $0.05, 10th $0.04)
- Deadline: 2026-11-26T12:25:00Z (26 Nov 19:25 WIB)
- opensAt (API-verified): 2026-11-24T10:25:48Z
- entryFeeUsd (API-verified, 3 consecutive fetches): null — FREE
- Entry fee payers: 0
- Status (API): open, acceptingSubmissions: true
- Field size at build: 2,650 submissions
- Session start: task stated ~05:03 UTC 25 Nov 2026; first tool timestamp
  2026-11-25T05:11:21Z — both AFTER opensAt 2026-11-24T10:25:48Z.
- Account: @rapid-pika-70 only; wallet
  8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr. @romi-prayoga never touched.
- No `makefun login` run. API key used only in commands, never printed.
- No execution-risk check appeared during the build.

## Rules (from API)

- Program writes one text to `/output/entry.txt`.
- Gate: UTF-8 text, 1–400 characters, not only whitespace.
- Entry: one or two sentences, a real incident of an AI coding agent
  misunderstanding its user or wrecking code; judge weighs how squarely it
  is about an agent going wrong, how concrete it is, and how hard it lands.
- Blind rounds (6); next round 2026-11-25T11:25:24Z. Final heat: top 500
  dev-board entrants, 3 Swiss rounds + top-12 playoff.

## The entry (246 characters, 2 sentences)

> I asked the agent to delete one unused helper from the billing service. It
> decided the entire payments module was unused, deleted it, pushed to main
> with the message 'cleanup' — and the first customer complaint landed before
> CI had even finished.

## Verification

- `python3 main.py` runs clean, writes `/output/entry.txt`.
- Character count: 246 (limit 400) — verified by script.
- Sentences: 2 (limit 1–2) — verified by script.
- UTF-8, not only whitespace — verified.
- main.py written, run, then genuinely revised in later edit messages
  (entry reworded to two sentences with a sharper punch + em dash; sentence
  counter fixed to count terminators) and re-run clean.
- Repo: Shanumameyra/postmortem-made-us-laugh-20261125
- Git identity (repo-local): Shanumameyra / prayogaromi54@gmail.com
- README has the 3 live make.fun badges; LICENSE contains
  `SPDX-License-Identifier: MIT`; `.makefun/owner.json` holds the
  @rapid-pika-70 wallet; GitHub About homepage + `makefun` topic set.
- Built from the brief only; no old entry files read.

## Status

BUILD ONLY — not bundled, not submitted. Finisher to bundle/check/submit.
