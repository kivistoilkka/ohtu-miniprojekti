*** Settings ***
Resource  resource.robot
Test Setup  Reset Database

*** Test Cases ***
Add Web Reference With Tag Successful
    Add Web Reference Values  testiauthor  testititle  0000  https://www.google.com/  abc  tag1  web_reference
    Data In Database Length Should Be  1

Add Web Reference Without Tag Successful
    Add Web Reference Values  testiauthor  testititle  0000  https://www.google.com/  abc  ${EMPTY}  web_reference
    Data In Database Length Should Be  1

Add Second Web Reference Successful
    Add Web Reference Values  testiauthor  testititle  0000  https://www.google.com/  abc  tag1  web_reference
    Add Web Reference Values  testiauthor  toinen title  0001  https://www.google.com/  def  tag2  web_reference
    Data In Database Length Should Be  2

Add Existing Web Reference Fails
    Add Web Reference Values  testiauthor  testititle  0000  https://www.google.com/  abc  tag1  web_reference
    Add Web Reference Values  testiauthor  testititle  0000  https://www.google.com/  abc  tag1  web_reference
    Data In Database Length Should Be  1


*** Keywords ***
Add Web Reference Values
    [Arguments]  ${author}  ${title}  ${year}  ${url}  ${key}  ${tag}  ${ref_type_str}
    Add Reference  ${author}  ${title}  ${year}  ${url}  ${key}  ${tag}  ${ref_type_str}