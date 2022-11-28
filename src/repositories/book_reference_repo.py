from reference_reader import ReferenceReader

class BookReference:
    def get_data(self, connection):
        cursor = connection.cursor()

        data = cursor.execute("SELECT * FROM bookreferences").fetchall()

        return data


    def add_to_table(self, connection, list):
        cursor = connection.cursor()

        cursor.execute("INSERT INTO bookreferences (author, title, year, publisher, bib_key) VALUES (?, ?, ?, ?, ?)", list)
        connection.commit()


