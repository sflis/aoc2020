from abc import ABCMeta, abstractmethod
from pathlib import Path


def get_input(file, name):
    return Path(file).parent / name


class Answer(metaclass=ABCMeta):
    def __init__(self, input_path):
        if not input_path.exists():
            raise ValueError(f"File does not exist: {input_path}")

        self.input = self._read_input(input_path)

    @abstractmethod
    def _read_input(self, input_path):
        pass

    @property
    @abstractmethod
    def answer1(self):
        pass

    @property
    @abstractmethod
    def answer2(self):
        pass

    @property
    def execution_time(self):
        return dict(input=0, answer1=0, answer2=0)
