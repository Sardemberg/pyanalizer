from processing.processes import Processes
from processing.rq import TestingRq

testing = TestingRq()
testing.enqueue_all()