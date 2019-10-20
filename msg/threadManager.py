from concurrent.futures import ThreadPoolExecutor

class ThreadManager:
    def __init__(self, max_workers=10):
        if not isinstance(max_workers, (int)):
            raise AttributeError('max_workers error, must be int')
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
