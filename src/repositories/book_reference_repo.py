def get_data(connection):
    cursor = connection.cursor()

    data = cursor.execute('''
        select * from bookreference;''').fetchall()

    return data
