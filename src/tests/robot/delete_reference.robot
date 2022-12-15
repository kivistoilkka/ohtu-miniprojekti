*** Settings ***
Resource  resource.robot
Test Setup  Reset Database And Add Book And Web Entries To Database

*** Test Cases ***
Delete One Book Reference Removes Correct Reference
    Data In Database Length Should Be  6
    Delete Reference  test02
    Data In Database Length Should Be  5
    View Ref  2  1  ${EMPTY}  book_references
    Output Should Contain  test01
    Output Should Contain  test03

Delete One Web Reference Removes Correct Reference
    Data In Database Length Should Be  6
    Delete Reference  test05
    Data In Database Length Should Be  5
    View Ref  2  1  ${EMPTY}  web_references
    Output Should Contain  test04
    Output Should Contain  test06

*** Keywords ***
Reset Database And Add Book And Web Entries To Database
    Reset Database
    Create Database Entry  Testaaja1  Testikirja1  2001  Unigrafia  test01  tag1  book_reference
    Create Database Entry  Testaaja2  Testikirja2  2000  Unigrafia  test02  tag2  book_reference
    Create Database Entry  Testaaja3  Testikirja3  2002  Unigrafia  test03  tag1  book_reference
    Create Database Entry  Testaaja4  Testisivu1  2003  http://  test04  tag1  website_reference
    Create Database Entry  Testaaja5  Testisivu2  1999  http://  test05  tag2  website_reference
    Create Database Entry  Testaaja6  Testisivu3  2022  http://  test06  tag1  website_reference
