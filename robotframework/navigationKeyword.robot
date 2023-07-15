*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
Navigation
    Open Browser    https://www.google.com    chrome
    maximize browser window
    ${loc}=     get location
    log to console      ${loc}
    sleep   4

    go to       https://www.facebook.com
    ${loc}=     get location
    log to console      ${loc}
    sleep   4

    go back
    ${loc}=     get location
    log to console      ${loc}
    sleep   4


