# Daily Learning

Turn a subject and a goal into short, researched lessons with something to practise.

**Status: early test version.** This repository contains portable instructions, not a hosted service. Your AI app supplies browsing, document creation, memory and scheduling. Setup checks what is available. A free Supadata account can retrieve existing YouTube captions; your AI account may have separate requirements or charges.

## Try it

Paste this message into a new conversation with an AI assistant that can open links:

> Set up my personal learning assistant using https://github.com/dayrentjiang/daily-learning. Open START_HERE.md and follow it. This is a one-time test: do not create a schedule yet. Ask what I want to learn, handle the steps you can, and guide me through only the account connections I need to make.

If the assistant cannot explore the repository, open [the complete single-file prompt](DAILY_LEARNING.md), copy its contents into the conversation, or attach that file. A model without web access can use the instructions, but cannot perform live research.

No terminal is required for the standard setup. If your app supports installing a skill folder, use [skills/daily-learning](skills/daily-learning/SKILL.md). This repo is not yet a published plugin or an automatically installed GitHub integration.

## What you get

- A learning path based on your outcome, current level and available time.
- One focused lesson with a worked example, a short exercise and recall questions.
- Source links, verified timestamps when available, and an explanation of source selection.
- A readable chat brief and, when supported, a matching PDF.
- A learner profile and learning log in storage your app can actually access.
- Optional scheduled delivery after a successful preview and your scheduling request.

Start with one topic. For example: “Learn photography so I can photograph my products with a phone; ten minutes a day.” Useful evergreen teaching takes priority over recent uploads.

See an actual [Python sample lesson](examples/python/preview.md) and its [PDF](examples/python/preview.pdf). It demonstrates the written-source fallback, with code examples checked by execution. It does not claim a successful YouTube connection.

## Free transcript mode

Connect your own Supadata account using [its hosted MCP guide](https://docs.supadata.ai/integrations/mcp). Setup will walk you through this if needed. Select existing captions (`native`) only, with at most two transcript attempts per lesson. Videos without captions can be replaced by another source. This version does not generate audio transcriptions or handle Spotify.

Check [current Supadata pricing](https://supadata.ai/pricing) before connecting. The free plan advertised on 2 October 2026 had 100 credits per month; existing transcripts cost one credit. Other use of that account shares the allowance. Instructions guide tool use; they are not a server-enforced spending cap. If your connection cannot specify native mode, the workflow uses accessible written sources instead of risking generated-transcription charges.

## Scheduling and memory

Keep learning in the same conversation or project. For delivery while your computer is off, use a supported cloud schedule and cloud-accessible instructions/history. Local files do not become cloud storage merely because a schedule references them.

After the preview, say: “Schedule this lesson workflow every weekday at 7 a.m. in [timezone].” The assistant must verify the actual schedule and report any untested connections. A successful manual lesson is not proof that an unattended run works. Test a scheduled run before relying on delivery.

Personal learning records and credentials belong in your own account, not in a fork or pull request. The included templates contain no personal data.

## For contributors

The canonical workflow lives in [SKILL.md](skills/daily-learning/SKILL.md) and its references. `DAILY_LEARNING.md` is generated from those files so the copy-and-paste version stays aligned.

```sh
python3 scripts/build_bundle.py
python3 scripts/check_repo.py
```

The optional sample PDF builder requires ReportLab: `python3 scripts/build_example_pdf.py`. Regenerate the release bundle afterwards. This dependency is only for contributors rebuilding that example, not for users copying the prompt.

See [the acceptance scenarios](tests/acceptance.md) and [test status](tests/RESULTS.md). Keep capability limitations explicit. No transcript retrieval or scheduled delivery should be reported as tested without an actual successful run.

Released under the [MIT license](LICENSE). Third-party sources, transcripts and services retain their own terms; they are not covered by this repository's license.
