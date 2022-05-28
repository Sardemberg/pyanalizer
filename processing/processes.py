from controllers.CustomersDAO import CustomersDAO
from models.consumer import Consumer
import subprocess

class Processes:
    def ips_queue(*args):
        output_shell = subprocess.Popen(f"ping -w 5 {args[1][3]} && echo 'POSITIVE' || echo 'NEGATIVE'", stdout=subprocess.PIPE, shell=True)
        result_ping = output_shell.communicate()[0].split(b'\n')[-2].decode("utf-8")
        customer_controller = CustomersDAO()
        
        if(result_ping == 'NEGATIVE'):
            consumer = Consumer(id=args[1][0], name=args[1][1], cellphone=args[1][2], ip=args[1][3], city_id=args[1][4], problem_id=1)
            customer_controller.update(consumer)
        else:
            consumer = Consumer(id=args[1][0], name=args[1][1], cellphone=args[1][2], ip=args[1][3], city_id=args[1][4], problem_id=0)
            customer_controller.update(consumer)

    def messages_queue():
        pass

    def area_analisys(self, customer):
        customers_area = self.customer_controller.execute(f"select * from customers where city_id = {customer[4]}")