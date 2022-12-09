*** Settings ***
Resource  resource.robot
Test Setup  Reset Database

*** Test Cases ***
Add Book Reference With Tag Successful
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag1  book_reference
    Data In Database Length Should Be  1

Add Reference Without Tag Successful
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  ${EMPTY}  book_reference
    Data In Database Length Should Be  1

Add Second Book Reference Successful
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag1  book_reference
    Add Reference Values  testiauthor  toinen title  0001  testipublisher  def  tag2  book_reference
    Data In Database Length Should Be  2

Add Existing Book Reference Fails
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag1  book_reference
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag1  book_reference
    Data In Database Length Should Be  1


*** Keywords ***
Add Reference Values
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${tag}  ${ref_type_str}
    Add Reference  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${tag}  ${ref_type_str}
