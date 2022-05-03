from controllers.CustomersDAO import CustomersDAO
from models.consumer import Consumer

customer = Consumer(name="Carlos", cellphone=88981994454, ip="192.168.1.1", city_id=1, problem_id=1)
customer_controller = CustomersDAO()

customer_controller.show_all()