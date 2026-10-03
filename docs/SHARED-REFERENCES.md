# Shared owner documentation

The shared contracts and runtime documentation are maintained in the `glide` owner repository. Use a trusted matching owner checkout or archive from the configured upstream source. Repository ownership is installation context; public templates do not hardcode a personal namespace.

Verify the owner commit against optional_memory_runtime.runtime_git_ref in `compatibility.json`. Set the GitHub Actions repository variable `GLIDE_CORE_REPOSITORY` to the verified owner/repository when the core lives elsewhere. By default, consumer CI checks the repository named `glide` under its current GitHub repository owner at that exact commit. If the owner checkout or upstream is unavailable, report the dependency gap; do not substitute an unverified repository or a moving branch.

The following paths resolve within the verified owner checkout, rather than this consumer repository.

## Setup

Read `docs/SETUP.md` for the shared runtime setup walkthrough.

## Validation

Read `docs/VALIDATION.md` for deterministic runtime and packaging checks and their limits.

## Storage and Git

Read `docs/STORAGE-AND-GIT.md` for SQLite, Markdown, synchronization and backup boundaries.

## Model screen

Read `examples/model-screen/README.md` for the earlier synthetic screen and its opt-in runner.

## Behavior screen

Read `docs/STREAMLINING-EVALUATION.md` for the paired public-policy results, earlier failures and limited targeted acceptance. These results do not establish private-instance or live-connector quality.
