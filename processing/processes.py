from controllers.CustomersDAO import CustomersDAO
from controllers.CityDAO import CityDAO
from controllers.HistoryDAO import HistoryDAO
from models.consumer import Consumer
from random import randint
import subprocess
from celery_queues import app

class Processes:
    def __init__(self):
        self.consumers_with_problem = []

    def enqueue_ips(self):
        customer_controller = CustomersDAO()
        for customer in customer_controller.get_all():
            self.send_ping.delay(customer)

    @app.task(name='send_ping', bind=True)
    def send_ping(self, consumer):
        customer_controller = CustomersDAO()
        city_controller = CityDAO()
        history_controller = HistoryDAO()

        output_shell = subprocess.Popen(f"ping -w 5 {consumer[3]} && echo 'POSITIVE' || echo 'NEGATIVE'", stdout=subprocess.PIPE, shell=True)
        result_ping = output_shell.communicate()[0].split(b'\n')[-2].decode("utf-8")

        if(result_ping == 'NEGATIVE'):
            consumer = Consumer(id=consumer[0], name=consumer[1], cellphone=consumer[2], ip=consumer[3], city_id=consumer[4], problem_id=randint(1, 5))
            customer_controller.update(consumer)
            history_controller.create(consumer=consumer, result_ping=result_ping)
            city_controller.add_new_problem(consumer.city_id)
        else:
            consumer = Consumer(id=consumer[0], name=consumer[1], cellphone=consumer[2], ip=consumer[3], city_id=consumer[4], problem_id=0)
            history_controller.create(consumer=consumer, result_ping=result_ping)
            customer_controller.update(consumer)

    def messages_queue():
        pass
