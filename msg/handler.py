import abc
import time

class BaseHandler(metaclass=abc.ABCMeta):
    """事件基类"""

    def __init__(self, delay=0):
        if not isinstance(delay, (int, float)) or delay < 0.0:
            raise AttributeError('delay error, must be gte 0.0')
        self.delay = delay

    def _prepare(self, *args, **kw):
        if self.delay > 0:
            time.sleep(self.delay)

    def execute(self, *args, **kw):
        """执行"""
        self._prepare(*args, **kw)
        self._execute(*args, **kw)

    @abc.abstractmethod
    def _execute(self, *args, **kw) -> None:
        """受保护的执行"""


class ReaderHandler(BaseHandler):

    def __read_book(self, book_name):
        print(f"{time.time()}, 正在看书:<<{book_name}>>")

    def _execute(self, book_name):
        self.__read_book(book_name)


class AuthorHandler(BaseHandler):

    def __write_book(self, book_name):
        print(f'{time.time()}, <<{book_name}>>书籍出版')

    def _execute(self, book_name):
        self.__write_book(book_name)


if __name__ == "__main__":
    print(issubclass(BaseHandler, AuthorHandler))
    print(issubclass(AuthorHandler, BaseHandler))
    print(issubclass(AuthorHandler().__class__, BaseHandler))
