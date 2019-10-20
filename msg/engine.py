"""异步事件驱动引擎"""
from eventQueue import EventQueue
from threading import Thread

from decorator import singleton
from collections import defaultdict
from handler import BaseHandler
from consumer import EventConsumer

@singleton
class EventEngine:
    """
    事件引擎
    单例 init 不要加各种参数
    """

    def __init__(self):
        """
        初始事件引擎
        1. _event_queue: 待处理的事件Queue
        2. _handlers: 事件对应的处理器, 需提前注册
        """
        print('EventEngine')
        self.__queue = EventQueue(10000)
        self.__handlers = {}
        EventConsumer(self.__queue, 2).start()

    def register(self, event_name, *handlers) -> None:
        """事件注册"""
        print(type(handlers), handlers)
        self.__add_handlers(event_name, handlers)

    def send(self, event_name: str, delay=0, *args, **kwargs) -> None:
        """事件发送"""
        self.__notify(event_name, delay, *args, **kwargs)

    def __exist_event(self, event_name):
        if self.__handlers.get(event_name):
            return True
        return False

    def __check_handler(self, handler: 'BaseHandler()'):
        if not issubclass(handler.__class__, BaseHandler):
            raise Exception(f'{handler} is not from BaseHandler')

    def __check_handlers(self, handlers: 'BaseHandler()'):
        for handler in handlers:
            self.__check_handler(handler)

    def __add_handlers(self, event_name: str, handlers:list):
        self.__check_handlers(handlers)
        if self.__exist_event(event_name):
            raise Exception(f'event_name:{event_name} exist')

        self.__handlers[event_name] = handlers

    def __get_handler(self, event_name):
        return self.__handlers[event_name]

    def __notify(self, event_name, delay, *args, **kwargs):
        if not self.__get_handler(event_name):
            return
        self.__queue.add(self.__get_handler(event_name),
                        delay, *args, **kwargs)
