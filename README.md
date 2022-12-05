# OhTu-miniprojekti

![CI badge](https://github.com/kivistoilkka/ohtu-miniprojekti/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/kivistoilkka/ohtu-miniprojekti/branch/main/graph/badge.svg?token=50Q0XDY2GC)](https://codecov.io/gh/kivistoilkka/ohtu-miniprojekti)

## Käyttöohje

- Lataa projekti koneellesi

- Tee alustustoimenpisteet antamalla projektikansiossa komento `python3 src/build.py` tai `poetry run invoke build`. HUOM! Komento alustaa tietokannan, joten se tulee tehdä vain silloin, kun tietokannan haluaa tyhjentää.

- Käynnistä ohjelma komennolla `python3 src/index.py` tai `poetry run invoke run`.

- Ohjelmassa voi tällä hetkellä luoda BibTex-tiedoston komennolla 1, tarkastella lisättyjä viitteitä komennolla 2, lisätä viitteitä komennolla 3 ja poistaa viitteitä komennolla 4. Ohjelmasta poistutaan komennolla 5.

## Komentorivikomennot

- Ohjelman käynnistys:
```bash
poetry run invoke run
```
- Tietokannan alustaminen:
```bash
poetry run invoke build
```
- Ohjelman testaus:
```bash
poetry run invoke test
```
- Testikattavuusraportin luominen:
```bash
poetry run invoke coverage-report
```
- Robot Framework -testit:
```bash
poetry run robot src/tests/
```
- Pylint-tarkistus:
```bash
poetry run invoke lint
```
- Koodin formatointi autopep8:lla:
```bash
poetry run invoke format
```

## Dokumentaatio

[Product backlog](https://github.com/users/kivistoilkka/projects/1)

[Sprint backlog](https://docs.google.com/spreadsheets/d/1ucSjkzkqewl7hF1RMTIi3dRhN4YwD-RomEDwHivYZaI/)

[Robot Frameworkin tiedostot](https://github.com/kivistoilkka/ohtu-miniprojekti/tree/main/src/tests)

## Definition of done

* User storyja vastaavat hyväksymiskriteerit dokumentoidaan Robot frameworkin syntaksilla, ja Robot-testitiedostoihin on linkki README:stä
* Toteutetun koodin testikattavuus on n. 70 % ja toteutetut yksikkötestit testaavat järkeviä tapauksia
* Ohjelmiston lähdekoodi ja testien tilanne on nähtävissä GitHubissa, ja README-tiedostossa on nähtävillä jatkuvan integraation (GitHub Actions) tilanne
* Luokat, metodit ja muuttujat on nimetty järkevästi ja noudattavat määriteltyjä Pylint-sääntöjä
* Sovellus on laadittu repository-suunnittelumallia noudattaen
