import time

from abc import ABC, abstractmethod


class JobBase(ABC):
    @staticmethod
    @abstractmethod
    async def execute(self, *args, **kw) -> None:
        """
        """


class JobSleep(JobBase):
    async def execute(self) -> None:
        print(f'{time.time()}: JobSleep begin...')
        time.sleep(1)
        print(f'{time.time()}: JobSleep end...')


class JobPrint(JobBase):
    async def execute(self) -> None:
        print(f'{time.time()}: JobPrint...')
