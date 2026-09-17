# ServiceNow Package Promotion Review Checklist

## Candidate package

- [ ] Purpose/requirement documented
- [ ] Source environment documented
- [ ] Update set/application/package identified
- [ ] Package hash/version captured where practical
- [ ] External build tools declared
- [ ] No employer/proprietary data was placed in an unapproved personal system

## Static package review

- [ ] XML/package parses
- [ ] Artifact inventory generated
- [ ] Scope/application verified
- [ ] Hard-coded instance URLs checked
- [ ] Hard-coded sys_ids checked
- [ ] Personal endpoints/accounts checked
- [ ] Secrets/tokens/private keys checked
- [ ] User/group references checked
- [ ] Plugins/spokes/apps identified
- [ ] Connection/Credential Alias dependencies identified
- [ ] Roles/ACL/security changes identified
- [ ] Cross-scope dependencies identified
- [ ] destructive/bulk operations identified
- [ ] post-import configuration documented
- [ ] rollback/disable documented

## Enterprise adoption

- [ ] Promotion Review Report completed
- [ ] Human agrees candidate may enter enterprise DEV
- [ ] Package uploaded to enterprise DEV
- [ ] ServiceNow Preview / install validation completed
- [ ] Preview conflicts/dependencies resolved
- [ ] DEV technical review completed
- [ ] Tests/ATF completed
- [ ] UAT completed
- [ ] Normal change/release process followed

A pre-review is not a production approval.
