# GenLayer Portal submission

**Contribution type:** Builder → Intelligent Contracts  
**Title:** Source-Conflict Resolution Kernel  
**Contribution date:** Use the actual date of the submitted release.

## Notes / Description

Built and deployed an MIT-licensed Source-Conflict Resolution Kernel, a reusable
GenLayer Intelligent Contract for prediction markets and oracles where public
sources may disagree. Deployment freezes 2-8 distinct source domains, source
tiers, a minimum confirmation policy, the claim, and deadline. The leader and
validators independently classify each source as SUPPORTS, REFUTES, or UNCLEAR;
the custom validator compares the normalized per-source observation set and
outcome. Deterministic policy produces YES, NO, CONTESTED, UNAVAILABLE, or
INCONCLUSIVE instead of forcing a false binary settlement. The contract rejects
private-network URLs and credentials, bounds fetched content, handles source
outages, prevents premature/repeated terminal resolution, and stores auditable
attempt metadata. Includes pinned GenVM source, validator tests, security audit,
test matrix, and StudioNet/Bradbury deployment records. It does not custody or
transfer funds.

## Evidence to add

1. GitHub Repository — replace with the private repository URL.
2. GitHub File — `contracts/SourceConflictKernel.py`.
3. GitHub File — `tests/test_source_conflict.py`.
4. GitHub File — `docs/SECURITY_AUDIT.md`.
5. GitHub File — `docs/TEST_MATRIX.md`.
6. GitHub File — `deployments/studionet.json`.
7. GitHub File — `deployments/bradbury.json`.
8. GenLayer Explorer Contract — replace with the finalized Bradbury address URL.
