from queue import Queue
import threading
import time
from core.producer import Producer
from core.consumer import Consumer

# Function to close the program after a certain time (Default 10 seconds)
def close(time_to_shutdown:int,shared_queue:Queue,tc:threading.Thread,tp:threading.Thread):
    time.sleep(time_to_shutdown)
    tc.join(timeout=0)
    tp.join(timeout=0)


# Main process 
if __name__ == "__main__":

    # Create a shared queue using Queue class that is thread safe
    start_time = time.time()
    shared_queue = Queue(maxsize=10)
    producer = Producer(shared_queue,0.1,start_time)
    consumer = Consumer(shared_queue,0.15,start_time)
    tc = threading.Thread(target=producer.produce,daemon=True)
    tp = threading.Thread(target=consumer.consume,daemon=True)

    # Start producer and consumer threads
    tc.start()
    tp.start()

    # Start a thread to close the program after 10 seconds
    close(10,shared_queue,tc,tp)
    


