# Personal Lab — Product Knowledge / Capability Resolver

## Goal

Test whether an agent can independently discover the right OOB ServiceNow option
before writing custom code.

## Example benchmark

Prompt:

> Build an automation that manages SharePoint Online content from ServiceNow.

Expected process:

1. Inspect PDI for installed/current capability.
2. Query official ServiceNow Docs/Store.
3. Identify Microsoft SharePoint Online Spoke when supported by evidence.
4. Inspect actions/dependencies/release compatibility.
5. Distinguish PDI availability from enterprise entitlement.
6. Compare OOB/extend/custom options.
7. Cite evidence.
8. Only then produce architecture.

## Experiments

Repeat for:
- Microsoft Teams;
- Azure DevOps;
- Entra/Azure AD;
- Okta;
- Slack;
- Microsoft 365;
- common ITOM/ITSM integrations.

Score hallucination rate separately from architecture quality.
