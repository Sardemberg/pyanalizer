from rq import Queue
from processing.processes import Processes
from controllers.CustomersDAO import CustomersDAO
from redis import Redis

class RQQueues:
    def __init__(self):
        self.redis = Redis(host='localhost', port=6379)
        self.queue_ips = Queue('ips', connection=self.redis)
        self.queue_area = Queue('area', connection=self.redis)
        self.process = Processes()

    def enqueue_ips(self):
        customer_controller = CustomersDAO()
        for customer in customer_controller.get_all():
            self.queue_ips.enqueue(self.process.ips_queue, customer)