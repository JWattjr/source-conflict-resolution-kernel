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
evidence. Its custom validator compares the complete normalized per-source
observation set and the derived outcome, not merely JSON format.

## Verify

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/SourceConflictKernel.py
pytest tests -v
```

See `docs/SECURITY_AUDIT.md`, `docs/TEST_MATRIX.md`, and
`PORTAL_SUBMISSION.md` for reviewer evidence.
