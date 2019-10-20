from msg.const import EVENT_READ_BOOK
from msg.const import EVENT_WRITE_BOOK
from msg.engine import EventEngine
from msg.handler import AuthorHandler
from msg.handler import SleepHandler
from msg.handler import ReaderHandler
import time


def main():
    # 注册一般没有参数
    EventEngine().register(EVENT_WRITE_BOOK,
                           AuthorHandler(), ReaderHandler(), SleepHandler()
                           )
    EventEngine().register(EVENT_READ_BOOK, ReaderHandler(), SleepHandler())

    EventEngine().send(EVENT_WRITE_BOOK, delay=0.1, book_name='book1', second=0.4)
    EventEngine().send(EVENT_WRITE_BOOK, delay=0.4, book_name='book2')
    EventEngine().send(EVENT_READ_BOOK, delay=0, book_name='book3', second=0.6)
    EventEngine().send(EVENT_READ_BOOK, delay=0.1, book_name='book4')


if __name__ == '__main__':
    main()
