# Worked Example — SharePoint Request

## Requirement

> When a new approved project record is created, create the appropriate
> SharePoint structure and return the destination to ServiceNow.

## Step 1 — Live instance

Search:
- existing SharePoint integration artifacts;
- installed spokes/apps;
- connection aliases;
- existing flows/subflows;
- prior project automation;
- tests.

## Step 2 — Official product knowledge

Retrieve official ServiceNow evidence for:
- Microsoft SharePoint Online Spoke;
- supported actions/flows;
- dependencies;
- required Integration Hub entitlement;
- applicable release/app version.

## Step 3 — Capability state matrix

| Capability | Exists in product | Installed | Configured | Entitled | Meets requirement |
|---|---:|---:|---:|---:|---:|
| SharePoint Online Spoke | evidence required | instance check | instance check | entitlement check | action-by-action analysis |
| Existing internal integration | instance evidence | n/a | instance evidence | n/a | requirement comparison |
| Custom REST | platform supports pattern | n/a | not yet | licensing/security review | fallback |

## Step 4 — Architecture recommendation

Example:

> Reuse the installed SharePoint Online Spoke for supported operations and create
> a reusable custom action only for the uncovered API operation. Do not implement
> the entire integration through bespoke REST scripts.

or:

> The official SharePoint spoke exists, but it is not currently licensed/
> installed in this environment. Present licensing/installation and custom
> integration as separate options rather than assuming spoke availability.

## Step 5 — Evidence

The Decision Record includes the exact product and instance evidence used.

That means a future reviewer can tell **why** the spoke/custom decision was made.
