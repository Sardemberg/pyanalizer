

# from concurrent.futures import process
# from processing.processes import Processes

# process = Processes()
# process.execute()

from ui.chart import ShowChart

chart = ShowChart()
chart.show()

from processing.rq_queues import RQQueues
from controllers.CustomersDAO import CustomersDAO

customer_controller = CustomersDAO()
print(customer_controller.get_all())

queue = RQQueues()
queue.enqueue_ips()

