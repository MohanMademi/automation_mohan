*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
LoginTest
    Open Browser    https://testautomationpractice.blogspot.com/    Chrome
    maximize browser window
    double click element    //*[@id="HTML10"]/div[1]/button
    sleep   4
    close browser
