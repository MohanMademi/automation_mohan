*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
login
    Open Browser    https://demo.nopcommerce.com/      chrome
    maximize browser window
    sleep   3

    Open Browser    https://www.google.com    chrome
    maximize browser window

    sleep   2

    switch browser  1
    ${title1}=   get title
    log to console      ${title1}
    sleep   4

    switch browser  2
    ${title2}=   get title
    log to console      ${title2}
    sleep   4

    close all browsers