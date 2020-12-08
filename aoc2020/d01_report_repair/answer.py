from aoc2020.answer import Answer
from aoc2020.d01_report_repair import sum_pair_equals, sum_triad_equals
import numpy as np


class AnswerD01(Answer):
    def _read_input(self, input_path):
        with open(input_path, "r") as f:
            self.data = np.array([int(i) for i in f.readlines()])

    @property
    def answer1(self):
        sum_pair = sum_pair_equals(self.data, 2020)
        return np.product(self.data[sum_pair])

    @property
    def answer2(self):
        sum_pair = sum_triad_equals(self.data, 2020)
        return np.product(self.data[sum_pair])
