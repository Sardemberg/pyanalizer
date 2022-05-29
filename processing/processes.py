from controllers.CustomersDAO import CustomersDAO
from controllers.CityDAO import CityDAO
from models.consumer import Consumer
import subprocess

class Processes:
    def __init__(self):
        self.consumers_with_problem = []

    def ips_queue(self, *args):
        print(args)
        output_shell = subprocess.Popen(f"ping -w 5 {args[0][3]} && echo 'POSITIVE' || echo 'NEGATIVE'", stdout=subprocess.PIPE, shell=True)
        result_ping = output_shell.communicate()[0].split(b'\n')[-2].decode("utf-8")
        customer_controller = CustomersDAO()

        if(result_ping == 'NEGATIVE'):
            consumer = Consumer(id=args[0][0], name=args[0][1], cellphone=args[0][2], ip=args[0][3], city_id=args[0][4], problem_id=1)
            customer_controller.update(consumer)
            self.area_analisys(consumer)
        else:
            consumer = Consumer(id=args[0][0], name=args[0][1], cellphone=args[0][2], ip=args[0][3], city_id=args[0][4], problem_id=0)
            customer_controller.update(consumer)

    def messages_queue():
        pass

    def area_analisys(self, customer):
        city_controller = CityDAO()
        city_controller.add_new_problem(customer.city_id)