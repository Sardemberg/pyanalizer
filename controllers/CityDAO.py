
import pathlib
import sqlite3


class CityDAO:
    def __init__(self):
         self.connection = sqlite3.connect(f"{pathlib.Path().resolve()}/db/banco.db", isolation_level=None)
         self.cursor = self.connection.cursor()

    def create(self, City):
        query = f"insert into cities (name) values ('{City.name}');"
        self.cursor.execute(query)
        print("Insert new city with status success")
    
    def delete(self, city_id ):
        query = f"delete from cities where id = '{city_id}';"
        self.cursor.execute(query)
        print("Delete city with status success")
    
    def add_new_problem(self, city_id):
        query_insert_problem = f"update cities set problems_quantity = problems_quantity + 1 where id = {city_id}"
        query_insert_pending_problem = f"update cities set pending_problems = pending_problems + 1 where id = {city_id}"

        self.cursor.execute(query_insert_problem)
        self.cursor.execute(query_insert_pending_problem)

    def get_city_problems(self):
        query = "select id, name, problems_quantity, pending_problems from cities;"   
        result = self.cursor.execute(query)
        return result.fetchall()
     
    

