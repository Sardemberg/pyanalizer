import sqlite3
import pathlib

class ProblemDAO:
    def __init__(self):
        self.connection = sqlite3.connect(f"{pathlib.Path().resolve()}/db/banco.sql", isolation_level=None)
        self.cursor = self.connection.cursor()

    def create(self, Problem):
        query = f"insert into problems (description, priority) values ('{Problem.description}', '{Problem.priority}')"
        self.cursor.execute(query)
        print("Insert new problem with status success")

    def delete(self, problem_id):
        query = f"delete from problems where description = '{problem_id}'"
        self.cursor.execute(query)
        print("Delete problem with status success")

    def show_all(self):
        query = f"select * from problems"
        for row in self.cursor.execute(query).fetchall():
            print(f"Description: {row[0]}")
            print(f"Priority: {row[1]}")