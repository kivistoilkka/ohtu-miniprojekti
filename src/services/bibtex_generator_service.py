class BibtexGeneratorService:
    def __init__(self):
        pass

    def create_bibtex_file(self, refs: dict, filename: str):
        # Raise an error if all the reference lists are empty
        if not any(refs.values()):
            raise ValueError(
                "Lisättyjä viitteitä ei ole, joten BibTeX-tiedostoa ei voi luoda!")
        if not filename.endswith(".bib"):
            filename += ".bib"

        with open(filename, "w") as file:
            for type, ref_list in refs.items():
                if type == "book_references":
                    for ref in ref_list:
                        bib_key = ref.bib_key
                        author = BibtexGeneratorService._replace_scandinavic_characters(
                            ref.author)
                        title = BibtexGeneratorService._replace_scandinavic_characters(
                            ref.title)
                        publisher = BibtexGeneratorService._replace_scandinavic_characters(
                            ref.publisher)
                        year = ref.year

                        BibtexGeneratorService._write_book_ref_to_bibtex_file(
                            file, bib_key, author, title, publisher, year)
                elif type == "web_references":
                    for ref in ref_list:
                        bib_key = ref.bib_key
                        author = BibtexGeneratorService._replace_scandinavic_characters(
                            ref.author)
                        title = BibtexGeneratorService._replace_scandinavic_characters(
                            ref.title)
                        url = ref.url
                        year = ref.year

                        BibtexGeneratorService._write_web_ref_to_bibtex_file(
                            file, bib_key, author, title, url, year)
                else:
                    raise ValueError(
                        "Vain kirja- ja verkkosivuviitteet ovat sallittuja!")

    @staticmethod
    def _replace_scandinavic_characters(string: str):
        replacements = {
            "å": "{\\aa}",
            "Å": "{\\aA}",
            "ä": '{\\"a}',
            "Ä": '{\\"A}',
            "ö": '{\\"o}',
            "Ö": '{\\"O}'
        }

        for key, value in replacements.items():
            string = string.replace(key, value)
        return string

    @staticmethod
    def _write_book_ref_to_bibtex_file(file, bib_key, author, title, publisher, year):
        file.write(f'@book{{{bib_key},\n')
        file.write(f'  author     = "{author}",\n')
        file.write(f'  title      = "{title}",\n')
        file.write(f'  publisher  = "{publisher}",\n')
        file.write(f'  year       = {year}\n')
        file.write('}\n\n')

    @staticmethod
    def _write_web_ref_to_bibtex_file(file, bib_key, author, title, url, year):
        file.write(f'@misc{{{bib_key},\n')
        file.write(f'  author     = "{author}",\n')
        file.write(f'  title      = "{title}",\n')
        file.write(f'  url        = "{url}",\n')
        file.write(f'  year       = {year}\n')
        file.write('}\n\n')
