
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
        query = f"select problems_quantity from cities where id = {city_id};"
        problems_quantity = self.cursor.execute(query).fetchone()
        if problems_quantity[0] == None: 
            problems_quantity = 1
        else:
            problems_quantity = problems_quantity[0] + 1
            print("Atualização:", problems_quantity)
        query_insert_new_problem = f"update cities set problems_quantity = {problems_quantity} where id = {city_id};"
        self.cursor.execute(query_insert_new_problem)
        print("Dado atualizado com sucesso")

    def show_all(self):
        query = "select * from cities;"
        for row in self.cursor.execute(query).fetchall():
            print(f'Name: {row}')
      
     
    

