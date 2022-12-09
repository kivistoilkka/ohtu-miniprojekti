class BookReferenceRepo:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_data(self):
        data = self.cursor.execute("SELECT * FROM bookreferences").fetchall()

        return data

    def add_to_table(self, data: list):
        self.cursor.execute(
            "INSERT INTO bookreferences (author, title, year, publisher, bib_key)\
            VALUES (?, ?, ?, ?, ?)",
            data
        )

        self.connection.commit()

    def delete_from_table(self, ref_key):
        self.cursor.execute(
            "DELETE FROM bookreferences WHERE bib_key=?", (ref_key,)
        )

        self.connection.commit()

    def get_reference(self, ref_key):
        data = self.cursor.execute(
            "SELECT * FROM bookreferences WHERE bib_key=?", (ref_key,)).fetchone()

        return data
