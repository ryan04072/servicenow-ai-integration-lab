---
name: repository-inventory
description: Deterministically inventory repository content before broad reviews.
---

# Repository Inventory

Run:

```text
python .agents/skills/repository-inventory/scripts/generate_inventory.py
```

Use the generated inventory and coverage ledger as the audit source of truth.

Never claim a full repository review is complete while in-scope files remain pending.
