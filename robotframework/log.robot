*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
LoginTest
    Open Browser    https://demo.nopcommerce.com/    Chrome
    maximize browser window
    Click Link    xpath:/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a
    Input Text    id:Email    pavanoltraining@gmail.com
    Input Text    id:Password    Test@123
    Click Element    xpath:/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button