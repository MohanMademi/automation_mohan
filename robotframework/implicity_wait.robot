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
    maximize browser window
    ${implicittime}=   get selenium implicit wait
    log to console      ${implicittime}
    set selenium implicit wait     15 seconds
    select from list by label       colors      Red
    select from list by label       colors      Green
    select from list by label       colors      Blue
    unselect from list by label       colors      Green
    ${implicittime}=   get selenium implicit wait
    log to console      ${implicittime}