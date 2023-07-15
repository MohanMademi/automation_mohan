*** Settings ***
Documentation    Test suite for API integration testing
Library          RequestsLibrary

*** Variables ***
${BASE_URL}    http://api.example.com
${VALID_USER}    johnsmith@example.com
${VALID_PASSWORD}    Pass1234

*** Test Cases ***
Get User Details
    [Documentation]    Test case to verify getting user details from API
    Create Session    example_api    ${BASE_URL}
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${payload}=    Create Dictionary    username=${VALID_USER}    password=${VALID_PASSWORD}
    ${response}=    Post Request    example_api    /login    headers=${headers}    json=${payload}
    ${access_token}=    Set Variable    ${response.json()['access_token']}
    ${headers}=    Create Dictionary    Authorization=Bearer ${access_token}
    ${response}=    Get Request    example_api    /user    headers=${headers}
    Should Be Equal As Strings    ${response.status_code}    200
    Should Contain    ${response.json()}    ${VALID_USER}
    Delete All Sessions