*** Settings ***
Resource  resource.robot
Test Setup  Reset Database And Add Multiple Entries To Database

*** Test Cases ***
All References Are Listed
    Data In Database Length Should Be  3

All References Are In Correct Order
    View Ref
    Output Should Contain  test01
    Output Should Contain  test02
    Output Should Contain  test03

*** Keywords ***
Add Multiple Entries To Database
    Create Database Entry  Testaaja1  Testikirja1  2000  Unigrafia  test01
    Create Database Entry  Testaaja2  Testikirja2  2001  Unigrafia  test02
    Create Database Entry  Testaaja3  Testikirja3  2002  Unigrafia  test03

Add Entry To Database
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}  ${key}
    Create Database Entry  ${author}  ${title}  ${year}  ${publisher}  ${key}

Reset Database And Add Multiple Entries To Database
    Reset Database
    Add Multiple Entries To Database
