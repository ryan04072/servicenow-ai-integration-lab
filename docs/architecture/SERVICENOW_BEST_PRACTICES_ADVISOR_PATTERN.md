# ServiceNow Best Practices Advisor Pattern

## Why a separate advisor?

The Architect owns the design decision.

The Best Practices Advisor supplies specialized evidence such as:

```text
"ServiceNow officially provides an OOB capability for X."
"This implementation uses a pattern that conflicts with the approved platform standard."
"This API/action is supported in the target release."
"This existing legacy pattern is common but not the desired target pattern."
```

The Architect then resolves:

```text
requirement
+ current state
+ product capability
+ standards
+ constraints
+ best-practice evidence
= architecture recommendation
```

## Invocation

The advisor is invoked when:

- a material ServiceNow design is proposed;
- custom code is proposed where an OOB/configurable option may exist;
- integration architecture is being selected;
- security/ACL/role behavior changes;
- platform scope/application boundaries change;
- the Code Reviewer detects a recurring design issue;
- a human explicitly asks for a best-practice assessment.

## Anti-pattern

Do not create a second competing architecture authority.

```text
Best Practices Advisor → evidence/advice
ServiceNow Architect   → cross-domain recommendation
Human / approved gate  → authoritative decision
```
