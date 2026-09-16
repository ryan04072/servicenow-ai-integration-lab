# ADR-0001 — Use Source-Driven Development for the Lab App

## Status
Proposed

## Context
This lab exists specifically to learn SDK/Fluent and Git-centric development.

## Decision
Use the ServiceNow SDK/Fluent path for artifacts supported by the chosen SDK version.

## Consequences
- source history is visible in Git,
- SDK constraints become part of the learning,
- unsupported metadata may still require native ServiceNow tooling.

## Revisit Trigger
If the chosen artifact type is not supported by the current SDK/Fluent toolchain.
