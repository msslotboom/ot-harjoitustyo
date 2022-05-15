from db_connection import get_database_connection
import highscores.initialise_database
class Highscores:
    def __init__(self, level) -> None:
        self.connection = get_database_connection()
        self.level = level
        highscores.initialise_database.initialize_database()
    def find_top(self, limit):
        cursor = self.connection.cursor()

        cursor.execute("select * from highscores")
        rows = cursor.fetchall()
        return rows

    def add_score(self, name, score):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO highscores (name, level, score) VALUES (?,?, ?)", [name, self.level, score])
        self.connection.commit()
    # def _check_table(self):
    #     """Checks whether table exists and if not creates one
    #     """
    #     cursor = self.connection.cursor()
    #     cursor.execute('''
    #     create table ? (
    #         name text primary key,
    #         score number
    #     );
    #     ''',[self.level])
        
        # table_exists = cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?",[self.level]).fetchone()
        # print(table_exists)
        # if table_exists is None:
        #     print("check")
        #     create_tables(self.level)
            