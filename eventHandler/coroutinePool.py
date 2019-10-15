import asyncio
import queue
import time
from singleton import Singleton
import threading
import atexit


class EventItem:
    def __init__(self, fn, args, kwargs):
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    async def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            pass


class CoroutinePool(Singleton):
    def __init__(self, max_workers=5):
        super(CoroutinePool, self).__init__()
        self._max_workers = max_workers
        self._work_queue = queue.Queue()
        self._loop = asyncio.get_event_loop()
        self._shutdown = False
        self.main_thread = threading.Thread(
            name='main_thread_run_loop', target=self.run_loop)
        self.start_loop()

        # atexit.register(self._python_exit)

    def _python_exit(self):
        self.main_thread.join()
        self._shutdown = True
        self._loop.close()

    def submit(self, event, *args, **kw):
        if self._shutdown:
            raise RuntimeError('cannot schedule new futures after shutdown')

        w = EventItem(event, args, kw)
        self._work_queue.put(w)

    def __get_events(self):
        event_num = self._work_queue.qsize()
        event_num = min(event_num, self._max_workers)
        events = []
        for i in range(event_num):
            events.append(self._work_queue.get(block=True, timeout=0.1))
        return events

    def start_loop(self):
        self.main_thread.daemon = True
        self.main_thread.start()

    def run_loop(self):
        while not self._shutdown:
            events = self.__get_events()
            if events:
                self.__execute(events)

    def __execute(self, events: list):
        self._loop.run_until_complete(asyncio.wait(list(map(lambda x: x.run(), events))))


coroutine_pool=CoroutinePool(3)

if __name__ == "__main__":
    async def hello(sec):
        print(f"{time.time()}, Hello world!")
        r=await asyncio.sleep(sec)
        print(f"{time.time()}, Hello again!")

    loop=asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait([hello(0.1)]))
    # loop.run_until_complete(asyncio.wait([hello(0.1)]))
    # loop.run_until_complete(asyncio.wait([hello(0.1)]))
    # loop.run_until_complete(asyncio.wait([hello(1), hello(0.1)]))
    # loop.run_until_complete(asyncio.wait([hello(1), hello(0.1)]))
    # loop.run_until_complete(asyncio.wait([hello(1), hello(0.1)]))
    # loop.close()
