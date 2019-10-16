from const import EVENT_READ_BOOK
from const import EVENT_WRITE_BOOK
from engine import EventEngine
from handler import AuthorHandler, ReaderHandler
import time


def main():
    EventEngine().register(EVENT_WRITE_BOOK, AuthorHandler(delay=1))
    EventEngine().register(EVENT_WRITE_BOOK, AuthorHandler())
    EventEngine().register(EVENT_READ_BOOK, ReaderHandler())
    EventEngine().register(EVENT_READ_BOOK, ReaderHandler(delay=0.2))
    EventEngine().register(EVENT_READ_BOOK, ReaderHandler())

    EventEngine().send(EVENT_WRITE_BOOK, '写书1')
    EventEngine().send(EVENT_WRITE_BOOK, '写书2')
    EventEngine().send(EVENT_READ_BOOK, '看书1')
    EventEngine().send(EVENT_READ_BOOK, '看书2')


if __name__ == '__main__':
    main()
