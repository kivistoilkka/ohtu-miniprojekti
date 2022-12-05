from ui.reference_reader import ReferenceReader

class UI:
    def __init__(self, app):
        self.app = app
        self.reference_reader = ReferenceReader()

    def run(self):
        while True:
            options = int(input(
                "Mitä haluat tehdä?\n\
Luoda tiedosto, paina 1\n\
Tarkastella luotuja viitteitä, paina 2\n\
Lisää uusi viite, paina 3 \n\
Poista viite, paina 4 \n\
Sulje ohjelma, paina 5\n"
            ))

            if options == 1:
                self.create_file()

            elif options == 2:
                self.view_ref()

            elif options == 3:
                self.add_ref()

            elif options == 4:
                self.del_ref()

            elif options == 5:
                break

    def create_file(self):
        filename = input("Minkä nimisen tiedoston haluat luoda? ")

        data = self.app.get_all_references()

        try:
            self.app.create_bibtex_file(data, filename)
            print("Tiedosto luotu!")
        except Exception as e:
            print(e + "\n")

    # def create_database(self):
    #     selection = input("Haluatko luoda uuden tietokannan (kyllä/ei)? ")
    #     if selection == "kyllä":
    #         self.app.db.create_tables(self.app.connection)

    def view_ref(self):

        data = self.app.get_all_references()

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
        ref_list = self.reference_reader.ref_reader()
        self.app.add_reference(ref_list)

    def del_ref(self):
        
        answer = input("Haluatko varmasti poistaa viitteen?(kyllä/en) ")
        if answer == "kyllä":
            self.app.delete_reference()
        