# Delivery Intelligence Agent Catalog

This extension adds specialist roles around the existing lifecycle.

| Agent | Purpose | Default Access |
|---|---|---|
| Context Curator | Build evidence-backed context envelopes | Read |
| Executive Brief Agent | Leadership-level delivery summary | Read + draft |
| Azure DevOps Expert | Interpret work planning/delivery records | Read |
| GitHub Expert | Interpret repo/PR/CI evidence | Read |
| Engineering Manager | Delivery health and engineering coordination | Read |
| Software Engineer | Implement approved code changes | Controlled write |
| Roadmap Alignment Reviewer | Check delivery vs roadmap | Read |
| Delivery Flow Analyst | Detect SDLC bottlenecks/WIP | Read |
| Validation Analyst | Analyze validation/UAT queue | Read |
| Enterprise Intake Analyst | Refine/triage incoming demand | Read + draft |

## Relationship to existing roles

Keep existing:
- orchestrator
- intake analyst
- backlog engineer
- portfolio advisor
- ServiceNow architect
- implementation planner
- developer
- code reviewer
- PR reviewer
- test engineer
- change prep
- release validator
- documentation engineer

The new roles specialize context and enterprise delivery visibility rather than replacing them.

## Routing examples

### New intake
Context Curator → Enterprise Intake Analyst → Backlog Engineer → Portfolio Advisor → Human triage

### Sprint executive brief
Context Curator → Azure DevOps Expert → Roadmap Alignment Reviewer → Delivery Flow Analyst → Executive Brief Agent → Human review

### Pull request
Context Curator → GitHub Expert → Code Reviewer / PR Reviewer → Test Engineer → Human merge

### ServiceNow solution
Context Curator → ServiceNow Architect → Implementation Planner → Developer → Review/Test → Human gates
