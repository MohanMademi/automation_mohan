*** Settings ***
Library  SeleniumLibrary

*** Variables ***
#${browser}  chrome
#${url}      https://www.practiceselenium.com/practice-form.html



*** Test Cases ***
login
    Open Browser    https://testautomationpractice.blogspot.com/      chrome
    RadioButtons
    close browser
*** Keywords ***
RadioButtons
    maximize browser window
    select radio button     gender         female
    sleep   5
    select checkbox      sunday
    sleep   3
    select checkbox      friday
    sleep   5
    unselect checkbox   sunday
    sleep   5
    select radio button   gender      male
    sleep   5

