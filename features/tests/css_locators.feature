Feature: Verify empty cart message
  # Enter feature description here

  Scenario: target cart empty
    Given Open target website
    When Click the cart
    Then Verify Cart is empty