"""异步事件驱动引擎"""
from eventQueue import EventQueue
from threading import Thread

from decorator import singleton
from collections import defaultdict
from handler import BaseHandler
from consumer import EventConsumer
from const import CONSUMER_TYPE_EVENT
from const import CONSUMER_TYPE_EVENT_DELAY
from consumerFactory import ConsumerFactory

@singleton
class EventEngine:
    """事件引擎"""

    def __init__(self, queue_max_size=10000, max_thread=2, consumer_type=CONSUMER_TYPE_EVENT_DELAY):
        """
        初始事件引擎
        1. _event_queue: 待处理的事件Queue
        2. _handlers: 事件对应的处理器, 需提前注册
        """
        print('EventEngine')
        self._queue = EventQueue(queue_max_size)
        print('_event_queue')
        self._handlers = defaultdict(list)
        ConsumerFactory().get_consumer(consumer_type)(self._queue, max_thread)

    def _exist_handler(self, event_name, handler):
        if handler in self._handlers[event_name]:
            return True
        return False

    def _check_handler(self, handler: 'BaseHandler()'):
        if not issubclass(handler.__class__, BaseHandler):
            raise Exception(f'{handler} is not from BaseHandler')

    def _add_handler(self, event_name:str, handler):
        self._check_handler(handler)
        if self._exist_handler(event_name, handler):
            raise Exception(f'handler:{handler} exist')

        self._handlers[event_name].append(handler)

    def _get_handler(self, event_name):
        return self._handlers[event_name]

    def register(self, event_name, handler) -> None:
        """事件注册"""
        self._add_handler(event_name, handler)

    def send(self, event_name: str, *args, **kw) -> None:
        """事件发送"""
        self._notify(event_name, *args, **kw)

    def _notify(self, event_name, *args, **kw):
        if not self._get_handler(event_name):
            return
        self._queue.accept(self._get_handler(event_name), *args, **kw)
