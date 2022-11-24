from reference_reader import ReferenceReader

class BookReference:
    def get_data(connection):
        cursor = connection.cursor()

        data = cursor.execute('''
            select * from bookreference;''').fetchall()

        return data


    def add_to_table(connection):
        cursor = connection.cursor()

        cursor.execute("INSERT INTO bookreference (author, title, year, publisher, bib_key) VALUES (?, ?, ?, ?, ?)", ReferenceReader.ref_reader())


