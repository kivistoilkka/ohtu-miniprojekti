class App:
    def __init__(self, connection, book_reference_repo, db, reference_reader):
        self.connection = connection
        self.book_reference_repo = book_reference_repo
        self.db = db
        self.reference_reader = reference_reader

    def run(self):
        selection = input("Haluatko luoda uuden tietokannan (kyllä/ei)? ")
        if selection == "kyllä":
            self.db.create_tables(self.connection)
        
        ref_list = self.reference_reader.ref_reader()

        self.book_reference_repo.add_to_table(self.connection,ref_list)

        data = self.book_reference_repo.get_data(self.connection)
        print(data)