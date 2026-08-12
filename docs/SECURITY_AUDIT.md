# Security and consensus audit: SourceConflictKernel

Audit date: 2026-08-12
Scope: `contracts/SourceConflictKernel.py`
Method: manual review, GenVM AST lint, SDK schema validation, direct-mode
tests, malicious-leader checks, and hosted-network receipt inspection.

## Result

No unresolved critical or high-severity issue was found after remediation.
The contract stores a bounded judgment and never custodies or transfers funds.

## Remediated findings

| ID | Severity | Finding | Remediation |
| --- | --- | --- | --- |
| SC-01 | Medium | An all-source outage could produce an unsupported terminal judgment. | Derive `SOURCE_UNAVAILABLE` before prompting when every fetch fails. |
| SC-02 | Medium | URL validation permitted private targets and duplicate source domains. | Require distinct public HTTPS domains and reject userinfo, private IPs, internal suffixes, and non-default ports. |
| SC-03 | Medium | Consensus closures captured contract storage. | Snapshot claim, canonical source specs, and confirmation threshold before nondeterministic execution; closures contain no `self`. |
| SC-04 | Medium | Diagnostic observation differences could reject an equivalent settlement. | Validators independently recompute and compare the consequential `status` and `outcome`; observations remain audit metadata. |
| SC-05 | Low | Malformed bytes, decoded CLI JSON, and loose return wrappers reduced resilience. | Bound/decode source bytes safely, canonicalize decoded JSON, and require `gl.vm.Return`. |

## Residual risks

- Source tiers are deployer-supplied policy labels, not cryptographic proof of
  authority.
- Two publishers can repeat the same upstream error despite distinct domains.
- Public content drift can cause disagreement; failure to reach consensus is a
  deliberate fail-closed outcome.
- DNS rebinding requires operational controls or a strict domain allowlist.

## Verification evidence

- Pinned GenVM runner; GenVM lint and SDK validation pass.
- Standalone direct suite: 3 passed, including explicit conflict and malicious
  leader rejection.
- StudioNet deployment and resolution are finalized with `SUCCESS`, 3 agree / 2
  idle, no storage warning, and two supporting independent observations.
- Live state: `RESOLVED`, outcome `YES`.
- Bradbury status remains governed by the separate deployment manifest.

This is an engineering assessment, not formal verification or a financial or
legal guarantee.
