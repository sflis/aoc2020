from aoc2020 import get_input
from aoc2020.d03_toboggan_trajectory import AnswerD03


def test_answers():
    example = AnswerD03(get_input(__file__, "example.txt"))

    assert example.answer1 == 7
    assert example.answer2 == 336

    input_ = AnswerD03(get_input(__file__, "input.txt"))
    print("")
    print(f"answer1: {input_.answer1}")
    print(f"answer2: {input_.answer2}")
