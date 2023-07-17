*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
LoginTest
    Open Browser    https://demo.nopcommerce.com/    Chrome
    maximize browser window
    Title Should Be    nopCommerce demo store
    Click Link    xpath:/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a
    ${"email_text"}     set variable    id:Email
    element should be visible     ${"email_text"}
    element should be enabled     ${"email_text"}

    input text      ${"email_text"}     mademimohan99@gmail.com
    sleep   5
    clear element text      ${"email_text"}
    sleep       5
    close browser


