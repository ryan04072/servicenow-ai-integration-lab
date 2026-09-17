# AI Workload Placement Checklist

For every new AI use case:

- [ ] What is the authoritative system?
- [ ] Where does the user naturally work?
- [ ] Is the task search, reasoning, analytics, or action?
- [ ] Does it require live ServiceNow configuration/records?
- [ ] Does it require Microsoft Graph/M365 context?
- [ ] Does it require repository/PR/CI context?
- [ ] Does it span multiple platforms?
- [ ] What permissions are required?
- [ ] What AI/runtime is already licensed?
- [ ] What consumption model/cost applies?
- [ ] Can OOB capability satisfy it?
- [ ] Is custom AI actually required?
- [ ] Where is the human gate?
- [ ] What is the fallback if the AI runtime is unavailable?
- [ ] How will we measure quality/value?

Default:
- ServiceNow-native task → ServiceNow AI first.
- M365 productivity task → Microsoft Copilot first.
- repo engineering → GitHub Copilot first.
- cross-platform event/action → orchestration layer.
