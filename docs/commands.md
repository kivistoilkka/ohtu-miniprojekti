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
