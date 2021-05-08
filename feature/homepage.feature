@sanity
Feature: HomePage Validation

  Scenario: The homepage should have correct title
    Given User go to the site
    Then Page title should be "Zoho - Cloud Software Suite and SaaS Applications for Businesses"


  Scenario: The homepage should have correct url
    Given User go to the site
    Then URL should be "https://www.zoho.com/"