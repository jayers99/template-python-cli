Feature: CLI Patterns
  The template CLI demonstrates key patterns for production CLIs.

  Scenario: Show version
    When I run the CLI with "--version"
    Then the exit code should be 0
    And the output should contain the version number

  Scenario: Greet a user
    When I run "hello World"
    Then the exit code should be 0
    And the output should contain "Hello, World!"

  Scenario: Verbose mode shows diagnostics
    When I run "hello --verbose Alice"
    Then the exit code should be 0
    And stderr should contain "Processing greeting for"
    And stdout should contain "Hello, Alice!"

  Scenario: Quiet mode suppresses output
    When I run "hello --quiet Bob"
    Then the exit code should be 0
    And stdout should be empty

  Scenario: Empty name fails validation
    When I run "hello ''"
    Then the exit code should be 65
    And stderr should contain "Error: Name cannot be empty"
    And stderr should contain "Hint:"

  Scenario: Whitespace-only name fails validation
    When I run "hello '   '"
    Then the exit code should be 65
    And stderr should contain "Error: Name cannot be empty"
