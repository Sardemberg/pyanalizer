import pathlib
import sqlite3
class CustomersDAO:
    def __init__(self):
         self.connection = sqlite3.connect(f"{pathlib.Path().resolve()}/db/banco.sql", isolation_level=None)
         self.cursor = self.connection.cursor()

    def create(self, Customers):
        query = f"insert into customers (name, cellphone, ip, city_id, problem_id) values ('{Customers.name}','{Customers.cellphone}','{Customers.ip}','{Customers.city_id}','{Customers.problem_id}')"
        self.cursor.execute(query)
        print("Insert new customer with status success")
    
    def delete(self, customers_id ):
        query = f"delete from customers where id = '{customers_id}'"
        self.cursor.execute(query)
        print("Delete customer with status success")

    def get_all(self):
        query = "select * from customers"
        return self.cursor.execute(query).fetchall()
      
     
    

