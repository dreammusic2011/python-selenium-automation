Feature: Test Scenarios for links


  Scenario: Verify Target Circle Links
    Given Open Target Circle page
    Then Verify 15 links


  Scenario Outline: Search for product on Target
    Given Open Target main page
    When search for <search_word>
    When Add to cart
    Then Verify in cart for <expected_text>

    Examples:
    |search_word  |expected_text  |
    |tea          |tea            |
    |lotion       |lotion         |
    |cleaner      |cleaner        |
    #