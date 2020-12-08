from aoc2020 import get_input
from aoc2020.d01_report_repair import AnswerD01, sum_pair_equals, sum_triad_equals
import numpy as np


def test_sum_pair_equals():
    assert np.array_equal(sum_pair_equals([3, 5, 9], 8), [0, 1])


def test_sum_triad_equals():
    assert np.array_equal(sum_triad_equals([3, 2, 1], 6), [0, 1, 2])


def test_answers():
    example = AnswerD01(get_input(__file__, "example.txt"))

    assert example.answer1 == 514579
    assert example.answer2 == 241861950

    input_ = AnswerD01(get_input(__file__, "input.txt"))
    print("")
    print(f"answer1: {input_.answer1}")
    print(f"answer2: {input_.answer2}")
