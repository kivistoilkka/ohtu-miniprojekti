class BibtexGeneratorService:
    def __init__(self):
        pass

    def create_bibtex_file(self, refs, filename):
        with open(filename, "w") as file:
            for ref in refs:
                file.write(f'@Book{{{ref.bib_key},\n')
                file.write(f'  author     = "{_change_scandinavic_characters(ref.author)}",\n')
                file.write(f'  title      = "{_change_scandinavic_characters(ref.title)}",\n')
                file.write(f'  publisher  = "{_change_scandinavic_characters(ref.publisher)}",\n')
                file.write(f'  year       = {ref.year}\n')
                file.write('}\n\n')

def _change_scandinavic_characters(string: str):
    string = string.replace("å", "{\\aa}")
    string = string.replace("Å", "{\\aA}")
    string = string.replace("ä", '{\\"a}')
    string = string.replace("Ä", '{\\"A}')
    string = string.replace("ö", '{\\"o}')
    string = string.replace("Ö", '{\\"O}')
    return string