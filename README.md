# Source-Conflict Resolution Kernel

A reusable GenLayer consensus primitive for claims whose official or reputable
sources may disagree.

The constructor freezes 2-8 distinct source domains, source tiers, a minimum
confirmation count, and a deadline. Validators independently classify each
source as `SUPPORTS`, `REFUTES`, or `UNCLEAR`. Deterministic policy produces
`YES`, `NO`, `CONTESTED`, `UNAVAILABLE`, or `INCONCLUSIVE`, so disagreement is
recorded rather than hidden behind a forced binary answer.

## GenLayer-native decision

The contract makes a neutral shared decision from conflicting natural-language
evidence. Its custom validator independently recomputes and compares the
consequential status and outcome, not merely JSON format. Per-source
observations remain stored as audit metadata.

## Lifecycle and API

- Deploy in `OPEN` with frozen source domains, tiers, and confirmation policy.
- Call `resolve()` after the deadline. Confirmed claims become `RESOLVED`;
  conflicts and outages stay explicit rather than being forced to yes/no.
- Read the policy result and audit summary with `get_state()`.
- Downstream contracts must consume only finalized GenLayer transactions.

## Live evidence

- [StudioNet contract](https://explorer-studio.genlayer.com/address/0xF9CE275c6B10e335b4f1D51Aa805C586Ae1317d4)
- [Bradbury contract](https://explorer-bradbury.genlayer.com/address/0x44826C9FF1bDa39CB14F60dB2C1de7833928b423)
- Exact receipts and current finality are recorded in `deployments/`.

## Verify

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/SourceConflictKernel.py
pytest tests -v
```

See `docs/SECURITY_AUDIT.md`, `docs/TEST_MATRIX.md`, and
`PORTAL_SUBMISSION.md` for reviewer evidence.
