from ui.reference_reader import ReferenceReader

class UI:
    def __init__(self, app):
        self.app = app
        self.reference_reader = ReferenceReader()

    def run(self):
        while True:
            self.print_instructions()

            options = {"1": self.create_file, "2": self.view_ref, "3": self.add_ref, "4": self.del_ref}

            option = input()

            if option in options.keys():
                options[option]()
            elif option == "5":
                break

    def create_file(self):
        filename = input("Minkä nimisen tiedoston haluat luoda? ")

        data = self.app.get_all_references()

        try:
            self.app.create_bibtex_file(data, filename)
            print("Tiedosto luotu!")
        except Exception as e:
            print(e + "\n")

    def print_instructions(self):
        instructions = ["Mitä haluat tehdä?",
                        "Luoda tiedosto, paina 1",
                        "Tarkastella luotuja viitteitä, paina 2",
                        "Lisää uusi viite, paina 3",
                        "Poista viite, paina 4",
                        "Sulje ohjelma, paina 5"]

        for instruction in instructions:
            print(instruction)

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
        key = input("Anna avain:")

        self.ref_to_delete(key)
        
        answer = input("Haluatko varmasti poistaa viitteen?(kyllä/en) ")

        if answer == "kyllä":
            self.app.delete_reference(key)
    

    def ref_to_delete(self, key):

        data = self.app.get_all_references()
        #print(data)

        
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
            
            if key == ref.bib_key:


                print(f"Author: {author:15} | Title: {title:15} | Year: {ref.year:4} \
                    | Publisher: {publisher:15} | Key: {ref.bib_key} \n"
                )
        