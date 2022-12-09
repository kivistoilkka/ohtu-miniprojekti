*** Settings ***
Resource  resource.robot
Test Setup  Reset Database And Add Multiple Entries To Database

*** Test Cases ***
All References Are Listed
    Data In Database Length Should Be  3

References Are In Correct Order By Year Ascending
    View Ref  1  1  book_references
    Output Should Contain  test02
    Output Should Contain  test01
    Output Should Contain  test03

References Are In Correct Order By Year Descending
    View Ref  1  2  book_references
    Output Should Contain  test03
    Output Should Contain  test01
    Output Should Contain  test02

References Are In Correct Order By Adding Date Ascending
    View Ref  2  1  book_references
    Output Should Contain  test01
    Output Should Contain  test02
    Output Should Contain  test03

References Are In Correct Order By Adding Date Descending
    View Ref  2  2  book_references
    Output Should Contain  test03
    Output Should Contain  test02
    Output Should Contain  test01
    

*** Keywords ***
Add Multiple Entries To Database
    Create Database Entry  Testaaja1  Testikirja1  2001  Unigrafia  test01  book_reference
    Create Database Entry  Testaaja2  Testikirja2  2000  Unigrafia  test02  book_reference
    Create Database Entry  Testaaja3  Testikirja3  2002  Unigrafia  test03  book_reference

Add Entry To Database
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${ref_type_str}
    Create Database Entry  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${ref_type_str}

Reset Database And Add Multiple Entries To Database
    Reset Database
    Add Multiple Entries To Database
