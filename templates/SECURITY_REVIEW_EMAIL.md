# Security / Identity Architecture Review — Email Template

Subject: Review Request — Authentication Standards for ServiceNow Automation & AI Integrations

Hi [Name],

We're expanding the ServiceNow delivery model to support more automation and
AI-assisted workflows across platforms such as Azure DevOps, GitHub, and
Microsoft tooling. Before we implement additional connections, I'd like to align
the design with our Security and Identity standards.

Current integrations in several areas use dedicated service accounts with tokens.
For new integrations, I'm proposing that we prefer platform-native non-human
application/workload identities and short-lived credentials where supported,
while retaining service-account/token patterns only as documented fallbacks.

Examples we are evaluating include:
- Microsoft Entra managed identity/service principal for unattended Azure DevOps access;
- GitHub Apps for long-lived organization integrations instead of user PATs;
- OAuth 2.0 with ServiceNow Connection & Credential Aliases for supported APIs;
- OAuth-authorized, bounded ServiceNow MCP tools for approved AI clients;
- service-principal ownership for applicable mission-critical Power Automate flows.

Before moving forward, I'd like to confirm:

1. Which machine/workload identity patterns are approved?
2. What credential hierarchy do we prefer (federation, certificate, client secret, token)?
3. What are our PAT and Basic Auth standards for production automation?
4. Which credential/vault services should be used?
5. Do DEV/UAT/PROD require separate identities?
6. What DLP, network, logging/SIEM, retention, and AI-data controls apply?
7. What review is required for MCP, AI agents, or new external connectors?
8. Who should own approval for future scopes/tool additions?

The intent is to start read-only in nonproduction, validate least privilege and
auditing, and only add bounded write capabilities after review.

I can provide a per-integration permission matrix and architecture diagram for
the review.

Thanks,
[Name]
