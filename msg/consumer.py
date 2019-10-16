from concurrent.futures import ThreadPoolExecutor
from queue import Empty
import time
import threading
import abc


class Consumer:
    def __init__(self, _queue, max_workers=10):
        self.thread_pool = ThreadPoolExecutor(max_workers=max_workers)
        self._queue = _queue
        self._active = False
        self._start()

    def _start(self):
        """
        """
        print('_start')
        _main_thread = threading.Thread(target=self._consume)
        if self._active:
            return
        self._active = True
        _main_thread.start()

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


class EventConsumer(Consumer):
    def _execute(self, _item: 'eventQueue._WorkItem'):
        """事件执行"""
        print('_execute', _item.cls_instance.delay)
        self._throw_to_thread_pool(_item)

class EventConsumerDelay(Consumer):
    def _execute(self, _item: 'eventQueue._WorkItem'):
        threading.Timer(_item.cls_instance.delay,
            function=self._throw_to_thread_pool, args=[_item]).start()




