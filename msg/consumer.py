from concurrent.futures import ThreadPoolExecutor
from queue import Empty
import time
import threading
import abc
import atexit

from eventQueue import EventQueue

class Consumer:
    def __init__(self, _queue, max_workers=10):
        if not issubclass(_queue.__class__, EventQueue):
            raise AttributeError('max_workers error, must be int')
        if not isinstance(max_workers, (int)):
            raise AttributeError('max_workers error, must be int')
        self.thread_pool = ThreadPoolExecutor(max_workers=max_workers)
        self._queue = _queue
        self._active = False
        self._start()
        atexit.register(self._python_exit)

    def _start(self):
        """
        """
        print('_start')
        _main_thread = threading.Thread(target=self._consume)
        if self._active:
            return
        self._active = True
        _main_thread.start()
        print('start finish')

    def _consume(self):
        """事件队列消费"""
        print('_consume')
        while self._active:
            print('self._active')
            with self._queue.cond_has_event:
                print('cond_has_event')
                try:
                    _item = self._queue.get_nowait()
                    print('_item', _item)
                    self._execute(_item)
                except Empty:
                    print('Empty')
                    self._queue.cond_has_event.wait()

    @abc.abstractmethod
    def _execute(self, _item: 'eventQueue._WorkItem') -> None:
        """事件执行"""
        print('_execute', _item.cls_instance.delay)
        self._throw_to_thread_pool(_item)

    def _throw_to_thread_pool(self, _item: 'eventQueue._WorkItem'):
        print('throw_to_thread_pool')
        self.thread_pool.submit(_item.execute)

    def _python_exit(self):
        self._active = False
        print('_python_exit')
        # items = list(_threads_queues.items())
        # for t, q in items:
        #     q.put(None)
        # for t, q in items:
        #     t.join()


class EventConsumer(Consumer):
    def _execute(self, _item: 'eventQueue._WorkItem'):
        """事件执行"""
        print('_execute', _item.cls_instance.delay)
        self._throw_to_thread_pool(_item)

class EventConsumerDelay(Consumer):
    def _execute(self, _item: 'eventQueue._WorkItem'):
        pass




