class App:
    def __init__(self, connection, book_reference_repo, reference_service, db, bibtex_generator):
        self.connection = connection
        self.book_reference_repo = book_reference_repo
        self.db = db
        self.ref_service = reference_service
        self.bibtex_generator = bibtex_generator

    def add_reference(self, ref_list):
        self.ref_service.add_reference(ref_list)

    def get_all_references(self):
        return self.ref_service.get_all_references()

    def create_bibtex_file(self, data, filename):
        self.bibtex_generator.create_bibtex_file(data, filename)

    def delete_reference(self, key):
        self.book_reference_repo.delete_from_table(key)

    def ref_before_delete(self, key):
        self.book_reference_repo.ref_to_delete(key)

    def filter_by_tag(self, tag):
        return self.ref_service.get_references_by_tag(tag)

    def get_tags(self):
        return self.book_reference_repo.get_tags()
