import unittest
import time
from unittest import mock

from msg.consumer import EventConsumer
from msg.handler import ReaderHandler
from msg.event_queue import EventQueue
from msg.event_queue import HandlePackage


class TestEventQueue(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self._handler = ReaderHandler()
        self._queue = EventQueue()
        self._delay = 0.1

    def test_add(self):
        self._queue.add([self._handler], self._delay)
        assert self._queue.qsize() == 1
        self._queue.add([self._handler, self._handler,
                         self._handler], self._delay)
        assert self._queue.qsize() == 4


class TestHandlePackage(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self._handler = ReaderHandler()
        self._delay = 1
        # self._job = HandlePackage(self._handler, self._delay)

    def test_can_execute(self):
        assert HandlePackage(self._handler, self._delay).can_execute() is False
        assert HandlePackage(self._handler, 0).can_execute() is True

    def test_need_wait_second(self):
        assert abs(self._delay - HandlePackage(self._handler, self._delay).need_wait_second()) < 0.01

    def test_execute(self):
        HandlePackage(self._handler, 0).execute()
        assert self._handler._execute_time is not None
