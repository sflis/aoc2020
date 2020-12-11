from aoc2020.answer import Answer
import string


def check_hex(s):
    return s[0] == "#" and all(c in string.hexdigits for c in s[1:])


class Passport:
    def __init__(self, **kwargs):
        self.passport_fields_rules = {
            "byr": ("lim", {"": (1920, 2002)}),
            "iyr": ("lim", {"": (2010, 2020)}),
            "eyr": ("lim", {"": (2020, 2030)}),
            "hgt": ("lim", {"cm": (150, 193), "in": (59, 76)}),
            "hcl": ("fun", check_hex),
            "ecl": ("seq", ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
            "pid": ("fun", lambda x: x.isdigit() & (len(x) == 9)),
            "cid": ("fun", lambda x: True),
        }
        self.passport_fields = {k: None for k in self.passport_fields_rules.keys()}
        self.passport_fields.update(kwargs)

    def validate(self, exceptions):
        for k, v in self.passport_fields.items():
            if k not in exceptions and v is None:
                return False
        return True

    def ext_validation(self):

        for k, v in self.passport_fields.items():
            rule = self.passport_fields_rules[k]
            if rule[0] == "lim":
                for s, lim in rule[1].items():
                    if s in v:
                        i = (v.find(s) or len(v))
                        digit = int(v[:i])
                        if digit >= lim[0] and digit <= lim[1]:
                            break
                else:
                    return False
            elif rule[0] == "fun":
                if not rule[1](v):
                    return False
            elif rule[0] == "seq":
                if v not in rule[1]:
                    return False
        return True


def process_passport_data(data):
    passports = []
    entries = []
    for line in data:
        entries += line.split()
        if len(line) < 2:
            entries = [e.split(":") for e in entries]
            args = {e[0]: e[1] for e in entries}
            passports.append(Passport(**args))
            entries = []
    entries = [e.split(":") for e in entries]
    args = {e[0]: e[1] for e in entries}
    passports.append(Passport(**args))

    return passports


class AnswerD04(Answer):
    def _read_input(self, input_path):
        with open(input_path, "r") as f:
            self.passport_data = f.readlines()

    @property
    def answer1(self):
        passports = process_passport_data(self.passport_data)
        valid_passports = 0
        for passport in passports:
            if passport.validate(["cid"]):
                valid_passports += 1
        return valid_passports

    @property
    def answer2(self):
        passports = process_passport_data(self.passport_data)
        valid_passports = 0
        for passport in passports:
            if passport.validate(["cid"]) and passport.ext_validation():
                valid_passports += 1
        return valid_passports
