*** Settings ***
Library          SeleniumLibrary

*** Variables ***
${BROWSER}       headlesschrome
${URL}           https://www.facebook.com/
${VALID_USERNAME}    6302935408
${VALID_PASSWORD}    mohan9642

*** Test Cases ***
Post_Pic
    open browser    ${URL}      ${BROWSER}
    Input Text      id=email        ${VALID_USERNAME}
    Input Text      id=pass         ${VALID_PASSWORD}
    Click Element       name=login
    sleep       5
#    Switch To Alert    action=ACCEPT
#    Log    Alert Accepted
#    sleep       3
#select_pic
#    Click Element       xpath=//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft'])[5
#    Click Element       xpath=//*[@id="mount_0_0_Vz"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]/div/span/span
#    Click Element       //*[@id="mount_0_0_Vz"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]
#    Choose File     "C:\Users\madem\OneDrive\Pictures\Screenshots\Screenshot 2023-07-05 161223.png"        /path/to/your/image.jpg
#    Click Element      xpath=//*[@id="mount_0_0_Vz"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div

