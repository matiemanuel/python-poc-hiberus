Feature: Hiberus homepage

  Background:
    Given launch a new browser
    And Hiberus homepage is displayed

  Scenario: Hiberus Markets page is displayed
    When the user accepts page cookies
    And the user clicks on "Mercados" link from the top bar
    Then the hiberus market page is displayed
    And browser is closed

  Scenario: Hiberus Work With Us page is displayed
    When the user accepts page cookies
    And the user clicks on "Trabaja en Hiberus" link from the top bar
    Then the hiberus job opportunities page is displayed
    And browser is closed


