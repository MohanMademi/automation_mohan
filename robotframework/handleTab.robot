*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
login
    Open Browser    https://demo.automationtesting.in/windows.html      chrome
    maximize browser window
    click element   xpath://*[@id='Tabbed']/a/button
    select window       title=Samkinalium | Home
    click element       xpath://*[@id='container']/header/div/div/div[2]/ul/li[4]/a
    sleep   3
    close browser