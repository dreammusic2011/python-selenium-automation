# Created by derekwest at 9/25/24
Feature: # Test for target search


  Scenario: # User can search for a product
    Given the target page
    When Click the cart
    Then Verify search results

  Scenario: # User can go to sign in
    Given the sign in page
    When Click on sign in
    Then Verify sign in page