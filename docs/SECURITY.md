# Threat model and security notes

## Threats addressed

- **Malicious leader:** validators independently fetch evidence and recompute
  decision fields; a well-formed but false leader output is rejected.
- **Prompt injection:** fetched pages are delimited as untrusted evidence and
  the prompts instruct models to ignore embedded commands.
- **Source drift:** only bounded extracts and canonical statuses are returned;
  raw HTML is never stored as the authoritative result.
- **Source outage:** unavailable pages produce `UNRESOLVED`, `UNAVAILABLE`, or
  `NEEDS_CLARIFICATION`; they never silently settle a market.
- **Conflicting evidence:** SourceConflictKernel records `CONTESTED`, and the
  other resolvers use `INCONCLUSIVE` where a decision cannot be justified.
- **Replay/double resolution:** terminal states return their current state or
  reject further writes; attempts are recorded for auditability.
- **Premature resolution:** each resolver checks a deterministic transaction
  timestamp against its frozen deadline.
- **Unbounded inputs:** constructor fields, criteria, rule counts, source counts,
  URL lengths, and fetched content lengths are capped.
- **Credential leakage:** HTTPS URLs containing userinfo are rejected.

## Deliberate non-goals

- This repository does not claim that an external webpage is authentic merely
  because it is reachable.
- It does not provide legal arbitration or guarantee market solvency.
- It does not send irreversible payouts; a payment wrapper should invoke a
  resolver only after the network's finality window and use idempotent claims.
- It does not allow market rules to be edited after deployment.

## Operational requirements

Use public, stable, source-specific URLs. Prefer immutable reports, official
records, or signed attestations. Before production use, add allowlists for
domains and a finality-aware payout adapter.

The dated audit, remediated findings, and residual-risk register are in
`docs/SECURITY_AUDIT.md`.
