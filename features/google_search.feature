Feature: Google Search

  Scenario: Search to car siena 2007
    Given in the google page
    When search to "Siena 2007"
    And press enter
    Then show the text "Imagens"