# OhTu-miniprojekti

![CI badge](https://github.com/kivistoilkka/ohtu-miniprojekti/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/kivistoilkka/ohtu-miniprojekti/branch/main/graph/badge.svg?token=50Q0XDY2GC)](https://codecov.io/gh/kivistoilkka/ohtu-miniprojekti)

## Käyttöohje

Lataa projekti koneellesi ja asenna riippuvuudet

```
poetry install
```

Tee alustustoimenpisteet antamalla projektikansiossa.  
HUOM! Komento alustaa tietokannan, joten se tulee tehdä vain silloin, kun
tietokannan haluaa tyhjentää.

```
poetry run invoke build
```
- Ohjelman käynnistys
```bash
poetry run invoke run
```


Ohjelmassa voi tällä hetkellä luoda BibTex-tiedoston komennolla 1, tarkastella
lisättyjä viitteitä komennolla 2, lisätä viitteitä komennolla 3 ja poistaa
viitteitä komennolla 4. Ohjelmasta poistutaan komennolla 5.

## Dokumentaatio

[Komentorivikomennot](./docs/commands.md)

[Definition of Done](./docs/definition_of_done.md)

[Robot Frameworkin tiedostot](https://github.com/kivistoilkka/ohtu-miniprojekti/tree/main/src/tests/robot)

## Backlogit

[Product backlog](https://github.com/users/kivistoilkka/projects/1)

[Sprint backlog](https://docs.google.com/spreadsheets/d/1ucSjkzkqewl7hF1RMTIi3dRhN4YwD-RomEDwHivYZaI/)

