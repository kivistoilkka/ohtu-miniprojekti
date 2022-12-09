class BookReferenceRepo:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_data(self):
        data = self.cursor.execute("SELECT * FROM bookreferences").fetchall()

        return data

    def add_to_table(self, data: list):
        self.cursor.execute(
            "INSERT INTO bookreferences (author, title, year, publisher, bib_key, tag)\
            VALUES (?, ?, ?, ?, ?, ?)",
            data
        )

        self.connection.commit()

    def delete_from_table(self, key):
        self.cursor.execute(
            "DELETE FROM bookreferences WHERE bib_key=?", (key,)
        )

        self.connection.commit()

    def get_reference(self, ref_key):
        data = self.cursor.execute(
            "SELECT * FROM bookreferences WHERE bib_key=?", (ref_key,)).fetchone()

        return data

    def get_data_by_tag(self, tag):
        cursor = self.connection.cursor()
        data = cursor.execute(
            "SELECT * FROM bookreferences WHERE tag=?", (tag,)).fetchall()

        return data

    def get_tags(self):
        cursor = self.connection.cursor()
        data = cursor.execute(
            "SELECT tag FROM bookreferences").fetchall()

        return set(data)
