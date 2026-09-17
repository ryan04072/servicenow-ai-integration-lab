# Skill: ServiceNow Build Tool Benchmark

## Purpose

Evaluate ServiceNow-native Build Agent and external/partner AI delivery tools
using the **same workload, evidence, and outcome metrics**.

Do not compare marketing claims alone.

## Candidate tools

Examples:
- ServiceNow Build Agent;
- Echelon AI;
- Codex/Claude Code + ServiceNow SDK/MCP;
- human developer baseline;
- other approved or lab-only build tools.

## Benchmark dimensions

### Requirement handling
- missing-requirement detection;
- clarifying questions;
- acceptance-criteria quality;
- reuse of existing instance patterns.

### Platform context
- instance/schema awareness;
- existing customization awareness;
- scope awareness;
- dependency discovery.

### Build
- first-pass implementation success;
- OOB/native design preference;
- correctness;
- maintainability;
- portability;
- UI/UX quality where relevant.

### Test
- test plan;
- ATF generation;
- negative/failure coverage;
- self-repair;
- regression behavior.

### Security / governance
- ACL/security treatment;
- secret handling;
- script approval;
- auditability;
- enterprise control integration.

### Documentation
- as-built documentation;
- dependency documentation;
- rollback;
- runbook/support material.

### Delivery
- time to usable DEV result;
- human interventions;
- number of AI calls/interactions;
- rework;
- deployment/package quality.

### Economics
- direct consumption;
- license/vendor cost;
- human review minutes;
- cost per successful story/capability.

## Required evidence

For every run capture:
- benchmark ID;
- exact normalized requirement;
- source-instance starting state;
- tool/provider;
- prompts/calls;
- elapsed time;
- artifacts changed;
- tests;
- review findings;
- human edits;
- final outcome;
- cost/consumption where available.

## Do not change the requirement to favor a tool

If a tool needs a platform-specific representation, preserve the same acceptance
criteria and business outcome.

## Benchmark result

Return evidence, tradeoffs, and observed strengths/limitations.

Do not assume a native or external tool is superior before testing.
