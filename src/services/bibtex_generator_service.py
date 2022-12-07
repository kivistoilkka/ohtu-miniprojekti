class BibtexGeneratorService:
    def __init__(self):
        pass

    def create_bibtex_file(self, refs: list, filename: str):
        if len(refs) == 0:
            raise ValueError(
                "Lisättyjä viitteitä ei ole, joten BibTeX-tiedostoa ei voi luoda!")
        if not filename.endswith(".bib"):
            filename += ".bib"
            raise ValueError("Tiedostopäätteen tulee olla .bib!")

        with open(filename, "w") as file:
            for ref in refs:
                bib_key = ref.bib_key
                author = BibtexGeneratorService._replace_scandinavic_characters(
                    ref.author)
                title = BibtexGeneratorService._replace_scandinavic_characters(
                    ref.title)
                publisher = BibtexGeneratorService._replace_scandinavic_characters(
                    ref.publisher)
                year = ref.year

                BibtexGeneratorService._write_ref_to_bibtex_file(
                    file, bib_key, author, title, publisher, year)

    @staticmethod
    def _replace_scandinavic_characters(string: str):
        string = string.replace("å", "{\\aa}")
        string = string.replace("Å", "{\\aA}")
        string = string.replace("ä", '{\\"a}')
        string = string.replace("Ä", '{\\"A}')
        string = string.replace("ö", '{\\"o}')
        string = string.replace("Ö", '{\\"O}')
        return string

    @staticmethod
    def _write_ref_to_bibtex_file(file, bib_key, author, title, publisher, year):
        file.write(f'@Book{{{bib_key},\n')
        file.write(f'  author     = "{author}",\n')
        file.write(f'  title      = "{title}",\n')
        file.write(f'  publisher  = "{publisher}",\n')
        file.write(f'  year       = {year}\n')
        file.write('}\n\n')
