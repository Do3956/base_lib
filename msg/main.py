from const import EVENT_READ_BOOK
from const import EVENT_WRITE_BOOK
from engine import EventEngine
from handler import AuthorHandler, ReaderHandler
import time


def main():
    EventEngine().register(EVENT_WRITE_BOOK, AuthorHandler(1))
    EventEngine().register(EVENT_WRITE_BOOK, AuthorHandler())
    EventEngine().register(EVENT_READ_BOOK, ReaderHandler())
    EventEngine().register(EVENT_READ_BOOK, ReaderHandler(0.2))
    EventEngine().register(EVENT_READ_BOOK, ReaderHandler())

    EventEngine().send(EVENT_WRITE_BOOK, '写书')
    EventEngine().send(EVENT_READ_BOOK, '看书')


if __name__ == '__main__':
    main()
