from aoc2020.answer import Answer
from collections import defaultdict


class AnswerD06(Answer):
    def _read_input(self, input_path):
        with open(input_path, "r") as f:
            self.answers = f.readlines()

    @property
    def answer1(self):

        count = 0
        current_answer_set = set()
        for answer in self.answers:
            if len(answer) == 1:
                count += len(current_answer_set)
                current_answer_set = set()
            for c in answer[:-1]:
                current_answer_set.add(c)
        count += len(current_answer_set)
        return count

    @property
    def answer2(self):
        count = 0
        current_answer_set = defaultdict(lambda: 0)
        group_size = 0
        for answer in self.answers:
            if len(answer) == 1:
                for k, v in current_answer_set.items():
                    if v == group_size:
                        count += 1
                current_answer_set = defaultdict(lambda: 0)
                group_size = -1

            for c in answer[:-1]:
                current_answer_set[c] += 1
            group_size += 1
        for k, v in current_answer_set.items():
            if v == group_size:
                count += 1
        return count
