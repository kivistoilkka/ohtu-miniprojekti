class App:
    def __init__(self, connection, book_reference_repo, db, reference_reader):
        self.connection = connection
        self.book_reference_repo = book_reference_repo
        self.db = db
        self.reference_reader = reference_reader
