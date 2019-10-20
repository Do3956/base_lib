from queue import Queue
import threading
import time


class HandlePackage(object):
    def __init__(self, cls_instance, delay, *args, **kwargs):
        self.cls_instance = cls_instance
        self.delay = delay
        self.args = args
        self.kwargs = kwargs
        self.create_time = time.time()

    def can_execute(self):
        return time.time() - self.create_time >= self.delay

    def need_wait_second(self):
        wait_second = self.delay - (time.time() - self.create_time)
        return wait_second if wait_second > 0 else 0

    def execute(self):
        print('HandlePackage...execute',
              self.cls_instance, self.args, self.kwargs)
        result = self.cls_instance.execute(*self.args, **self.kwargs)
        if hasattr(self.cls_instance, 'callback'):
            self.cls_instance.callback(result, *self.args, **self.kwargs)


class EventQueue(Queue):
    """
    延时处理
    优先级
    maxsize: 负数 代表不限制，最大内存模式，
    """

    def __init__(self, max_size=10000):
        if not isinstance(max_size, (int)):
            raise AttributeError('max_size error, must be int')
        super(EventQueue, self).__init__(max_size)
        self.cond_has_event = threading.Condition()

    def _package_hander(self, handler, delay, *args, **kwargs):
        # print('_package_hander', handler.delay)
        return HandlePackage(handler, delay, *args, **kwargs)

    def add(self, handlers, delay, *args, **kwargs):
        with self.cond_has_event:
            self._add_handlers(handlers, delay, *args, **kwargs)
            print('notify...')
            self.cond_has_event.notify()

    def _add_handlers(self, handlers, delay, *args, **kwargs):
        for handler in handlers:
            _job = self._package_hander(handler, delay, *args, **kwargs)
            # print('_add_handlers', _job.execute, _job.cls_instance.delay)
            self.put_nowait(_job)
