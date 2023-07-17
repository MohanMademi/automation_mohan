*** Settings ***
Documentation    Test suite for login functionality
Library          SeleniumLibrary

*** Variables ***
${BROWSER}       chrome
${URL}           http://www.example.com
${VALID_USERNAME}    johnsmith
${VALID_PASSWORD}    Pass1234

*** Test Cases ***
Valid Login
    [Documentation]    Test case to verify valid login
    Open Browser    ${URL}    ${BROWSER}
    Input Text    id=username    ${VALID_USERNAME}
    Input Text    id=password    ${VALID_PASSWORD}
    Click Button    id=login-btn
    Page Should Contain    Welcome, ${VALID_USERNAME}
    Close Browser

Invalid Login
    [Documentation]    Test case to verify invalid login
    Open Browser    ${URL}    ${BROWSER}
    Input Text    id=username    invaliduser
    Input Text    id=password    Invalid123
    Click Button    id=login-btn
    Page Should Contain    Invalid username or password.
    Close Browser