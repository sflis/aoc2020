from aoc2020 import get_input
from aoc2020.d06_custom_customs import AnswerD06


def test_answers():
    example = AnswerD06(get_input(__file__, "example.txt"))

    assert example.answer1 == 11
    assert example.answer2 == 6

    input_ = AnswerD06(get_input(__file__, "input.txt"))
    print("")
    print(f"answer1: {input_.answer1}")
    print(f"answer2: {input_.answer2}")
