from random import randint
from db.connection import Connection
db = Connection()

def create_new_user(name, ip):
    query = f"insert into customers (name, cellphone, ip, city_id, problem_id) values ('{name}','88981994454','{ip}','{randint(1, 4)}','{randint(1, 4)}')"
    db.execute(query)

def create_new_problem(description, message):
    query = f"insert into problems(description, priority, message) values ('{description}', 1, '{message}')"
    db.execute(query)

def create_new_city(name):
    query = f"insert into cities (name) values ('{name}')"
    db.execute(query)