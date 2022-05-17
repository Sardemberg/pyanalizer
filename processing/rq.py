from rq import Queue
from redis import Redis
from controllers.CustomersDAO import CustomersDAO
import subprocess

class TestingRq:
    def __init__(self):
        self.queue_ips = Queue(name="ips", connection=Redis())
        self.customer_controller = CustomersDAO()

    def enqueue_all(self):
        data_prepared = []
        for customer in self.customer_controller.get_all():
            data_prepared.append(Queue.prepare_data(self.send_ping, customer, job_id=f"{customer[0]}"))
        self.queue_ips.enqueue_many(data_prepared)

    def send_ping(customer):
        output_shell = subprocess.Popen(f"ping -w 5 {customer[3]} && echo 'POSITIVE' || echo 'NEGATIVE'", stdout=subprocess.PIPE, shell=True)
        print(output_shell.communicate()[0].split(b'\n')[-2], customer[1])