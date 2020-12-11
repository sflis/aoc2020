from aoc2020 import get_input
from aoc2020.d04_passport_processing import AnswerD04


def test_answers():
    example = AnswerD04(get_input(__file__, "example.txt"))

    assert example.answer1 == 2
    assert example.answer2 == 2

    input_ = AnswerD04(get_input(__file__, "input.txt"))
    print("")
    print(f"answer1: {input_.answer1}")
    print(f"answer2: {input_.answer2}")
