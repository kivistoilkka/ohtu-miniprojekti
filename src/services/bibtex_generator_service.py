class BibtexGeneratorService:
    def __init__(self):
        pass

    def create_bibtex_file(self, refs, filename):
        with open(filename, "w") as file:
            for ref in refs:
                file.write(f'@Book{{{ref.bib_key},\n')
                file.write(f'  author     = "{ref.author}",\n')
                file.write(f'  title      = "{ref.title}",\n')
                file.write(f'  publisher  = "{ref.publisher}",\n')
                file.write(f'  year       = {ref.year}\n')
                file.write('}\n\n')
