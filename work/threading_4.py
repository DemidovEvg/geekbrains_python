from threading import Thread
from queue import Queue
import time

class Worker:
    def __init__(self):
        self.input_queue = Queue()

    def send(self, value):
        self.input_queue.put(value)

    def close(self):
        self.input_queue.put(None)
        self.input_queue.join()

    def __call__(self):
        while True:
            item = self.input_queue.get()
            self.input_queue.task_done()
            time.sleep(1)
            if item is None:
                break
            print('Get', item)
        

worker = Worker()
work = Thread(target=worker, daemon=False)
work.start()
worker.send("Simple")
worker.send("Data")
worker.close()
print("Done")