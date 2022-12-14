*** Settings ***
Resource  resource.robot
Test Setup  Reset Database And Add Multiple Entries To Database

*** Test Cases ***
All References Are Listed
    Data In Database Length Should Be  3

References Are In Correct Order By Year Ascending
    View Ref  1  1  ${EMPTY}  book_references
    Output Should Contain  test02
    Output Should Contain  test01
    Output Should Contain  test03

References Are In Correct Order By Year Descending
    View Ref  1  2  ${EMPTY}  book_references
    Output Should Contain  test03
    Output Should Contain  test01
    Output Should Contain  test02

References Are In Correct Order By Adding Date Ascending
    View Ref  2  1  ${EMPTY}  book_references
    Output Should Contain  test01
    Output Should Contain  test02
    Output Should Contain  test03

References Are In Correct Order By Adding Date Descending
    View Ref  2  2  ${EMPTY}  book_references
    Output Should Contain  test03
    Output Should Contain  test02
    Output Should Contain  test01
