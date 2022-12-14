*** Settings ***
Resource  resource.robot
Test Setup  Reset Database And Add Multiple Entries To Database

*** Test Cases ***
Filter By Tag Finds Correct References
    Add Entry To Database Without Tag
    View Ref  2  1  tag1  book_references
    Output Should Contain  test01
    Output Should Contain  test03

Filter By Tag Finds Both Books And Websites
    Create Database Entry  Testaaja1  TestiWebbisivu  2001  testurl.com  test11  tag1  website_reference
    View Ref  2  1  tag1  book_references
    View Ref  2  1  tag1  web_references
    Output Should Contain  test01
    Output Should Contain  test03
    Output Should Contain  test11


*** Keywords ***
