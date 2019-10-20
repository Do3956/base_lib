import unittest
import time
import threading
from unittest import mock

from msg.const import EVENT_READ_BOOK
from msg.const import EVENT_WRITE_BOOK
from msg.engine import EventEngine
from msg.handler import AuthorHandler
from msg.handler import SleepHandler
from msg.handler import ReaderHandler


class TestMain(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self._delay = 0.1

    def test_async(self):
        start_time = time.time()

        event_write_book_handler_1 = AuthorHandler()
        event_write_book_handler_2 = ReaderHandler()
        event_write_book_handler_3 = SleepHandler()
        event_read_book_handler_1 = ReaderHandler()
        event_read_book_handler_2 = SleepHandler()

        EventEngine().register(EVENT_WRITE_BOOK,
                               event_write_book_handler_1,
                               event_write_book_handler_2,
                               event_write_book_handler_3
                               )
        EventEngine().register(EVENT_READ_BOOK,
                               event_read_book_handler_1,
                               event_read_book_handler_2)

        EventEngine().send(EVENT_WRITE_BOOK, delay=0.1, book_name='book1', second=0.4)
        EventEngine().send(EVENT_WRITE_BOOK, delay=0.5, book_name='book2')
        EventEngine().send(EVENT_READ_BOOK, delay=0, book_name='book3', second=0.6)
        EventEngine().send(EVENT_READ_BOOK, delay=0.2, book_name='book4')

        assert time.time() - start_time < 0.01

        t = threading.Thread(target=time.sleep, args=[1])
        t.start()
        t.join()
        assert EventEngine()._queue.qsize() == 0
