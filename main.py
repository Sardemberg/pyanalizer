from controllers.CustomersDAO import CustomersDAO
from processing.processes import Processes
from time import sleep
from utils import menus_principais

customer_controller = CustomersDAO()
process = Processes()
process.enqueue_ips()

while True:
    if(len(customer_controller.get_consumers_errors()) > 0):
        menus_principais.menu_conserto(customer_controller)
    sleep(5)