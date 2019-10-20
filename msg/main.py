from const import EVENT_READ_BOOK
from const import EVENT_WRITE_BOOK
from engine import EventEngine
from handler import AuthorHandler
from handler import SleepHandler
from handler import ReaderHandler
import time


def main():
    # 注册一般没有参数
    EventEngine().register(EVENT_WRITE_BOOK,
                           AuthorHandler(), ReaderHandler(), SleepHandler()
        )
    EventEngine().register(EVENT_READ_BOOK, ReaderHandler(), SleepHandler())

    EventEngine().send(EVENT_WRITE_BOOK, delay=0.1, book_name='book1', second=0.4)
    EventEngine().send(EVENT_WRITE_BOOK, delay=2, book_name='book2')
    EventEngine().send(EVENT_READ_BOOK, delay=0, book_name='book3', second=0.6)
    EventEngine().send(EVENT_READ_BOOK, delay=0.1, book_name='book4')


if __name__ == '__main__':
    main()
