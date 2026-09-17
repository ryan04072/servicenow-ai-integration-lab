# Reliability Test Checklist

- [ ] Duplicate trigger
- [ ] Tool timeout
- [ ] Rate limit
- [ ] Authentication expired
- [ ] Authorization denied
- [ ] Malformed model output
- [ ] Missing context
- [ ] Downstream create succeeds but callback fails
- [ ] Approval timeout
- [ ] Provider outage
- [ ] ServiceNow unavailable
- [ ] Azure DevOps unavailable
- [ ] GitHub unavailable
- [ ] Retry does not duplicate write
- [ ] Circuit breaker activates
- [ ] Manual fallback works
