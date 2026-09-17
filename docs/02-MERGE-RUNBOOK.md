# Personal Lab Merge Runbook

## 1. Create branch

```text
feature/personal-agentic-ai-platform-lab
```

## 2. Merge the overlay

Copy package contents to the existing repository.

Resolve conflicts by keeping the existing canonical role and extending behavior
through personal-lab config/skills.

## 3. Configure environment

Edit:

```text
context/personal-lab/LAB_ENVIRONMENT.yaml
```

Identify:
- ServiceNow PDI;
- GitHub repo(s);
- personal Azure DevOps organization/project;
- Microsoft tenant/tools;
- optional n8n;
- optional MCP servers;
- optional local containers/services.

## 4. Configure auth

Use `docs/06-PERSONAL-AUTH-STANDARD.md`.

For personal DEV, a scoped PAT may be perfectly reasonable while learning.
Do not over-engineer identity before the lab proves value.

## 5. Turn on LAB mode

Review:

```text
config/personal-lab/lab-policy.yaml
```

Default:
- read/write allowed in personal DEV;
- destructive actions require manual approval;
- no employer/production targets;
- budget caps enabled;
- agent delegation allowed with limits.

## 6. Select experiment

Create a copy of:

```text
experiments/EXPERIMENT_TEMPLATE.md
```

## 7. Build

Use normal branch/PR habits.

## 8. Evaluate

Run:
- tests;
- golden task;
- failure case;
- manual review.

## 9. Promote

For the personal lab, "promotion" usually means:

```text
experiment
→ reusable lab capability
→ portfolio/demo project
```

No CAB required.
