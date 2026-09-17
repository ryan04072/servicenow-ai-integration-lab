# Validation Report — Final

- JSON parsed: **83**
- YAML parsed: **71**
- JSON/YAML errors: **0**
- Canonical roles: **42**
- GitHub agent wrappers: **42**
- Pipeline roles referenced: **31**
- Missing pipeline role definitions: **0**
- Missing agent wrappers: **0**
- Missing required final artifacts: **0**
- Reference runtime tests: **PASS**
- Overall: **PASS**

## Missing role definitions
```json
[]
```

## Missing wrappers
```json
[]
```

## Missing required artifacts
```json
[]
```

## Unit test output
```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/generated/interface/models.py", line 32317, in hydrate_crdt_from_proto
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/remote.py", line 749, in __call__
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
test_bad_code_is_blocked_before_atf (test_quality_and_docs.QualityAndDocumentationTests.test_bad_code_is_blocked_before_atf) ... ok
test_decision_record_captures_rationale_not_chain_of_thought (test_quality_and_docs.QualityAndDocumentationTests.test_decision_record_captures_rationale_not_chain_of_thought) ... ok
test_free_text_expert_context_is_captured (test_quality_and_docs.QualityAndDocumentationTests.test_free_text_expert_context_is_captured) ... ok
test_good_code_runs_all_synthetic_atf (test_quality_and_docs.QualityAndDocumentationTests.test_good_code_runs_all_synthetic_atf) ... ok
test_context_finds_reuse_and_dependencies (test_runtime.RuntimeTests.test_context_finds_reuse_and_dependencies) ... ok
test_orchestrator_pauses_and_resumes (test_runtime.RuntimeTests.test_orchestrator_pauses_and_resumes) ... ok
test_unauthorized_responder_rejected (test_runtime.RuntimeTests.test_unauthorized_responder_rejected) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.016s

OK
```
