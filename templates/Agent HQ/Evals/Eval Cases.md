# Eval Cases

Reusable behavior cases for preventing regressions.

Add a case only when a run reveals a reusable failure, near-miss, or unusually good behavior.

## Case Template

### YYYY-MM-DD Short Name

- Request:
- Required sources:
- Expected behavior:
- Forbidden behavior:
- Source trace expectations:
- Pass/fail notes:

For an enabled memory instance, seed local cases from the distribution's synthetic `examples/memory-evaluation-cases.json`. Keep private observations in the private instance; contribute only independently fictionalized cases upstream. A copied fixture is not a completed evaluation.
