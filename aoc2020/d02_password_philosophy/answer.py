from aoc2020.answer import Answer
from collections import namedtuple


class AnswerD02(Answer):
    def _read_input(self, input_path):
        Rule = namedtuple("Rule", "char min max")
        self.data = []
        with open(input_path, "r") as f:
            for line in f.readlines():
                rule, passw = line.split(":")
                minmax, char = rule.split()
                min_, max_ = minmax.split("-")
                self.data.append((passw.strip(), Rule(char, int(min_), int(max_))))

    @property
    def answer1(self):
        valid = 0
        for entry in self.data:
            passw, rule = entry
            c = passw.count(rule.char)
            if c >= rule.min and c <= rule.max:
                valid += 1
        return valid

    @property
    def answer2(self):
        valid = 0
        for entry in self.data:
            passw, rule = entry
            i1, i2 = rule.min - 1, rule.max - 1
            if rule.char in [passw[i1], passw[i2]] and passw[i1] != passw[i2]:
                valid += 1
        return valid
