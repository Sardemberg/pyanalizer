from db.connection import Connection
import json

class CustomersDAO:
    def create(self, Customers):
        db = Connection()
        query = f"insert into customers (name, cellphone, ip, city_id, problem_id) values ('{Customers.name}','{Customers.cellphone}','{Customers.ip}','{Customers.city_id}','{Customers.problem_id}')"
        db.execute(query)
        print("Insert new customer with status success")

    def delete(self, customers_id):
        db = Connection()
        query = f"delete from customers where id = '{customers_id}'"
        db.execute(query)
        print("Delete customer with status success")

    def execute(self, query):
        db = Connection()
        result_data = db.execute(query).fetchall()
        return result_data

    def update(self, customer):
        db = Connection()
        query = f"update customers set name='{customer.name}', cellphone={customer.cellphone}, ip='{customer.ip}', city_id={customer.city_id}, problem_id={customer.problem_id} where id = {customer.id};"
        db.execute(query)
        print("Dado atualizado com sucesso")

    def get_all(self):
        db = Connection()
        query = "select * from customers"
        return db.select(query).fetchall()

    def get_consumers_errors(self):
        db = Connection()
        query = "select customers.name, customers.ip, cities.name, problems.description from customers inner join problems on customers.problem_id = problems.id inner join cities on customers.city_id = cities.id where problem_id is not 0;"
        response = db.select(query)
        return response.fetchall()
        
