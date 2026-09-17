# External SaaS / API Authentication Checklist

Before connecting a new platform:

- [ ] Does vendor support OAuth 2.0?
- [ ] Does vendor support workload/application identities?
- [ ] Does vendor support certificate or federated credentials?
- [ ] Does vendor require API key?
- [ ] Does vendor support only Basic Auth?
- [ ] Are scopes/resource permissions fine-grained?
- [ ] Can access be limited by environment/tenant/project?
- [ ] Token lifetime?
- [ ] Rotation/revocation?
- [ ] IP/network restrictions?
- [ ] Webhook signing/verification?
- [ ] Audit logging?
- [ ] Rate limits?
- [ ] Secret storage requirements?
- [ ] Data residency/classification concerns?
- [ ] Vendor compromise/revocation procedure?
- [ ] Security approval recorded?

Use the strongest supported and approved mechanism.
Document why any downgrade is required.
