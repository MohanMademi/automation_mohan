*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
login
    Open Browser    https://testautomationpractice.blogspot.com/      chrome
    maximize browser window

    Open Browser    https://www.google.com/     chrome
    maximize browser window
    sleep   2

    close all browsers