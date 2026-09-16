# Target Architecture

```mermaid
flowchart TD
    A[ServiceNow Intake] --> B[Azure DevOps Work Item]
    B --> C[Agentic Orchestrator]
    C --> D[Intake / Grooming]
    D --> E[Architecture Agent]
    E --> F{Human Architecture Gate}
    F -->|Approved| G[Backlog / Priority]
    G --> H{Human Priority Gate}
    H -->|Ready| I[Implementation Planner]
    I --> J[Developer / Build Agent / Native Config]
    J --> K[GitHub Branch + PR]
    K --> L[Code + PR Review]
    L --> M[Test / ATF]
    M --> N{Human UAT}
    N -->|Accepted| O[Documentation]
    O --> P[DevOps Change Velocity Evidence]
    P --> Q{CAB / Human Change Gate}
    Q -->|Approved| R[Scheduled / Deploy]
    R --> S[Release Validator]
    S --> T[Release Manifest + As-Built PR]
    T --> U{Human Merge}
```

## Systems
- ServiceNow PDI: intake, runtime platform, change governance, native development
- Azure DevOps: planning/work items
- GitHub: code/source, PRs, durable engineering knowledge
- VS Code: local engineering cockpit
- Copilot / Claude / Codex / Gemini: interchangeable specialists
