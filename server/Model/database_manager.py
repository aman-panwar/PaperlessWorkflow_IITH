""" experimental file to make a singleton resource manager class to handle
    database client"""

from queue import Queue
from threading import Lock
from pymongo import MongoClient

class SingletonMetaClass(type):
    my_instances = {}
    thread_lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls.thread_lock:
            if cls not in cls.my_instances:
                inst = super().__call__(*args, **kwargs)
                cls.my_instances[cls] = inst
        return cls.my_instances[cls]

class DbManager(metaclass = SingletonMetaClass):
    class ClientWrapper:
        def __init__(self, client) -> None:
            self.client = client
        def __enter__(self):
            return self.client
        def __exit__(self, a, b, c):
            DbManager().return_client(self.client)
        def __call__(self, *args, **kwds):
            return self.client

    def __init__(self) -> None:
        self.max_size = 10
        self.clientQ = Queue(maxsize= self.max_size)
        self.host = 'mongodb+srv://cs20btech11004:Y1JDdwqWBLgOWp2g@cluster0.iz8c5af.mongodb.net/?retryWrites=true&w=majority'
        for _ in range(self.max_size):
            self.clientQ.put(MongoClient(self.host))
        self.lock = Lock()
    def get_client(self):
        while self.clientQ.empty():
            continue
        with self.lock:
            return self.ClientWrapper(self.clientQ.get())
    def return_client(self, c):
        if self.clientQ.full()==False:
            with self.lock:
                self.clientQ.put(c)