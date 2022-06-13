from db.connection import Connection
from sqlite3 import Timestamp
from datetime import date
import pathlib

class HistoryDAO:
    def create(self, consumer, result_ping):
        connection = Connection()
        query = f"insert into history(consumer_name, status, created_at) values ('{consumer.name}', '{result_ping}', '{Timestamp.now()}');"
        connection.execute(query)
        print("Histórico criado com sucesso")

    def build_file(self):
        atual_date = date.today().isoformat()
        query_history = f"select * from history where status = 'NEGATIVE' and DATE(created_at) = '{atual_date}';"
        db = Connection()
        result_database = db.select(query_history).fetchall()
        lines = []

        for result in result_database:
            lines.append(f"{result[1]} - {result[2]}\n")

        file = open(f"{pathlib.Path().resolve()}/history/{atual_date}.txt", "w")
        file.write(f"Usuários com problema no dia: {atual_date}\n\n")
        file.writelines(lines)
        file.close()

