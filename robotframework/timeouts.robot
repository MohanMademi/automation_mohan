*** Settings ***
Library  SeleniumLibrary

*** Variables ***
#${browser}  chrome
#${url}      https://www.practiceselenium.com/practice-form.html



*** Test Cases ***
login
    Open Browser    https://testautomationpractice.blogspot.com/      chrome
#    RadioButtons
    CheckBoxes
    close browser
*** Keywords ***
CheckBoxes
    set selenium speed      2 seconds
    select from list by label       colors      Red
#    sleep   3
    select from list by label       colors      Green
#    sleep   3
    select from list by label       colors      Blue
#    sleep   3
    unselect from list by label       colors      Green
#    sleep   3
    ${speed}=   get selenium speed
    log to console      ${speed}