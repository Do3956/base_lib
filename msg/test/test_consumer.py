import unittest
import time
from unittest import mock

from msg.consumer import EventConsumer
from msg.handler import ReaderHandler
from msg.event_queue import EventQueue


class TestEventConsumer(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self._handler = ReaderHandler()
        self._queue = EventQueue()
        self._consumer = EventConsumer(self._queue)
        self._delay = 0.1

    def tearDown(self):
        super().tearDown()

    def test_init(self):
        try:
            EventConsumer('event')
        except AttributeError as e:
            assert e.__str__() == 'event is not from EventQueue'

    def test_consume_delay(self):
        self._queue.add([self._handler], self._delay)
        second = self._consumer._consume()
        assert abs(self._delay - second) < 0.001

    def test_consume(self):
        self._queue.add([self._handler], delay=0, book_name='abc')
        second = self._consumer._consume()
        assert second is None
