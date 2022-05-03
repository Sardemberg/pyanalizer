
import pathlib
import sqlite3


class CityDAO:
    def __init__(self):
         self.connection = sqlite3.connect(f"{pathlib.Path().resolve()}/db/banco.sql", isolation_level=None)
         self.cursor = self.connection.cursor()

    def create(self, City):
        query = f"insert into cities (name) values ('{City.name}');"
        self.cursor.execute(query)
        print("Insert new city with status success")
    
    def delete(self, city_id ):
        query = f"delete from cities where id = '{city_id}';"
        self.cursor.execute(query)
        print("Delete city with status success")

    def show_all(self):
        query = "select * from cities;"
        for row in self.cursor.execute(query).fetchall():
            print(f'Name: {row}')
      
     
    

