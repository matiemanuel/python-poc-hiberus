@regression
Feature: Hiberus homepage

  Background:
    Given Hiberus homepage is displayed

  @smoke @markets
  Scenario: Hiberus Markets page is displayed
    When the user accepts page cookies
    And the user clicks on "Mercados" link from the top bar
    Then the hiberus market page is displayed

  @work
  Scenario: Hiberus Work With Us page is displayed
    When the user accepts page cookies
    And the user clicks on "Trabaja en Hiberus" link from the top bar
    Then the hiberus job opportunities page is displayed


