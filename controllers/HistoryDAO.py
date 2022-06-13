from db.connection import Connection
from sqlite3 import Timestamp


class HistoryDAO:
    def create(self, consumer, result_ping):
        connection = Connection()
        query = f"insert into history(consumer_name, status, created_at) values ('{consumer.name}', '{result_ping}', '{Timestamp.now()}');"
        connection.execute(query)
        print("Histórico criado com sucesso")
