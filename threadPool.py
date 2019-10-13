from concurrent.futures import ThreadPoolExecutor
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


class ThreadPool(Singleton):
    def __init__(self, max_workers=1):
        self.workers = ThreadPoolExecutor(max_workers=max_workers)


thread_pool = ThreadPool(2)
