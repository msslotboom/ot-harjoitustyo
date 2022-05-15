from db_connection import get_database_connection


def drop_tables(connection):
    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists highscores;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table highscores (
            name text primary key,
            level text,
            score number
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == "main":
    initialize_database()
