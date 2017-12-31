Feature: Login to gmail
As a registered gmail user I want to login to gmail, so I can see my emails

    Scenario: Successful login to gmail
        Given I'm on gmail login page
        When I enter proper email
        And I enter "proper" password
        And I click next button
        And I go to e-mails
        Then I am redirected to gmail homepage, so I can see my emails

    Scenario: Unable to login
        Given I'm on gmail login page
        When I enter proper email
        And I enter "wrong" password
        And I click next button
        Then user​ ​is​ informed​ ​about​ wrong​ ​credentials

    Scenario: No password
        Given I'm on gmail login page
        When I enter proper email
        And I click next button
        Then user is asked to enter password
