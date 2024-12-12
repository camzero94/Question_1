from queue import Queue
import threading
import time
import random

class Producer:
    """
    Class to produce items to a safe thread shared queue 
    produce: Method to consume items from the queue at a given interval
    """

    def __init__(self, queue:Queue,interval,start_time:float):
        self.queue = queue
        self.interval = interval
        self.start_time = start_time

    def produce(self):
        while True:
            time.sleep(self.interval)
            my_random = random.randint(0, 1000)
            self.queue.put(my_random)
            print(f"Produced {my_random} Time: {round((time.time() - self.start_time),2)}")
