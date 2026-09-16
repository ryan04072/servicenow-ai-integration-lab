# Implementation Runbook

## Foundation
1. Create private repository.
2. Import package.
3. Run `python scripts/validate_repo.py`.
4. Commit baseline.
5. Create GitHub branch protection appropriate to a solo developer without fake approvals.

## Providers
1. Install official clients/extensions.
2. Authenticate each separately.
3. Verify each provider reads `AGENTS.md`.
4. Do not enable CLI automation until manual output is trusted.
5. Configure local provider command only in ignored `providers.local.json`.

## Work Packages
1. Create with `new_work_package.py`.
2. Link ServiceNow intake and ADO work item when available.
3. Use structured evidence files.
4. Advance state explicitly.
5. Never jump a human gate via an AI tool.

## PDI / SDK
1. Build a small scoped app.
2. Validate local SDK/Fluent workflow.
3. Commit source.
4. Use independent review.
5. Add tests.
6. Validate in PDI.
7. Record as-built.

## Change / Release
1. Prefer DevOps Change Velocity for governed change creation/evidence.
2. Ensure PR/build/tests/work items are traceable.
3. Keep CAB/change approval human-controlled.
4. Create release manifest after the actual release identifiers exist.
5. Run release validation.
6. Create/update as-built docs.
