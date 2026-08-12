# Test matrix

| Requirement | Direct test | Consensus/integration test |
| --- | --- | --- |
| Constructor validation | Invalid JSON, duplicate IDs, bad URL, bad deadline | Deployment rejection on invalid args |
| Access control | Owner-only evidence/review methods | Unauthorized transaction fails |
| Deadline enforcement | Resolve before deadline reverts | Same on a real network timestamp |
| Happy-path decision | Mock web/LLM produces canonical result | Five-validator agreement |
| Malicious leader | Mock leader result differs from independent result | Validator disagreement/rotation |
| Missing source | Mock 4xx/5xx or unavailable page | Fail-closed unresolved/unavailable state |
| Prompt injection | Evidence contains fake instructions | Result still follows frozen schema/policy |
| Replay/idempotency | Repeat terminal resolve | Repeat finalized transaction is safe |
| Boundary semantics | K-of-N, threshold, trigger routing, rulebook status | Same result under consensus |

The repository's direct tests are intentionally small and deterministic. Add
network-specific integration tests after choosing a Studio/GLSim endpoint and
funding/deploy credentials.

