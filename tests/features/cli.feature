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

  Scenario: Info command shows environment
    When I run "info"
    Then the exit code should be 0
    And the output should contain "template-cli"
    And the output should contain "Environment:"
    And the output should contain "TTY detected:"

  Scenario: Environment variable for name
    Given environment variable "TEMPLATE_CLI_NAME" is set to "EnvUser"
    When I run "hello"
    Then the exit code should be 0
    And the output should contain "Hello, EnvUser!"

  Scenario: CLI argument overrides environment variable
    Given environment variable "TEMPLATE_CLI_NAME" is set to "EnvUser"
    When I run "hello CliUser"
    Then the exit code should be 0
    And the output should contain "Hello, CliUser!"

  Scenario: Config command shows default location
    When I run "config"
    Then the exit code should be 0
    And the output should contain "Configuration File:"
    And the output should contain "Default location:"

  Scenario: Config init creates file
    Given a temporary directory
    When I run config init with path to temp directory
    Then the exit code should be 0
    And the output should contain "Created config file:"
    And the config file should exist

  Scenario: Info command shows config section
    When I run "info"
    Then the exit code should be 0
    And the output should contain "Configuration:"
