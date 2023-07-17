*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
login
    Open Browser    https://testautomationpractice.blogspot.com/      headlesschrome
    maximize browser window
    execute javascript      window.scroll(0,400)
    sleep   2
#    scroll element into view        id:pagination
#    sleep   3
    execute javascript      window.scroll(0,document.body.scrollHeight)
    sleep       3
    execute javascript      window.scroll(0,-document.body.scrollHeight)
    sleep   3
    close browser
