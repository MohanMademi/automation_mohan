*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
Navigation
    Open Browser    https://testautomationpractice.blogspot.com/    chrome
    maximize browser window

    capture element screenshot      xpath://*[@id="HTML9"]/div[1]/button[2]    C:/Users/madem/PycharmProjects/automationtesting/element_sceenshot.png
    capture page screenshot      C:/Users/madem/PycharmProjects/automationtesting/page_screeshot.png

    close browser