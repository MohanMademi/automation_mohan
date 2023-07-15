*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
DragAndDrop
    Open Browser    https://testautomationpractice.blogspot.com/    Chrome
    maximize browser window
    drag and drop   xpath://*[@id="draggable"]/p        xpath://*[@id="droppable"]
    sleep   4
    close browser
