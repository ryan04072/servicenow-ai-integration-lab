# Short Teams Message to Security

Hi [Name] — we're starting to design a more formal authentication model for
ServiceNow automation and AI-assisted delivery across systems like Azure DevOps,
GitHub, and Microsoft tooling.

Before we expand anything, I want to make sure we're aligned with our Security
and Identity standards rather than just continuing the existing service-account
and token patterns.

My proposed default is to use dedicated non-human application/workload identities
with least privilege and short-lived credentials where the target platform
supports them—for example, an Entra service principal/managed identity for Azure
DevOps and a GitHub App for long-lived GitHub integration—with service-account
tokens only as a documented fallback when a stronger option isn't supported.

Could we review:
- our approved workload/service identity patterns;
- preferred OAuth/service-principal/certificate/managed-identity standards;
- PAT and Basic Auth restrictions;
- approved credential storage/rotation;
- nonprod vs prod identity separation;
- MCP/AI connector requirements;
- any DLP, network, logging, or AI-data requirements we need to design around?

I can provide the specific read/write permissions we're proposing for each
integration so we can keep the access as narrow as possible.
