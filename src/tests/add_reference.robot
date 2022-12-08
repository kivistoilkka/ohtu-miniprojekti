*** Settings ***
Resource  resource.robot
Test Setup  Reset Database

*** Test Cases ***
Add Reference Successful
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag1
    Data In Database Length Should Be  1

Add Second Reference Successful
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag1
    Add Reference Values  testiauthor  toinen title  0001  testipublisher  def  tag2
    Data In Database Length Should Be  2

Add Existing Reference
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag1
    Add Reference Values  testiauthor  testititle  0000  testipublisher  abc  tag2
    Data In Database Length Should Be  1

*** Keywords ***
Add Reference Values
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${tag}
    Add Reference  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${tag}