from queue import Queue
import threading
import time


class _WorkItem(object):
    def __init__(self, cls_instance, args, kwargs):
        self.cls_instance = cls_instance
        self.args = args
        self.kwargs = kwargs

    def execute(self):
        print('_WorkItem...execute', self.cls_instance, self.args, self.kwargs)
        print('_WorkItem...execute', self.cls_instance.delay)
        self.cls_instance.execute(*self.args, **self.kwargs)


class EventQueue(Queue):
    """
    延时处理
    优先级
    maxsize: 负数 代表不限制，最大内存模式，
    """

    def __init__(self, max_size=10000):
        super(EventQueue, self).__init__(max_size)
        self.cond_has_event = threading.Condition()

    def _package_hander(self, handler, *args, **kw):
        print('_package_hander', handler.delay)
        return _WorkItem(handler, args, kw)

    def accept(self, handlers, *args, **kw):
        print('accept')
        with self.cond_has_event:
            self._add_handlers(handlers, *args, **kw)
            print('_add_handlers')
            self.cond_has_event.notify()
            print('notify')

    def _add_handlers(self, handlers, *args, **kw):
        for h in handlers:
            _item = self._package_hander(h, *args, **kw)
            print('_add_handlers', _item.execute, _item.cls_instance.delay)
            self.put_nowait(_item)


