from multiprocessing import Process
from controllers.CustomersDAO import CustomersDAO
import subprocess
from time import sleep

class Processes:
    def __init__(self):
        self.customer_controller = CustomersDAO()
        self.subqueue_ips = []
        self.should_enqueue_ips = True
        self.should_enqueue_messages = True

    # Public
    def execute(self):
        while True:
            customers = self.customer_controller.get_all()
            for customer in customers:
                if self.should_enqueue_ips:
                    self.subqueue_ips.append(customer)
                    Process(target=self.ips_queue()).start()

                    if len(self.subqueue_ips) == 10:
                        self.should_enqueue_ips = False
                    else:
                        self.should_enqueue_ips = True
                else:
                    while(self.should_enqueue_ips == False):
                        sleep(5)
                        if len(self.subqueue_ips) < 10:
                            self.should_enqueue_ips = True
                            self.subqueue_ips.append(customer)
                            Process(target=self.ips_queue()).start()

    # Private
    def ips_queue(self):
        customer = self.subqueue_ips.pop()
        output_shell = subprocess.Popen(f"ping -w 5 {customer[3]} && echo 'POSITIVE' || echo 'NEGATIVE'", stdout=subprocess.PIPE, shell=True)
        print(output_shell.communicate()[0].split(b'\n')[-2], customer[1])

    def messages_queue():
        pass
