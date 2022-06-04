from processing.rq_queues import RQQueues
from controllers.CustomersDAO import CustomersDAO
from time import sleep
from utils import menus_principais

customer_controller = CustomersDAO()

queue = RQQueues()
queue.enqueue_ips()

while True:
    if(len(customer_controller.get_consumers_errors()) > 0):
        menus_principais.menu_conserto(customer_controller)
    sleep(5)
