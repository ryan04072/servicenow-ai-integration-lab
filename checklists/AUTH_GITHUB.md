# GitHub Authentication & Integration Checklist

## Preferred target

- [ ] Determine whether the integration should be a GitHub App.
- [ ] Install the GitHub App only on required repositories.
- [ ] Request only required repository/organization permissions.
- [ ] Use installation access tokens for app-owned automation.
- [ ] Use a user access token only when acting on behalf of a user.
- [ ] Protect the GitHub App private key in an approved secret store.
- [ ] Define App owner and backup owner.
- [ ] Document revocation/rotation process.
- [ ] Verify audit attribution to the App.
- [ ] Test denied repository access.

## PAT exception

If a PAT is currently required:

- [ ] Use fine-grained PAT when supported.
- [ ] Scope to minimum repositories.
- [ ] Scope to minimum permissions.
- [ ] Use shortest practical lifetime.
- [ ] Store only in approved credential storage.
- [ ] Record owner and expiration.
- [ ] Create migration item to GitHub App or other preferred identity.
- [ ] Do not use a broad classic PAT without explicit justification.

## AI-agent boundary

- [ ] Read-only review agent does not receive write permissions.
- [ ] PR creation permission is separate from merge permission.
- [ ] Merge-to-protected-branch remains governed by branch protection/human policy.
