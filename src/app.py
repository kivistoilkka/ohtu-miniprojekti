class App:
    def __init__(self, connection, book_reference_repo, book_ref_service,
                 web_reference_repo, web_ref_service, db, bibtex_generator):
        self.connection = connection
        self.book_reference_repo = book_reference_repo
        self.book_ref_service = book_ref_service
        self.web_reference_repo = web_reference_repo
        self.web_ref_service = web_ref_service
        self.db = db
        self.bibtex_generator = bibtex_generator

    def add_book_reference(self, ref_list):
        self.book_ref_service.add_reference(ref_list)

    def add_web_reference(self, ref_list):
        self.web_ref_service.add_reference(ref_list)

    def get_all_book_references(self):
        return self.book_ref_service.get_all_references()

    def get_all_web_references(self):
        return self.web_ref_service.get_all_references()

    def get_all_references(self):
        return self.get_all_book_references() + self.get_all_web_references()

    def create_bibtex_file(self, data, filename):
        self.bibtex_generator.create_bibtex_file(data, filename)

    def delete_book_reference(self, key):
        self.book_reference_repo.delete_from_table(key)

    def delete_web_reference(self, key):
        self.web_reference_repo.delete_from_table(key)

    def get_book_ref_with_key(self, key):
        self.book_reference_repo.get_book_ref_with_key(key)

    def get_web_ref_with_key(self, key):
        self.web_reference_repo.get_book_ref_with_key(key)
