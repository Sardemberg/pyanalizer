from controllers.CustomersDAO import CustomersDAO
from processing.processes import Processes
from time import sleep
from utils import menus_principais

customer_controller = CustomersDAO()
# process = Processes()
# process.enqueue_ips()

# CustomersDAO.solve_problem(5)

print(customer_controller.get_consumers_errors())
# print(customer_controller.get_problems_errors())