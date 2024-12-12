from queue import Queue
import threading
import time
import random

class Consumer:
    """
    Class to consume items from a safe thread shared queue 
    consume: Method to consume items from the queue at a given interval
    """
    def __init__(self, queue:Queue, interval,start_time:float):
        self.queue = queue
        self.interval = interval
        self.start_time = start_time

    def consume(self):
        while True:
            time.sleep(self.interval)
            item = self.queue.get()
            print(f"Consumed {item} Time: {round((time.time() - self.start_time),2)}")
