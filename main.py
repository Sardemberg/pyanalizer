from controllers.CustomersDAO import CustomersDAO
from processing.processes import Processes
from time import sleep
from utils import menus_principais

customer_controller = CustomersDAO()
# process = Processes()
# process.enqueue_ips()
print(customer_controller.get_problems_errors())