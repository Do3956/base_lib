from msg.thread_manager import ThreadManager
from queue import Empty
import time
import threading
import abc
import traceback

from msg.event_queue import EventQueue


class Consumer:
    def __init__(self, _queue, max_workers=10):
        if not issubclass(_queue.__class__, EventQueue):
            raise AttributeError(f'{_queue} is not from EventQueue')
        self.thread_pool_executor = ThreadManager(
            max_workers=max_workers).executor
        self._queue = _queue
        self._active = False

    def __get_job(self):
        return self._queue.get_nowait()

    def __recover_job(self, job):
        self._queue.put_nowait(job)

    def __get_job_num(self):
        return self._queue.qsize()

    def __get_single(self):
        return self._queue.cond_has_event

    def __wait_single(self, second):
        print('__wait_single', second)
        self._queue.cond_has_event.wait(second)

    def start(self):
        """
        """
        print('start')
        _main_thread = threading.Thread(target=self._run_event_loop)
        if self._active:
            return
        self._active = True
        _main_thread.start()
        print('start finish')

    def _run_event_loop(self):
        """事件队列消费"""
        print('_run_event_loop')
        while self._active:
            print('self._active')
            with self.__get_single():
                second = self._consume()
                self.__wait_single(second)

    def __min_second(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        return min(a, b)

    def _consume(self) -> any:
        """
        return: wait timeout: None/int
        """
        wait_second = None
        for _ in range(self.__get_job_num()):
            job = self.__get_job()
            if job.can_execute():
                self._execute(job)
            else:
                self.__recover_job(job)
                return job.need_wait_second()
        #         wait_second = self._min_second(job.need_wait_second(), wait_second)
        # print('_consume', wait_second)
        # return wait_second

    @abc.abstractmethod
    def _execute(self, _job: 'eventQueue.HandlePackage') -> None:
        """事件执行"""
        # print('_execute', _job.cls_instance.delay)
        self._throw_to_thread_pool(_job)

    def _throw_to_thread_pool(self, _job: 'eventQueue.HandlePackage'):
        # print('throw_to_thread_pool')
        self.thread_pool_executor.submit(_job.execute)


class EventConsumer(Consumer):
    def _execute(self, _job: 'eventQueue.HandlePackage'):
        """事件执行"""
        # print('_execute', _job.cls_instance.delay)
        self._throw_to_thread_pool(_job)
