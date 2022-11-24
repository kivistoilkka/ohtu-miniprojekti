class App:
    def __init__(self, connection, book_reference_repo, db):
        self.connection = connection
        self.book_reference_repo = book_reference_repo
        self.db = db

    def run(self):
        data = self.book_reference_repo.get_data(self.connection)

        selection = input("Haluatko luoda uuden tietokannan (kyllä/ei) ?")
        if selection == "kyllä":
            self.db.create_tables(self.connection)
        print(data)