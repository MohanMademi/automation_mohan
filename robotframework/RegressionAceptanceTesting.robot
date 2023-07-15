*** Settings ***
Documentation    Test suite for user registration
Library          SeleniumLibrary

*** Variables ***
${BROWSER}       chrome
${URL}           http://www.example.com
${VALID_USERNAME}    johnsmith
${VALID_PASSWORD}    Pass1234
${INVALID_USERNAME}  invaliduser
${INVALID_PASSWORD}  Invalid123

*** Test Cases ***
Valid User Registration
    [Documentation]    Test case to verify valid user registration
    Open Browser    ${URL}    ${BROWSER}
    Input Text    id=username    ${VALID_USERNAME}
    Input Text    id=password    ${VALID_PASSWORD}
    Click Button    id=register-btn
    Page Should Contain    Welcome, ${VALID_USERNAME}
    Close Browser

Invalid User Registration
    [Documentation]    Test case to verify invalid user registration
    Open Browser    ${URL}    ${BROWSER}
    Input Text    id=username    ${INVALID_USERNAME}
    Input Text    id=password    ${INVALID_PASSWORD}
    Click Button    id=register-btn
    Page Should Contain    Invalid username or password.
    Close Browser