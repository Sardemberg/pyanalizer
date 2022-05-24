import pathlib
import sqlite3
import json

class Connection:
    def __init__(self):
         self.connection = None
         self.cursor = None

    def execute(self, query):
        self.start_connection()
        self.cursor.execute(query)
        self.connection.commit()
        self.close_connection()

    def select(self, query):
        self.start_connection()
        return self.cursor.execute(query)

    def start_connection(self):
        self.connection = sqlite3.connect("/home/sardemberg/pyanalizer/db/banco.db")
        self.cursor = self.connection.cursor()
    
    def close_connection(self):
        self.connection.close()