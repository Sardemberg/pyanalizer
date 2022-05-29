from rq import Queue, Worker
from processing.processes import Processes
from controllers.CustomersDAO import CustomersDAO
from redis import Redis
from time import sleep

class RQQueues:
    def __init__(self):
        self.redis = Redis(host='localhost', port=6379)
        self.queue_ips = Queue('ips', connection=self.redis)
        self.queue_area = Queue('area', connection=self.redis)
        self.ip_worker = Worker([self.queue_ips], connection=self.redis, name='ips_worker')
        self.area_worker = Worker([self.queue_area], connection=self.redis, name='area_worker')
        self.process = Processes()

    def enqueue_ips(self):
        customer_controller = CustomersDAO()
        for customer in customer_controller.get_all():
            self.queue_ips.enqueue(self.process.ips_queue, customer)