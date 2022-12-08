*** Settings ***
Library  ../ReferenceLibrary.py

*** Keywords ***
Add Multiple Entries To Database
    Create Database Entry  Testaaja1  Testikirja1  2001  Unigrafia  test01  tag1
    Create Database Entry  Testaaja2  Testikirja2  2000  Unigrafia  test02  tag2
    Create Database Entry  Testaaja3  Testikirja3  2002  Unigrafia  test03  tag1

Add Entry To Database
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${tag}
    Create Database Entry  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${tag}

Reset Database And Add Multiple Entries To Database
    Reset Database
    Add Multiple Entries To Database
