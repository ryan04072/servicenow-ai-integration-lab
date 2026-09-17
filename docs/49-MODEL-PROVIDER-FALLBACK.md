# Model / Provider Fallback

## Objective

Provider neutrality should exist operationally, not only in repository structure.

## For each workflow define

- primary model/runtime;
- supported fallback;
- unsupported features;
- timeout/failure behavior;
- whether workflow can degrade to human-only;
- data-classification restrictions.

## Fallback modes

### Equivalent provider
Run the same canonical role through an approved alternate provider.

### Reduced-capability provider
Run a smaller read-only analysis and require more human work.

### Human fallback
Skip AI and route to established manual process.

## Multi-model review

Use independent model review selectively for:
- high-risk architecture;
- disputed technical recommendation;
- major releases;
- material policy changes.

Do not use majority vote as truth.

Evidence and tests decide technical questions.
