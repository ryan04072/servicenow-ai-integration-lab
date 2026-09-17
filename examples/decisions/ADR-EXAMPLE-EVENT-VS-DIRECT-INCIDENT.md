# ADR-EXAMPLE — Event Management vs Direct Incident Creation

Status: Example
Scope: Synthetic/reference only

## Context

A monitoring-originated signal needs to create actionable ServiceNow work while
preventing duplicate incidents and preserving correlation/lifecycle context.

## Options considered

### Option A — Direct Incident creation

Advantages:
- simpler path for sources that already produce fully-qualified incident events;
- fewer intermediate records.

Tradeoffs:
- weaker fit when the source produces noisy/repeating monitoring signals;
- correlation/deduplication must be implemented elsewhere;
- less natural representation of alert/event lifecycle.

### Option B — Event/Alert Management path

Advantages:
- preserves monitoring signal lifecycle;
- enables correlation/deduplication before incident creation;
- supports impact/context enrichment;
- separates raw operational signals from user-facing incident work.

Tradeoffs:
- additional platform components/configuration;
- requires clear alert-to-incident policy.

## Decision

Use the Event/Alert Management path for monitoring-originated signals that need
correlation/deduplication before incident creation.

Retain direct Incident creation as a valid pattern for sources where correlation
and event lifecycle are not needed.

## Rationale

The requirement is fundamentally an operational-event processing problem before
it becomes an Incident-management problem. The selected path preserves that
distinction and avoids pushing correlation logic into incident creation.

## Rejected alternative

Direct Incident creation was not removed as a capability; it was not selected as
the default for this signal class.

## Review trigger

Revisit if the source platform becomes the authoritative correlation engine or
ServiceNow event-management architecture changes.
