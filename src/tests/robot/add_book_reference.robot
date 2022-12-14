*** Settings ***
Resource  resource.robot
Test Setup  Reset Database

*** Test Cases ***
Add Book Reference With Tag Successful
    Add Book Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag1  book_reference
    Data In Database Length Should Be  1

Add Book Reference Without Tag Successful
    Add Book Reference Values  testiauthor  testititle  0000  testipublisher  abc  ${EMPTY}  book_reference
    Data In Database Length Should Be  1

Add Second Book Reference Successful
    Add Book Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag1  book_reference
    Add Book Reference Values  testiauthor  toinen title  0001  testipublisher  def  tag2  book_reference
    Data In Database Length Should Be  2

Add Existing Book Reference Fails
    Add Book Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag1  book_reference
    Add Book Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag1  book_reference
    Data In Database Length Should Be  1

*** Keywords ***
Add Book Reference Values
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${tag}  ${ref_type_str}
    Add Reference  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${tag}  ${ref_type_str}