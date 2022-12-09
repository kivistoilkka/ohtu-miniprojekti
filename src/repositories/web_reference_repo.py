class WebReferenceRepo:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_data(self):
        data = self.cursor.execute("SELECT * FROM webreferences").fetchall()

        return data

    def add_to_table(self, data: list):
        self.cursor.execute(
            "INSERT INTO webreferences (author, title, year, url, bib_key, tag)\
            VALUES (?, ?, ?, ?, ?, ?)", data
        )

        self.connection.commit()

    def delete_from_table(self, ref_key):
        self.cursor.execute(
            "DELETE FROM webreferences WHERE bib_key=?", (ref_key,)
        )

        self.connection.commit()

    def get_reference(self, ref_key):
        data = self.cursor.execute(
            "SELECT * FROM webreferences WHERE bib_key=?", (ref_key,)).fetchone()

        return data

    def get_data_by_tag(self, tag):
        cursor = self.connection.cursor()
        data = cursor.execute(
            "SELECT * FROM webreferences WHERE tag=?", (tag,)).fetchall()

        return data

    def get_tags(self):
        cursor = self.connection.cursor()
        data = cursor.execute(
            "SELECT tag FROM webreferences").fetchall()

        return set(data)
