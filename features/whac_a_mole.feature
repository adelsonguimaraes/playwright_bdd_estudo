Feature: Whack a mole

    Scenario: Hit until complete 40 points
        Given in the Whac a mole page
        When hit in mole unitl 40 points
        Then received 40 points

    Scenario: Hit until complete 60 points
        Given in the Whac a mole page
        When hit in mole unitl 60 points
        Then received 60 points

    Scenario: Hit until complete 80 points
        Given in the Whac a mole page
        When hit in mole unitl 80 points
        Then received 80 points