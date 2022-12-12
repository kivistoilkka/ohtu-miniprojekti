from colorama import Fore
from getkey import getkey
from ui.reference_reader import ReferenceReader
from services.reference_service import ReferenceType

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

            option = getkey()

            if option in options:
                options[option]()
            elif option == "5":
                break

    def create_file(self):
        filename = input("\nMinkä nimisen tiedoston haluat luoda? ")

        data = self.app.get_all_references()

        try:
            self.app.create_bibtex_file(data, filename)
            print(Fore.GREEN + "Tiedosto luotu projektin juurihakemistoon!\n")
        except ValueError as error:
            print(error, "\n")

    def print_instructions(self):
        instructions = ["Luoda tiedosto, paina 1",
                        "Tarkastella luotuja viitteitä, paina 2",
                        "Lisää uusi viite, paina 3",
                        "Poista viite, paina 4",
                        "Sulje ohjelma, paina 5"]

        print(self.text_to_bold(Fore.WHITE + "\nMitä haluat tehdä?"))
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
        tags = self.app.get_tags()

        tag_string = ""
        for tag in tags:
            tag_string += tag + ', '
        tag_string = tag_string[:-2]

        tag_msg = (
            f"Haluatko suodattaa listaa tagin perusteella? Syötä tagi tai jätä tyhjäksi. \n "
            f"Tagit: {tag_string} "
        )

        tag = input(tag_msg)

        order_msg = "\nMillä perusteella haluat järjestää listan? \n"\
                    "Vuosiluvun perusteella, paina 1 \n"\
                    "Lisäysjärjestyksessä, paina 2 \n"

        print(order_msg)

        sorting_key = getkey()

        order_msg = "\nHaluatko listan \nNousevassa järjestyksessä, paina 1 "\
                    "\nLaskevassa järjestyksessä, paina 2 \n"

        print(order_msg)
        order = getkey()
        if tag == "":
            refs = self.app.get_all_references()
        else:
            refs = self.app.filter_by_tag(tag)
        book_data = refs["book_references"]
        web_data = refs["web_references"]
        book_data_sorted = self.sort_data(book_data, sorting_key, order)
        web_data_sorted = self.sort_data(web_data, sorting_key, order)

        title_bar1 = f'{self.text_to_bold("Author")}                    {self.text_to_bold("Title")}                                         {self.text_to_bold("Year")} {self.text_to_bold("Publisher")}                 {self.text_to_bold("Key")}   {self.text_to_bold("Tagi")}'
        title_bar2 = "------------------------- --------------------------------------------- "\
                     "---- ------------------------- ----- ----------"

        print(self.text_to_bold(f"Kirjaviitteet:\n{title_bar1}\n{title_bar2}"))

        for ref in book_data_sorted:
            self.print_book_ref(ref)

        title_bar1 = f'{self.text_to_bold("Author")}                    {self.text_to_bold("Title")}                                         {self.text_to_bold("Year")} {self.text_to_bold("URL")}                       {self.text_to_bold("Key")}   {self.text_to_bold("Tagi")}'
        title_bar2 = "------------------------- --------------------------------------------- "\
                     "---- ------------------------- ----- ----------"

        print(self.text_to_bold(f"Verkkosivuviitteet:\n{title_bar1}\n{title_bar2}"))

        for ref in web_data_sorted:
            self.print_web_ref(ref)

    def add_ref(self):
        print(
            "Haluatko tallentaa kirjaviitteen (paina 1) vai verkkosivuviitteen (paina 2): ")
        answer = getkey()
        if answer == "1":
            ref_list = self.reference_reader.book_ref_reader()
            key = ref_list[4]
            key_used_in_table = self.app.key_used(key)
            if key_used_in_table:
                print(f"Valitsemasi avain on jo käytössä taulussa {key_used_in_table}")
            else:
                self.app.add_reference(ref_list, ReferenceType.Book)
        elif answer == "2":
            ref_list = self.reference_reader.web_ref_reader()
            key = ref_list[4]
            key_used_in_table = self.app.key_used(key)
            if key_used_in_table:
                print(f"Valitsemasi avain on jo käytössä taulussa {key_used_in_table}")
            else:
                self.app.add_reference(ref_list, ReferenceType.Website)

    def del_ref(self):
        key = input("\nAnna avain:")
        try:
            print(self._get_ref_to_delete(key))
        except Exception as error:
            print(error)
            return
        print(Fore.RED + "Haluatko varmasti poistaa viitteen?(kyllä k/en e)\n")
        answer = getkey()
        if answer == "k":
            result = self.app.delete_reference(key)
            if result:
                print(Fore.GREEN + "Viitteen poisto onnistui")
            else:
                print(Fore.RED + "Viitteen poisto ei onnistunut")

    def _get_ref_to_delete(self, bib_key):
        return str(self.app.get_reference(bib_key))

    def text_to_bold(self, text):
        return "\033[1m" + text + "\033[0m"

    def print_book_ref(self, ref):
        author = ref.author
        title = ref.title
        publisher = ref.publisher
        bib_key = ref.bib_key
        tag = ref.tag

        if len(author) > 25:
            author = author[:22] + "..."
        if len(title) > 45:
            title = title[:42] + "..."
        if len(publisher) > 25:
            publisher = publisher[:22] + "..."
        if len(bib_key) > 8:
            bib_key = bib_key[:8] + "..."
        if len(tag) > 15:
            tag = tag[:15] + "..."

        print(f"{author:25} {title:45} {ref.year:4} {publisher:25} {bib_key:7} {tag:10}\n")

    def print_web_ref(self, ref):
        author = ref.author
        title = ref.title
        url = ref.url
        bib_key = ref.bib_key
        tag = ref.tag

        if len(author) > 25:
            author = author[:22] + "..."
        if len(title) > 45:
            title = title[:42] + "..."
        if len(url) > 25:
            url = url[:22] + "..."
        if len(bib_key) > 8:
            bib_key = bib_key[:8] + "..."
        if len(tag) > 15:
            tag = tag[:15] + "..."

        print(f"{author:25} {title:45} {ref.year:4} {url:25} {bib_key:7} {tag:10}\n")
