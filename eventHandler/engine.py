import time
from collections import defaultdict

from singleton import Singleton


class Engine(Singleton):
    def __init__(self, workers):
        Singleton.__init__(self)
        # 事件处理字典{'func_name': [func1, func2]}
        self._handlers = defaultdict(list)
        self._workers = workers

    def register(self, msg_name: str, handler):
        """ 注册消息处理函数 """
        # 若不在, 则注册该消息事件
        handler_list = self._handlers[msg_name]
        assert handler not in handler_list
        handler_list.append(handler)

    def send_message(self, msg_name: str, *args, **kw) -> None:
        """ 发送消息，获取消息对应的事件列表，逐个发送给消费者 """
        for event in self._handlers[msg_name]:
            self.send_event(event, *args, **kw)

    def send_event(self, event: 'class', *args, **kw) -> None:
        """ 发送单个事件 """
        self._workers.submit(event().execute, *args, **kw)

