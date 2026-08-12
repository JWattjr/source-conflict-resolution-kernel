# Security and consensus audit

Audit date: 2026-08-12  
Scope: the six Python Intelligent Contracts in `contracts/`  
Method: manual review, GenVM AST lint, SDK schema validation, direct-mode
regression tests, explicit validator execution, and hosted-network smoke tests.

## Executive summary

The reviewed contracts implement bounded GenLayer-native judgment primitives.
No unresolved critical or high-severity code issue was found after remediation.
They do not hold or transfer funds, which substantially limits direct asset-loss
risk. A production payout adapter remains out of scope and must wait for
GenLayer finality before making irreversible transfers.

## Remediated findings

| ID | Severity | Finding | Remediation |
| --- | --- | --- | --- |
| GL-01 | High | Rulebook winner IDs were free-form LLM output. | Freeze a participant allowlist at deployment and fail to `INCONCLUSIVE` for unknown winners. |
| GL-02 | Medium | MarketSpecGuard checked terminal state `LISTED` although it stores `LISTABLE`. | Correct terminal-state check and add idempotency regression coverage. |
| GL-03 | Medium | All-source outages still invoked the LLM, allowing unsupported terminal judgments. | Derive deterministic unresolved/inconclusive results before any LLM call when every source is unavailable. |
| GL-04 | Medium | HTTPS validation allowed localhost, private literal IPs, userinfo, non-default ports, and internal-style hosts. | Add bounded public-host validation to all evidence inputs. |
| GL-05 | Medium | TruthGraph formulas could reference undeclared atom IDs and silently resolve them as unknown. | Validate the complete formula graph against frozen atom IDs in the constructor. |
| GL-06 | Medium | CLI JSON arguments are decoded before contract invocation, while constructors originally assumed JSON strings. | Accept decoded list/object values and persist canonical JSON strings internally. |
| GL-07 | Low | UTF-8 decoding could fail on malformed or truncated source bytes. | Bound bytes before decoding and replace invalid byte sequences. |
| GL-08 | Low | Conditional false-trigger state did not expose an explicit terminal outcome. | Store `outcome = VOID` when the trigger is false. |
| GL-09 | Low | Milestone score used a float-producing division before integer conversion. | Use integer floor division for deterministic basis-point scoring. |
| GL-10 | Low | Validator wrappers accepted any object exposing `calldata`. | Require `gl.vm.Return` before comparing leader and independent results. |

## Residual risks and assumptions

- Hostname validation cannot prevent DNS rebinding by itself. Deploy only with
  stable, pre-reviewed public source domains; production deployments should add
  an explicit domain allowlist.
- Public pages can drift between leader and validator fetches. The contracts
  compare normalized decision fields and fail consensus on substantive
  disagreement, but highly dynamic pages remain poor evidence.
- LLMs may disagree on genuinely ambiguous language. This is expected; the
  network can rotate validators or become undetermined rather than forcing a
  settlement.
- Source authenticity is external to the contracts. HTTPS reachability is not
  proof that a publisher is authoritative.
- Contract-level outcomes should be consumed only after network finality. This
  repository contains no payout or escrow code.

## Verification gates

- All contract files use the pinned `py-genlayer` runner.
- GenVM AST lint passes for all six files.
- GenLayer SDK schema validation passes for all six files.
- Direct tests cover happy paths, fail-closed paths, deadline/lifecycle logic,
  malicious leader disagreement, URL controls, formula integrity, source
  conflict, unknown participants, and idempotency.
- Hosted deployments are counted as evidence only when the leader execution
  receipt is `SUCCESS` and schema/state reads succeed.

This review is an engineering security assessment, not a formal verification,
financial guarantee, or legal certification.
