*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
login
    Open Browser    https://testautomationpractice.blogspot.com/      chrome
    maximize browser window
    click button    xpath://*[@id="HTML9"]/div[1]/button[2]
#    handle alert    accept
#    handle alert    dismiss
#    handle alert    leave
    alert should be present  Press a button!
    sleep   3