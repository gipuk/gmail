Feature: Send e-mail
As a logged user I want to send e-mail to comuunicate with others.

    Scenario: Sending e-mail
        Given User is logged to gmail
        When I click compose button
        And I enter e-mail addres 
        And I enter e-mail subject
        And I enter text
        And I attach file
        And I click send button
        Then e-mail is sent

#     Scenario: Sending empty e-mail
#         Given User is logged to gmail
#         When I click compose button
#         And I enter e-mail addres 
#         And I enter e-mail subject
#         And I click send button
#         Then e-mail is sent
#  
#     Scenario: Cancel sending e-mail
#         Given User is logged to gmail
#         When I click compose button
#         And I enter e-mail addres
#         And I click cancel button
#         Then e-mail is not sent
