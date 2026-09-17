# Security Review Request Packet

Use this before connecting enterprise AI/automation agents to a new system.

## 1. Use case

What are we automating?

## 2. Current state

How does the process authenticate today?

Example:

```text
ServiceNow service account → PAT → Azure DevOps
```

## 3. Proposed target

Example:

```text
ServiceNow → Entra service principal → Azure DevOps
```

## 4. Data

- systems involved;
- data classification;
- whether PII/confidential data is involved;
- DEV/UAT/PROD.

## 5. Operations

List explicitly:

```text
READ
- query work items
- read sprint metadata

WRITE
- create work item
- add comment

NOT REQUESTED
- delete work item
- project administration
- pipeline administration
```

## 6. Proposed identity

- identity type;
- owner;
- backup owner;
- environment;
- credential type;
- credential store;
- rotation;
- expiry/review.

## 7. AI involvement

- agent/runtime;
- what context is supplied;
- what tools it can invoke;
- human approval point;
- audit/run trace;
- kill switch.

## 8. Fallback

What happens if the preferred identity or connector is not approved/supported?

## 9. Questions for Security / Identity

1. Is the proposed workload identity pattern approved?
2. Do you prefer managed identity, workload federation, certificate-backed service principal, or another enterprise pattern for this use case?
3. What is the approved secret/certificate store?
4. What app-registration/service-principal ownership process should we follow?
5. Are there Conditional Access or workload-identity policies we must account for?
6. Are there restrictions on GitHub Apps?
7. Are PATs allowed for production automation? If yes, under what scope/lifetime?
8. Is Basic Auth prohibited for new integrations?
9. Are MCP clients/servers approved? Are there specific review requirements?
10. Are there outbound network/egress restrictions or proxies?
11. Are webhook endpoints allowed? What signing/validation standards apply?
12. What Power Platform DLP policies apply?
13. What data classifications may be processed by the approved AI runtimes?
14. What logging/SIEM/audit events are required?
15. What credential rotation/expiration standards apply?
16. Do nonproduction and production require separate identities?
17. What is the emergency credential-revocation process?
18. Who should approve future additions of tools/scopes?
