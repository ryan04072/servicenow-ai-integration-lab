# Personal Lab — AI Quality Engineering

## Goal

Use the personal sandbox to practice the permanent quality loop:

```text
Build Agent / Codex / Claude / manual
→ ServiceNow Code Reviewer
→ static scan
→ PDI Instance Scan where available
→ ATF/Test Engineer
→ bounded repair
→ evidence
```

## Sequence

1. Run synthetic quality tests:
   ```bash
   python -m reference_runtime.cli quality --fixture bad
   python -m reference_runtime.cli quality --fixture good
   ```
2. Create a deliberately flawed PDI script.
3. Export/retrieve the artifact into your review adapter.
4. Compare:
   - deterministic scan;
   - AI semantic review;
   - PDI Instance Scan.
5. Correct it.
6. Map acceptance criteria to ATF.
7. Generate/run ATF in PDI.
8. Export normalized test evidence.
9. Repeat the same benchmark using Build Agent, Codex, and Claude when useful.
