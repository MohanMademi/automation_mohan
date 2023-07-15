*** Settings ***
Library  SeleniumLibrary

*** Variables ***
#${browser}  chrome
#${url}      https://www.practiceselenium.com/practice-form.html



*** Test Cases ***
login
    Open Browser    https://testautomationpractice.blogspot.com/      chrome
    RadioButtons
    CheckBoxes
    close browser
*** Keywords ***
RadioButtons
    maximize browser window
    Select from list by value       country     india
    sleep   2
    Select from list by index       country     2
    sleep   5
    Select from list by label       country     Japan
    sleep   5
CheckBoxes
    select from list by label       colors      Red
    sleep   3
    select from list by label       colors      Green
    sleep   3
    select from list by label       colors      Blue
    sleep   3
    unselect from list by label       colors      Green
    sleep   3


