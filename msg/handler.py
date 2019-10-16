import abc


class BaseHandler(metaclass=abc.ABCMeta):
    """事件基类"""

    def __init__(self, delay=0):
        self.delay = delay

    def execute(self, *args, **kw):
        """执行"""
        self._execute(*args, **kw)

    @abc.abstractmethod
    def _execute(self, *args, **kw) -> None:
        """受保护的执行"""


class ReaderHandler(BaseHandler):

    def __read_book(self, book_name):
        print(f"正在看书:<<{book_name}>>")

    def _execute(self, book_name):
        self.__read_book(book_name)


class AuthorHandler(BaseHandler):

    def __write_book(self, book_name):
        print(f'<<{book_name}>>书籍出版')

    def _execute(self, book_name):
        self.__write_book(book_name)


if __name__ == "__main__":
    print(issubclass(BaseHandler, AuthorHandler))
    print(issubclass(AuthorHandler, BaseHandler))
    print(issubclass(AuthorHandler().__class__, BaseHandler))
