from rq import Queue
from processing.processes import Processes
from controllers.CustomersDAO import CustomersDAO
from redis import Redis

class RQQueues:
    def __init__(self):
        self.redis = Redis(host='localhost', port=6379)
        self.queue = Queue(connection=self.redis)

    def enqueue_ips(self):
        process = Processes()
        customer_controller = CustomersDAO()
        for customer in customer_controller.get_all():
            self.queue.enqueue(process.ips_queue, customer)
