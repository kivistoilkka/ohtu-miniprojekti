*** Settings ***
Resource  resource.robot
Test Setup  Reset Database And Add Multiple Entries To Database

*** Test Cases ***
Correct File With Correct Content Is Created
    Write Data To Bibtex File
    Data In Bibtex File Should Be  test.bib
    
*** Keywords ***
Write Data To Bibtex File
    Create Bibtex File  Testaaja1  Testikirja1  2001  Unigrafia  test01  tag  test.bib
