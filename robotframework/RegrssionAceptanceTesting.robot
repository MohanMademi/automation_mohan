*** Settings ***
Documentation    Test suite for shopping cart functionality
Library          SeleniumLibrary

*** Variables ***
${BROWSER}       chrome
${URL}           http://www.example.com
${PRODUCT_NAME}    Test Product
${PRODUCT_PRICE}   $10.00
${QUANTITY}        2

*** Test Cases ***
Add Product to Cart
    [Documentation]    Test case to verify adding a product to the shopping cart
    Open Browser    ${URL}    ${BROWSER}
    Click Link    ${PRODUCT_NAME}
    Input Text    id=quantity    ${QUANTITY}
    Click Button    id=add-to-cart
    Page Should Contain    Product added to the cart successfully.
    Close Browser

Remove Product from Cart
    [Documentation]    Test case to verify removing a product from the shopping cart
    Open Browser    ${URL}    ${BROWSER}
    Click Link    Shopping Cart
    Click Link    Remove    css=#cart-item-${PRODUCT_NAME} .remove-button
    Page Should Not Contain    ${PRODUCT_NAME}
    Close Browser