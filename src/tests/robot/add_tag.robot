*** Settings ***
Resource  resource.robot
Test Setup  Reset Database

*** Test Cases ***
Tag Can Be Added To Reference
    Add Entry To Database  Testaaja1  Testikirja1  2001  Unigrafia  test01  tag1  book_reference
    View Ref  2  1  tag1  book_references
    Output Should Contain  tag1

Can Add Reference Without Tag
    Add Entry To Database  Testaaja1  Testikirja1  2001  Unigrafia  test01  ${EMPTY}  book_reference
    View Ref  2  1  ${EMPTY}  book_references
    Output Should Contain  test01