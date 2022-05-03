from models.consumer import Consumer
from controllers.CustomersDAO import CustomersDAO

controller_customer = CustomersDAO()
consumer = Consumer(name="Carlos", cellphone=88981994454, ip="192.168.1.1", city_id=1, problem_id=1)

controller_customer.show_all()