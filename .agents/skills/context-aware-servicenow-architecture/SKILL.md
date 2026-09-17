# Skill: Context-Aware ServiceNow Architecture

Use this skill for any request that changes or adds ServiceNow functionality.

## Required sequence

1. Normalize requirement and acceptance criteria.
2. Build a Context Envelope.
3. Search for similar existing ServiceNow artifacts.
4. Inspect the strongest candidates.
5. Expand dependencies.
6. Retrieve relevant approved standards.
7. Retrieve related ADO/GitHub precedent when available.
8. Separate:
   - current state;
   - approved target/reference;
   - gaps.
9. Prefer:
   - OOB capability;
   - reuse;
   - extension;
   before net-new custom implementation when they satisfy the requirement.
10. Do not copy a common pattern if it conflicts with an approved standard.
11. Cite artifact/evidence IDs in the architecture result.
12. If a material fact is unresolved, create a Human Action instead of guessing.
13. Architecture approval must pause orchestration when policy requires it.

## Required architecture output

- Requirement
- Current State
- Existing Reuse Candidates
- Dependencies / Blast Radius
- Approved Reference
- Gap
- Options
- Tradeoffs
- Recommendation
- Test / Rollback considerations
- Evidence
- Human Decision Required
