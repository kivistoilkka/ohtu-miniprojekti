*** Settings ***
Resource  resource.robot
Test Setup  Reset Database

*** Test Cases ***
Add Book Reference Successful
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  book_reference
    Data In Database Length Should Be  1

Add Second Book Reference Successful
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  book_reference
    Add Reference Values  testiauthor  toinen title  0001  testipublisher  def  book_reference
    Data In Database Length Should Be  2

Add Existing Book Reference Fails
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  book_reference
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  book_reference
    Data In Database Length Should Be  1

*** Keywords ***
Add Reference Values
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${ref_type_str}
    Add Reference  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${ref_type_str}