# Echelon Capability Crosswalk — Reference Comparison

## Purpose

Use this document to compare the operating model with Echelon based on
**observed evidence** and **vendor-documented/claimed capabilities**.

Do not treat vendor claims as measured results.

## Crosswalk

| Capability | This operating model | Echelon comparison question |
|---|---|---|
| Instance discovery | Context Service + artifact catalog | How broad/deep is Echelon's instance model? |
| Similar-pattern detection | `find_similar_artifacts` + Context Envelope | Does it identify the same reusable artifacts? |
| Dependency awareness | Dependency Graph | How does Echelon determine blast radius/dependencies? |
| Requirement clarification | Intake agents + Human Action Broker | Does it ask better/more relevant questions? |
| Architecture | ServiceNow Architect + standards | How transparent is its recommendation/evidence? |
| Build | pluggable execution engine | What can Echelon actually implement end-to-end? |
| Test | ATF/test specialists + evals | Quality/coverage/repair loop? |
| Documentation | docs-as-code + documentation agent | Completeness/accuracy/freshness? |
| Human gates | authoritative approvals + Teams | Where/how are Echelon human decisions captured? |
| Delivery integration | ADO/GitHub/ServiceNow contracts | How well does Echelon fit existing SDLC? |
| Telemetry | trace + eval schemas | How observable/auditable is agent behavior? |
| Operations | extensible workflows | What managed-service/remediation capability is additional? |

## Biggest comparison point

The key benchmark is not "who has more agents."

It is:

> Given the same real ServiceNow requirement, which approach retrieves the right
> current-state context, proposes the most supportable architecture, produces the
> highest-quality implementation/test evidence, and requires the least corrective
> human work?

Use the benchmark templates already included in the package.
