class BookReference:
    def __init__(self, connection):
        self.connection = connection

    def get_data(self):
        cursor = self.connection.cursor()

        data = cursor.execute("SELECT * FROM bookreferences").fetchall()

        return data


    def add_to_table(self, data:list):
        cursor = self.connection.cursor()

        cursor.execute(
            "INSERT INTO bookreferences (author, title, year, publisher, bib_key)\
            VALUES (?, ?, ?, ?, ?)",
            data
        )
        self.connection.commit()
    
    def delete_from_table(self):
        cursor = self.connection.cursor()

        cursor.execute(
            "DELETE FROM bookreferences WHERE id=2"
        )

        self.connection.commit()
