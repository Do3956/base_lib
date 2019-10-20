import unittest
from unittest import mock

from msg.handler import SleepHandler
from msg.handler import ReaderHandler
from msg.handler import AuthorHandler


class TestHandler(unittest.TestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_execute(self):
        ReaderHandler().execute()
        SleepHandler().execute()
        AuthorHandler().execute()

    def test_execute_with_params(self):
        ReaderHandler().execute(book_name=12)
        ReaderHandler().execute(second=12)
        SleepHandler().execute(second=0.01)
        SleepHandler().execute(second=-0.01)
        SleepHandler().execute(second='fds')
        AuthorHandler().execute(book_name=12)
        AuthorHandler().execute(second=12)

    def test_callback(self):
        ReaderHandler().callback(second=0.01)
        AuthorHandler().callback(second=0.01)
        try:
            SleepHandler().callback(second=0.01)
        except AttributeError:
            pass
