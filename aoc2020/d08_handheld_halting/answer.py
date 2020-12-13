from aoc2020.answer import Answer
import copy


def execute_program(inputs):
    line = 0
    op = inputs[line]
    visited_lines = set()
    acc = 0
    terminated = False
    while line not in visited_lines and line <= len(inputs) - 1:
        op = inputs[line]
        visited_lines.add(line)
        if op[0] == "jmp":
            line += op[1]
        elif op[0] == "acc":
            acc += op[1]
            line += 1
        else:
            line += 1
        # print(line, acc, op)

    if line == len(inputs):
        terminated = True
    return acc, terminated


class AnswerD08(Answer):
    def _read_input(self, input_path):
        with open(input_path, "r") as f:
            self.raw_inputs = f.readlines()
        self.inputs = []
        for l in self.raw_inputs:
            op, val = l.split()
            self.inputs.append((op, int(val)))

    @property
    def answer1(self):
        acc, term = execute_program(self.inputs)
        print(term)
        return acc

    @property
    def answer2(self):
        op_index = [i for i, op in enumerate(self.inputs) if op[0] in ["jmp", "nop"]]
        for i in op_index:
            fixed_input = copy.copy(self.inputs)
            fixed_input[i] = (
                ("jmp", fixed_input[1])
                if fixed_input[0] == "nop"
                else ("nop", fixed_input[1])
            )
            acc, term = execute_program(fixed_input)
            # print(acc,term)
            if term:
                return acc
        return 0
