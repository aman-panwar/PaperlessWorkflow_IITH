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
    """An thread safe singleton object pool class for MongoClient.client

    Intended use:\n
    with DbManager().get_client() as c:
        c.get_database('example)\n
        ... 
    """
    class ClientWrapper:
        """a context managing class. sole purpose of this class is to allow DbManager.get_client() to be used in a 'with' statement"""
        def __init__(self, client) -> None:
            self.client = client
        def __enter__(self):
            return self.client
        def __exit__(self, a, b, c):
            DbManager().return_client(self.client)
        def __call__(self, *args, **kwds):
            return self.client

    def __init__(self) -> None:
        self.max_size = 10 #total number of clients
        self.clientQ = Queue(maxsize= self.max_size) #saves the clients available for use
        self.host = 'mongodb+srv://cs20btech11004:Y1JDdwqWBLgOWp2g@cluster0.iz8c5af.mongodb.net/?retryWrites=true&w=majority'
        for _ in range(self.max_size):
            self.clientQ.put(MongoClient(self.host))
        self.lock = Lock()
    def get_client(self):
        """returns a client wrapper object containing the MongoClient

        Returns:
            a ClientWrapper obj.

        to get MongoClient obj\n
        client =  ClientWrapper() or client = ClientWrapper().client
        """
        while self.clientQ.empty():
            continue
        with self.lock:
            return self.ClientWrapper(self.clientQ.get())
    def return_client(self, client):
        """saves the client back into the DbManager"""
        if self.clientQ.full()==False:
            with self.lock:
                self.clientQ.put(client)


#############################
#       intended use        #
#############################
# with DbManager().get_client() as c:
#     db = c.get_database('PaperlessWorkflow')
#     coll = db.get_collection('Forms')
#     for x in coll.find({"_id":"643ff5dd326f4d6638bea447"}):
#         print(x)