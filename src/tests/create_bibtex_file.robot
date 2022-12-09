*** Settings ***
Resource  resource.robot
Test Setup  Reset Database And Add Multiple Entries To Database

*** Test Cases ***
Correct File With Correct Content Is Created
    Write Data To Bibtex File
    Data In Bibtex File Should Be  test.bib
    
*** Keywords ***
Add Multiple Entries To Database
    Create Database Entry  Testaaja1  Testikirja1  2001  Unigrafia  test01  book_reference

Add Entry To Database
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${ref_type_str}
    Create Database Entry  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${ref_type_str}

Reset Database And Add Multiple Entries To Database
    Reset Database
    Add Multiple Entries To Database

Write Data To Bibtex File
    Create Bibtex File  Testaaja1  Testikirja1  2001  Unigrafia  test01  test.bib