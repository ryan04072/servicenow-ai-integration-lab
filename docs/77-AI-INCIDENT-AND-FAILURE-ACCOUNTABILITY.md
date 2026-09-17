# AI Incident and Failure Accountability

## Use existing enterprise response processes

Do not create a disconnected incident universe. Use existing incident, major
incident, security incident, privacy incident, risk issue, and problem/root-cause
processes.

AI Control Tower AI cases can provide the AI-governance record and should be
correlated to operational/security incidents when both are required.

## Immediate response hierarchy

```text
Detection
→ contain/disable capability if necessary
→ notify operational owner
→ triage impact
   ├─ security/privacy → Security/Privacy process
   ├─ business impact → Process/Asset owner
   ├─ platform failure → Platform owner
   └─ AI quality/governance → AI Steward / AI case
→ restore safe service / human fallback
→ root cause
→ remediation
→ re-evaluation/re-approval if material
→ lessons/eval/standard update
```

## Example accountability

### Bad recommendation; no action taken
Primary: AI asset owner + maintainer.

### Wrong but reversible business action
Primary: capability/process owner + platform owner; notify AI asset owner.

### Unauthorized access / data exposure / malicious behavior
Primary response: Security/Privacy; include AI asset owner, steward, and platform owner.

### Repeated quality degradation
Primary: AI asset owner/maintainer; reduce autonomy or disable if needed.

### Material business harm
Escalate under existing major incident / executive risk governance.

AI is never the accountable party.
