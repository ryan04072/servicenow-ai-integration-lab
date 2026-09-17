# Personal Lab Autonomy Model

The enterprise model is intentionally stricter. The personal lab can move faster.

## L0 — Explore

AI reads context and gives advice.

## L1 — Draft

AI creates:
- code;
- docs;
- work-item drafts;
- architecture plans.

## L2 — Bounded DEV write

AI may:
- create/update personal Azure DevOps work;
- create feature branches/PRs;
- write DEV/PDI records/config through approved tools;
- call personal APIs.

Human review remains before destructive actions.

## L3 — Agentic engineering

AI may orchestrate:

```text
requirement
→ architecture
→ implementation
→ test
→ PR
→ documentation
```

Manual merge.

## L4 — Disposable autonomous experiment

AI may perform destructive actions only inside explicitly disposable lab
resources.

Examples:
- rebuild a test table;
- delete synthetic records;
- recreate a disposable app.

## Never automatic

- employer production systems;
- financial purchases;
- irreversible external/public actions;
- sharing private credentials/data;
- destructive actions outside disposable personal resources.
