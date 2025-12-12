# import sqlite3

# class Database:
#     def __init__(self, path="data.db"):
#         self.conn = sqlite3.connect(path)
#         self.cursor = self.conn.cursor()
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS tests(
#                 code TEXT PRIMARY KEY,
#                 answers TEXT
#             )
#         """)
#         self.conn.commit()

#     def save_test(self, code, answers):
#         self.cursor.execute("REPLACE INTO tests(code, answers) VALUES(?, ?)", (code, answers))
#         self.conn.commit()

#     def get_answers(self, code):
#         self.cursor.execute("SELECT answers FROM tests WHERE code = ?", (code,))
#         row = self.cursor.fetchone()
#         return row[0] if row else None


# === database.py ===

import sqlite3

class Database:
    def __init__(self, path="data.db"):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tests(
                code TEXT PRIMARY KEY,
                answers TEXT
            )
        """)
        self.conn.commit()

    def save_test(self, code, answers):
        self.cursor.execute("REPLACE INTO tests(code, answers) VALUES(?, ?)", (code, answers))
        self.conn.commit()

    def get_answers(self, code):
        self.cursor.execute("SELECT answers FROM tests WHERE code = ?", (code,))
        row = self.cursor.fetchone()
        return row[0] if row else None
