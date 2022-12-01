class UI:
    def __init__(self, app, reference_service, bibtex_generator):
        self.app = app
        self.ref_service = reference_service
        self.bibtex_generator = bibtex_generator

    def run(self):
        while True:
            options = int(input(
                "Mitä haluat tehdä?\n\
Luoda tiedosto, paina 1\n\
Tarkastella luotuja viitteitä, paina 2\n\
Lisää uusi viite, paina 3 \n\
Sulje ohjelma, paina 4\n"
            ))

            if options == 1:
                self.create_file()

            elif options == 2:
                self.view_ref()

            elif options == 3:
                self.add_ref()

            elif options == 4:
                break

    def create_file(self):
        filename = input("Minkä nimisen tiedoston haluat luoda?")

        data = self.ref_service.get_all_references()

        self.bibtex_generator.create_bibtex_file(data, filename)

    # def create_database(self):
    #     selection = input("Haluatko luoda uuden tietokannan (kyllä/ei)? ")
    #     if selection == "kyllä":
    #         self.app.db.create_tables(self.app.connection)

    def view_ref(self):

        data = self.ref_service.get_all_references()

        for ref in data:
            author = ref.author
            title = ref.title
            publisher = ref.publisher

            if len(author) > 15:
                author = author[:11] + "..."
            if len(title) > 15:
                title = title[:11] + "..."
            if len(publisher) > 15:
                publisher = publisher[:11] + "..."

            print(f"Author: {author:15} | Title: {title:15} | Year: {ref.year:4} \
                | Publisher: {publisher:15} | Key: {ref.bib_key} \n"
            )

    def add_ref(self):
        ref_list = self.app.reference_reader.ref_reader()
        self.ref_service.add_reference(ref_list)
