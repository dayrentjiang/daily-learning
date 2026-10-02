# Supadata connection and transcript policy

Use this reference when connecting a transcript provider or retrieving YouTube captions. The user's Supadata account is separate from their AI account.

## Connection

1. Check whether a Supadata transcript tool is already callable. Reuse it if present; a successful request is still required to verify retrieval.
2. If absent, open the current [official hosted MCP setup guide](https://docs.supadata.ai/integrations/mcp). The documented hosted endpoint is `https://api.supadata.ai/mcp`, authenticated through Supadata account sign-in. Guide the user through only the settings and sign-in actions you cannot perform. Do not ask for an API key in a message.
3. Use the host's documented remote-MCP/custom-app connection if available. Menu names and plan support vary; inspect current official host instructions rather than applying ChatGPT menus to another app. No custom connection support means the automated transcript path is unavailable in that host. Offer the written-source path.
4. After connection, inspect the actual tool schema. Verify that a request can explicitly select `mode: native`. A tool that silently defaults to automatic generation does not satisfy this workflow's free-caption policy.

## Retrieval

- Request existing captions only: `mode: native`. Prefer timestamped chunks (`text: false`) if the schema supports them. Do not call `auto`, `generate`, structured-video extraction or paid translation.
- Allow at most two transcript attempts per local lesson date and track, including failures and retries across repeated runs. Read the attempts ledger before calling; reserve an attempt before dispatch when durable storage is available. If previous usage is uncertain, use a written-source fallback for that run. This is a workflow budget, not a provider-enforced billing limit.
- Only request shortlisted videos. Discovery should use the host's search tool before spending transcript credits. Other apps sharing the account can consume the same monthly allowance.
- Read actual returned captions. Record URL, title, publisher, access date, relevant segment offsets and whether captions are human or automatic when known. Convert returned millisecond offsets correctly to timestamps. Avoid assuming a timestamp from one upload applies to another.
- If the tool returns a job ID, use the documented status tool, with at most three checks during the run. Record a pending job for later continuation instead of starting a duplicate job. A job ID is not a transcript. Account for any host execution time limit.
- Missing captions, quota exhaustion, blocked content or an unavailable connection: use another candidate within the remaining attempt budget, then a credible written source. Disclose the fallback. Do not upgrade plans or enable paid generation.

Pricing and support change. Review [current pricing](https://supadata.ai/pricing) during setup and [transcript modes](https://docs.supadata.ai/get-transcript) when schema behavior is unclear. A free transcript allowance does not make ChatGPT, other AI apps, hosting or all future usage free.

Full transcripts are research input. Keep your original lesson notes, source details and verified timestamps in the learning log; do not commit retrieved transcripts or credentials to the public repo.
