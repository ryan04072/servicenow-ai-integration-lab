# Azure DevOps Authentication & Integration Checklist

## Identify platform

- [ ] Azure DevOps Services or Azure DevOps Server?
- [ ] Microsoft Entra tenant relationship confirmed.

## Preferred unattended auth

For Azure DevOps Services:

- [ ] Azure-hosted workload: evaluate managed identity first.
- [ ] Non-Azure/external automation: evaluate Entra service principal.
- [ ] Azure Pipelines: evaluate service connection/workload identity federation.
- [ ] Add identity to only required ADO organizations/projects.
- [ ] Apply minimum ADO permissions separately from Entra permissions.
- [ ] Verify audit identity.

## Service-principal credential

If a credential is required:

- [ ] Evaluate federated credential.
- [ ] Evaluate certificate.
- [ ] Use client secret only if required/approved.
- [ ] Store in approved credential store.
- [ ] Rotate and monitor.

## PAT exception

- [ ] PAT use is temporary, personal, Azure DevOps Server, or compatibility-driven.
- [ ] Scope is minimal.
- [ ] Lifetime is minimal.
- [ ] Secret storage is approved.
- [ ] Migration path is documented.
- [ ] PAT is not tied to an employee whose departure would break production automation.

## AI-agent boundary

Separate where practical:
- [ ] read/query work items;
- [ ] create/update draft work items;
- [ ] sprint/iteration modification;
- [ ] repository permissions;
- [ ] pipeline/release permissions.
