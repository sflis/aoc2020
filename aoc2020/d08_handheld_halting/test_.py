from aoc2020 import get_input
from aoc2020.d08_handheld_halting import AnswerD08


def test_answers():
    example = AnswerD08(get_input(__file__, "example.txt"))

    assert example.answer1 == 5
    assert example.answer2 == 8

    input_ = AnswerD08(get_input(__file__, "input.txt"))
    print("")
    print(f"answer1: {input_.answer1}")
    print(f"answer2: {input_.answer2}")
