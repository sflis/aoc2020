from aoc2020.answer import Answer
import copy


def process_rules(raw_rules):
    color_rules = {}
    for rr in raw_rules:
        color_token, contains_expr = rr[:-2].split("contain")
        bag_color = " ".join(color_token.split()[:-1])

        if bag_color not in color_rules:
            color_rules[bag_color] = {"contain": {}, "contained_in": []}
        bag_rule_tree = color_rules[bag_color]

        if "no other bags" in contains_expr:
            continue

        bag_rules = contains_expr.split(",")
        for bag_rule in bag_rules:
            bag_tokens = bag_rule.split()
            number = bag_tokens[0]
            color = " ".join(bag_tokens[1:3])
            if "no" in number:
                print(rr)
                print(color_token, contains_expr)
            bag_rule_tree["contain"][color] = int(number)
            if color not in color_rules:
                color_rules[color] = {"contain": {}, "contained_in": []}
            color_rules[color]["contained_in"].append(bag_color)

    return color_rules


def number_of_outer_bag_colors(bag_color, rules):
    colors = set()
    contained_in = copy.copy(rules[bag_color]["contained_in"])
    while len(contained_in) > 0:
        cc = contained_in.pop()
        colors.add(cc)
        contained_in += copy.copy(rules[cc]["contained_in"])
        for c in colors:
            if c in contained_in:
                contained_in.remove(c)
    return colors


def rec_number_of_contained_bags(bag_color, rules, level=0):
    n_bags = 1
    levels = [level]
    for color, n in rules[bag_color]["contain"].items():
        nn, level = rec_number_of_contained_bags(color, rules, level + 1)
        n_bags += n * nn
        levels.append(level)
    return n_bags, max(levels)


class AnswerD07(Answer):
    def _read_input(self, input_path):
        with open(input_path, "r") as f:
            self.raw_rules = f.readlines()
        self.color_rules = process_rules(self.raw_rules)

    @property
    def answer1(self):
        colors = number_of_outer_bag_colors("shiny gold", self.color_rules)
        return len(colors)

    @property
    def answer2(self):
        n, level = rec_number_of_contained_bags("shiny gold", self.color_rules)
        print(level)
        return n - 1
