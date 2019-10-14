import time
from threadPool import thread_pool
from collections import defaultdict

from singleton import Singleton


class Engine(Singleton):
    __handlers = defaultdict(list)  # 事件处理字典{'func_name': [func1, func2]}
    workers = thread_pool.workers

    @classmethod
    def register(cls, msg_name: str, handler):
        """ 注册消息处理函数 """
        # 若不在, 则注册该消息事件
        handler_list = cls.__handlers[msg_name]
        if handler not in handler_list:
            handler_list.append(handler)

    @classmethod
    def send_message(cls, msg_name: str, *args, **kw):
        """ 发送消息 """
        for event in cls.__handlers[msg_name]:
            cls.workers.submit(event().execute, *args, **kw)


engine = Engine()
