# ADR 003: Use pytest-bdd for Behavior-Driven Testing

## Status

Accepted

## Context

We need a testing strategy that:

- Documents expected behavior in human-readable format
- Validates the CLI from a user's perspective
- Integrates with existing pytest infrastructure
- Supports both acceptance tests and unit tests

## Decision

Use **pytest-bdd** for behavior-driven development (BDD) testing alongside regular pytest unit tests.

## Rationale

- **Gherkin syntax**: Feature files serve as living documentation
- **pytest integration**: Reuses existing fixtures, plugins, and configuration
- **User perspective**: Scenarios describe behavior, not implementation
- **Separation of concerns**: Feature files for acceptance, unit tests for internals
- **Consistent with Praxis**: Matches praxis-ai's testing approach

## Consequences

### Positive

- Tests double as documentation
- Non-technical stakeholders can read/write scenarios
- Clear distinction between "what" (features) and "how" (step definitions)
- pytest's full ecosystem remains available

### Negative

- Additional dependency (pytest-bdd)
- Learning curve for Gherkin syntax
- Step definitions require maintenance alongside features

## Test Structure

```
tests/
├── features/           # Gherkin feature files
│   └── cli.feature
├── step_defs/          # Step implementations
│   └── test_cli.py
├── conftest.py         # Shared fixtures
└── test_domain.py      # Unit tests (pure pytest)
```

## Example

```gherkin
# tests/features/cli.feature
Feature: CLI Commands
  Scenario: Show version
    When I run the CLI with --version
    Then the output should contain the version number
```

```python
# tests/step_defs/test_cli.py
@when("I run the CLI with --version")
def run_version(cli_runner, context):
    context["result"] = cli_runner.invoke(app, ["--version"])
```

## References

- [pytest-bdd documentation](https://pytest-bdd.readthedocs.io/)
- [Gherkin syntax](https://cucumber.io/docs/gherkin/)
