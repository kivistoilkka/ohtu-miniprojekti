
class ReferenceReader:

    def ref_reader(self):
        author = input("Author: ")
        title = input("Title: ")
        year = input("Year: ")
        publisher = input("Publisher: ")
        bib_key = input("Key: ")
        tag = input("Tägi (voi jättää tyhjäksi): ")

        reference_list = [author, title, year, publisher, bib_key, tag]

        return reference_list
