# Friday Demo Runbook

Target: 5–10 minutes.

## 1. Start with the problem

"We are running a lean platform team with humans, vendors, and increasingly AI-assisted delivery.
The challenge is not just generating code. It is keeping all contributors aligned to the same roadmap,
standards, evidence, and SDLC."

## 2. Show the architecture

Show:
- canonical `agents/roles/`;
- `context/`;
- `config/tools/`;
- thin `.github/agents/` adapters.

Explain:

"The roles survive model/provider changes. Enterprise connectors supply live context."

## 3. Show one context envelope

Open `context/CONTEXT_ENVELOPE.md`.

Explain source, authority, freshness, permissions, and unresolved questions.

## 4. Show the executive brief flow

Open `docs/18-EXECUTIVE-BRIEF-AND-INTAKE.md`.

Example question:

"What are we working on, how does it map to the roadmap, what is blocked, and what decisions are needed?"

## 5. Show specialist expansion

Open `docs/16-DELIVERY-INTELLIGENCE-AGENT-CATALOG.md`.

Highlight:
- ADO Expert
- GitHub Expert
- Engineering Manager
- ServiceNow Architect
- Roadmap Reviewer
- Executive Brief Agent

## 6. Show enterprise-safe runtime model

Open `config/tools/TOOL-CONTRACTS.md`.

Key statement:

"We do not require local Git, PowerShell, or unrestricted developer tooling.
The repo defines capability contracts; approved enterprise connectors implement them."

## 7. Close

"The immediate goal is read-only delivery intelligence and better decision support.
Writes and autonomous actions remain gated until we have evidence the system is reliable."

## Do not demo yet

- autonomous production writes;
- live secrets;
- production customer/employee data;
- a giant multi-agent workflow just for spectacle.

## Good demo question

"If our Monday sprint meeting happened right now, what should leadership know,
what is off-plan, and what decisions are required?"
