# Scheduling and continuity

Read this when the user requests recurring delivery or when executing a scheduled lesson. A preview alone does not authorize a recurring task.

## Establish a runnable configuration

Reuse an explicit scheduling request and any supplied time, days and timezone. Ask only for missing required settings. Use the host's native scheduling tool when exposed. If unavailable, explain that this environment can produce lessons on demand; do not claim that instructions alone will wake the assistant later.

Before creation, identify an actual accessible home for the workflow, learner profile, learning log and artifacts. A public GitHub URL supplies instructions, not writable personal memory. Uploaded files may be readable without being editable; verify that distinction. For an initial small course, the same conversation can hold a compact structured log, with occasional user-saveable snapshots. Do not promise indefinite recall.

Use a cloud-capable schedule for “deliver while my computer is off.” Local scheduling requires the relevant computer/runtime to remain available. Neither a raw GitHub link nor a path to a local checkout makes files accessible to a cloud task.

On ChatGPT, consult [current scheduling documentation](https://learn.chatgpt.com/docs/automations) and [plugin documentation](https://learn.chatgpt.com/docs/plugins). For another host, use its official documentation and actual tools. Do not assume all apps called an LLM support scheduling, remote MCP, PDFs or shared project memory.

## Create or update

Inspect existing accessible schedules to avoid duplicates. Preserve unrelated schedules. Create or update one task for this learning track using the user's requested recurrence. Include:

- The complete daily workflow or a verified accessible skill reference. A vague instruction to “continue learning” is insufficient.
- The learner's outcome, level, time budget, language and local timezone.
- Where the profile and log can actually be read and updated.
- Native-only Supadata mode, the two-attempt daily budget and written-source fallback.
- The phone-readable lesson, PDF when supported, and honest partial-failure behavior.
- Same-date deduplication and the return destination.

Use a stable release or commit for scheduled workflow instructions where possible. Record the version; apply later repo updates deliberately rather than silently changing the workflow every morning.

Confirm the schedule only from a successful scheduler response. State the time and timezone, destination and whether the schedule starts work or promises a delivery deadline. Keep notification preferences in the host's settings. Do not send email or messages to third parties without a separate user request.

## Verify unattended execution

A successful manual source lookup does not establish scheduled tool access. Mark the setup “scheduled; unattended run not yet verified” until an actual scheduled run confirms source access, usable history and delivery. Arrange a short trial run when the user asks to test scheduling. Check its result instead of reporting a scheduled lesson as completed at creation time.

For failed authentication, quota or file creation, deliver a concise truthful status or the defined fallback. Preserve enough state to repair the failed part without duplicating paid requests or successful lessons.
