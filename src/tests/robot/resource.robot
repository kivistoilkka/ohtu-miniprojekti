*** Settings ***
Library  ../../ReferenceLibrary.py

*** Keywords ***
Add Multiple Entries To Database
    Create Database Entry  Testaaja1  Testikirja1  2001  Unigrafia  test01  tag1  book_reference
    Create Database Entry  Testaaja2  Testikirja2  2000  Unigrafia  test02  tag2  book_reference
    Create Database Entry  Testaaja3  Testikirja3  2002  Unigrafia  test03  tag1  book_reference

Add Entry To Database
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${tag}  ${ref_type_str}
    Create Database Entry  ${author}  ${title}  ${year}  ${publisher}  ${key}  ${tag}  ${ref_type_str}

Add Entry To Database Without Tag
    Create Database Entry  Testaaja4  Testikirja4  2003  Unigrafia  test04  ${EMPTY}  book_reference

Reset Database And Add Multiple Entries To Database
    Reset Database
    Add Multiple Entries To Database
