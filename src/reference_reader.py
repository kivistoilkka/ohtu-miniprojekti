
class ReferenceReader:
    def __init__(self):
        pass

    def ref_reader(self):
        author = input("Author:")
        title = input("Title:")
        year = int(input("Year:"))
        publisher = input("Publisher:")
        bib_key = input("Key:")

        reference_list = [author,title,year,publisher,bib_key]

        return reference_list

