from concurrent.futures import ThreadPoolExecutor
from singleton import Singleton


class ThreadPool(Singleton):
    def __init__(self, max_workers=1):
        self.workers = ThreadPoolExecutor(max_workers=max_workers)


thread_pool = ThreadPool(2)
