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
| Nondeterministic storage isolation | AST asserts no `self` reference in leader/validator closures | Live receipt must contain no storage-capture warning |

The direct tests are intentionally small and deterministic. StudioNet and
Bradbury deployment manifests record the live contract address, deployment
transaction, schema/state verification, and consensus transaction where
applicable. A live `UNRESOLVED` or `INCONCLUSIVE` result is a passing safety
test when the public evidence does not support a terminal judgment.

## Recorded results — 2026-08-12

- Standalone suite: 3 passed.
- Six-contract aggregate suite: 28 passed, 1 environment-only skip.
- GenVM lint and SDK schema validation: passed.
- StudioNet: finalized deployment plus finalized `RESOLVED / YES` test; leader
  execution `SUCCESS`, 3 agree / 2 idle, no storage-capture warning.
- Bradbury: deployment submitted in the six-contract batch and accepted; see
  `deployments/bradbury.json` for the current finality status.
