Feature: CLI basics
  The template CLI greets users by name.

  Scenario: Show version
    When I run the CLI with "--version"
    Then the exit code is 0
    And the output contains "template-python-cli"

  Scenario: Greet a user
    When I run the CLI with "hello World"
    Then the exit code is 0
    And the output contains "Hello, World!"

  Scenario: Whitespace name produces error
    When I greet with whitespace
    Then the exit code is 1
    And the error output contains "Name cannot be empty"
