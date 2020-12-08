from aoc2020 import get_input
from aoc2020.d02_password_philosophy import AnswerD02


def test_answers():
    example = AnswerD02(get_input(__file__, "example.txt"))

    assert example.answer1 == 2
    assert example.answer2 == 1

    input_ = AnswerD02(get_input(__file__, "input.txt"))
    print("")
    print(f"answer1: {input_.answer1}")
    print(f"answer2: {input_.answer2}")
