from aoc2020.answer import Answer
import numpy as np


def traverse_pattern(patterns, right, down=1):
    n_trees = 0
    x_pos = 0
    pattern_len = len(patterns[0]) - 1
    for i in range(0, len(patterns), down):
        p = patterns[i]
        n_patterns = x_pos // pattern_len + 1
        pattern = p[:-1] * n_patterns
        if pattern[x_pos] == "#":
            n_trees += 1
        x_pos += right
    return n_trees


class AnswerD03(Answer):
    def _read_input(self, input_path):
        with open(input_path, "r") as f:
            self.pattern = f.readlines()

    @property
    def answer1(self):
        return traverse_pattern(self.pattern, 3)

    @property
    def answer2(self):
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        trees = []
        for slope in slopes:
            trees.append(traverse_pattern(self.pattern, *slope))
        return np.product(trees)
