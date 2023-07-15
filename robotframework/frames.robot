*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
login
    Open Browser    https://seleniumhq.github.io/selenium/docs/api/java/index     chrome
    maximize browser window

    select frame    xpath:/html/body/header/nav/div[1]/div[2]/ul[1]/li[1]/a
    click link  org.openqa.selenium
    unselect frame
    sleep   3


    select frame    packageframe
    click link  WerbDriver
    unselect frame
    sleep   3


    select frame    classFrame
    click link  Help
    unselect frame
    sleep   3

    close browser
