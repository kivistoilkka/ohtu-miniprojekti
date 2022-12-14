from services.reference_service import ReferenceType


class App:
    def __init__(self, connection, reference_service, db, bibtex_generator):
        self.connection = connection
        self.reference_service = reference_service
        self.db = db
        self.bibtex_generator = bibtex_generator

    def add_reference(self, ref_list, ref_type):
        self.reference_service.add_reference(ref_list, ref_type)

    def get_all_references(self):
        return self.reference_service.get_all_references()

    def create_bibtex_file(self, data, filename):
        self.bibtex_generator.create_bibtex_file(data, filename)

    def delete_reference(self, bib_key):
        data = self.key_used(bib_key)
        if data:
            if data == "bookreference":
                return self.reference_service.delete_reference(bib_key, ReferenceType.Book)
            if data == "webreference":
                return self.reference_service.delete_reference(bib_key, ReferenceType.Website)
            raise ValueError("Virhe viitteen taulun tiedossa")
        raise ValueError("Viitettä ei löytynyt")

    def key_used(self, bib_key) -> str:
        data = self.db.key_used(bib_key)
        if data:
            return data[0]
        return None

    def filter_by_tag(self, tag):
        return self.reference_service.get_references_by_tag(tag)

    def get_tags(self):
        data = self.db.get_used_tags_from_database()
        tags = []

        for tag in data:
            if tag[0] != "":
                tags.append(tag[0])

        return tags

    def get_reference(self, bib_key):
        data = self.key_used(bib_key)
        if not data:
            raise ValueError("Viitettä ei löytynyt")

        if data == "bookreference":
            return self.reference_service.get_reference(bib_key, ReferenceType.Book)
        if data == "webreference":
            return self.reference_service.get_reference(bib_key, ReferenceType.Website)
        raise ValueError("Virhe viitteen taulun tiedossa")
