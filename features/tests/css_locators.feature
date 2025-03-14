Feature: Verify empty cart message
  # Enter feature description here

  Scenario: target cart empty
    Given Open target.com
    When Click on Cart icon
    Then Verify Cart is empty

  Scenario: Navigate to sign in
    Given Open target.com
    When Click Sign In
    When Sign In from menu
    Then Verify sign in page