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
from msg.main import main


class TestMain(unittest.TestCase):

    def setUp(self):
        super().setUp()
        EventEngine().clean_register()

    def test_async(self):
        start_time = time.time()
        main()
        assert time.time() - start_time < 0.01

    def test_all_done(self):
        main()
        t = threading.Thread(target=time.sleep, args=[1])
        t.start()
        t.join()
        assert EventEngine()._queue.qsize() == 0
