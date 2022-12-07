from ui.reference_reader import ReferenceReader


class UI:
    def __init__(self, app):
        self.app = app
        self.reference_reader = ReferenceReader()

    def run(self):
        while True:
            self.print_instructions()

            options = {
                "1": self.create_file, "2": self.view_ref,
                "3": self.add_ref, "4": self.del_ref
            }

            option = input()

            if option in options:
                options[option]()
            elif option == "5":
                break

    def create_file(self):
        filename = input("\nMinkä nimisen tiedoston haluat luoda? ")

        data = self.app.get_all_references()

        try:
            self.app.create_bibtex_file(data, filename)
            print("Tiedosto luotu!")
        except ValueError as error:
            print(error, "\n")

    def print_instructions(self):
        instructions = ["Luoda tiedosto, paina 1",
                        "Tarkastella luotuja viitteitä, paina 2",
                        "Lisää uusi viite, paina 3",
                        "Poista viite, paina 4",
                        "Sulje ohjelma, paina 5"]

        print(self.text_to_bold("Mitä haluat tehdä?"))
        for instruction in instructions:
            print("\n" + instruction)


    def sort_data(self, data, sorting_key, order):
        if sorting_key == "1":
            if order == "1":
                data.sort(key=lambda ref: ref.year, reverse=False)
            if order == "2":
                data.sort(key=lambda ref: ref.year, reverse=True)

        elif sorting_key == "2":
            if order == "2":
                data.reverse()
        return data

    def view_ref(self):
        sorting_key = input(
            "\nMillä perusteella haluat järjestää listan? \nVuosiluvun perusteella, paina 1 \nLisäysjärjestyksessä, paina 2 \n")
        order = input(
            "\nHaluatko listan \nNousevassa järjestyksessä, paina 1 \nLaskevassa järjestyksessä, paina 2 \n")

        data = self.app.get_all_references()
        data = self.sort_data(data, sorting_key, order)

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

            print(f"\nAuthor: {author:15} | Title: {title:15} | Year: {ref.year:4} \
                | Publisher: {publisher:15} | Key: {ref.bib_key} \n"
                  )

    def add_ref(self):
        ref_list = self.reference_reader.ref_reader()
        self.app.add_reference(ref_list)

    def del_ref(self):
        key = input("\nAnna avain:")

        self.ref_to_delete(key)

        answer = input("Haluatko varmasti poistaa viitteen?(kyllä/en)\n")

        if answer == "kyllä":
            self.app.delete_reference(key)

    def ref_to_delete(self, key):

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

            if key == ref.bib_key:
                print(f"\nAuthor: {author:15} | Title: {title:15} | Year: {ref.year:4} \
                    | Publisher: {publisher:15} | Key: {ref.bib_key} \n"
                      )

    def text_to_bold(self, text):
        return "\033[1m" + text + "\033[0m"
