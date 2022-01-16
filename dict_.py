import threading

class SafeDict(dict):

    def __init__(self, *args, **kwargs):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()
        super().__init__(*args, **kwargs)
    
    def __getitem__(self, item):
        self.consumer_lock.acquire()
        value = super().__getitem__(item)
        self.producer_lock.release()
        return value

    def __setitem__(self, item, value):
        self.producer_lock.acquire()
        super().__setitem__(item, value)
        self.consumer_lock.release()


d = SafeDict()
d[1] = 100
print(d[1])
pass