from aoc2020 import get_input
from aoc2020.d07_handy_haversacks import AnswerD07


def test_answers():
    example = AnswerD07(get_input(__file__, "example.txt"))

    assert example.answer1 == 4
    assert example.answer2 == 32

    input_ = AnswerD07(get_input(__file__, "input.txt"))
    print("")
    print(f"answer1: {input_.answer1}")
    print(f"answer2: {input_.answer2}")
