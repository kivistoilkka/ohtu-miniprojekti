class BookReference:
    def __init__(self, connection):
        self.connection = connection

    def get_data(self):
        cursor = self.connection.cursor()

        data = cursor.execute("SELECT * FROM bookreferences").fetchall()

        return data

    def add_to_table(self, data: list):
        cursor = self.connection.cursor()

        cursor.execute(
            "INSERT INTO bookreferences (author, title, year, publisher, bib_key, tag)\
            VALUES (?, ?, ?, ?, ?, ?)",
            data
        )
        self.connection.commit()

    def delete_from_table(self, ref_key):
        cursor = self.connection.cursor()

        key = ref_key
        cursor.execute(
            "DELETE FROM bookreferences WHERE bib_key=?", (key,)
        )

        self.connection.commit()

    def ref_to_delete(self, ref_key):
        cursor = self.connection.cursor()

        key = ref_key
        data = cursor.execute(
            "SELECT * FROM bookreferences WHERE bib_key=?", (key,)).fetchone()

        return data
