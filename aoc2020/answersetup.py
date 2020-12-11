import requests
import argparse
import os
import urllib.request
import json

# import shutil
from pathlib import Path

templ = """from aoc2020.answer import Answer


class AnswerD{day:02}(Answer):
    def _read_input(self, input_path):
        pass

    @property
    def answer1(self):
        pass

    @property
    def answer2(self):
        pass

"""
test_tmpl = """
def test_answers():
    example = AnswerD{day:02}(get_input(__file__, "example.txt"))

    assert example.answer1 == None
    assert example.answer2 == None

    input_ = AnswerD{day:02}(get_input(__file__, "input.txt"))
    print("")
    print(f"answer1: {{input_.answer1}}")
    print(f"answer2: {{input_.answer2}}")
"""


def gen_file(path, content):
    with open(path, "w") as f:
        f.writelines(content)


def extract_data_from_url(day):
    base_url = "https://adventofcode.com/2020/day"
    url = f"{base_url}/{day}"
    page = requests.get(url)
    data = {}

    j = page.content.find(b"<pre><code>") + len("<pre><code>")
    j2 = page.content[j:].find(b"</code>")
    data["example"] = page.content[j:][:j2].decode()

    descr = b'<article class="day-desc">'
    i = page.content.find(descr) + len(descr) + len("<h2>")
    i2 = page.content[i:].find(b"</h2>")

    raw_title = page.content[i:][:i2]
    print(raw_title.decode())

    title = "_".join(raw_title.decode().split(":")[1][:-3].lower().split())
    data["folder_name"] = f"d{day:02}_{title}"

    print(data["folder_name"])
    input_url = f"{url}/input"
    cookie = json.load(open(Path(__file__).parent.absolute() / "cookie.json"))
    data["input"] = requests.post(input_url, cookies=cookie).content.decode()
    data["day"] = day
    data["title"] = title
    return data


def create_folder(data):
    path = Path(__file__).parent.absolute() / data["folder_name"]
    if os.path.isdir(path):
        print("Folder for day has already been created")
        exit()
    os.makedirs(path)
    gen_file(path / "__init__.py", "from .answer import AnswerD{day:02}".format(**data))
    gen_file(path / "answer.py", templ.format(**data))
    gen_file(path / "methods.py", "")
    gen_file(
        path / "test_.py",
        "from aoc2020 import get_input\n"
        "from aoc2020.d{day:02}_{title} import AnswerD{day:02}".format(**data)
        + test_tmpl.format(**data),
    )
    gen_file(path / "input.txt", data["input"])
    gen_file(path / "example.txt", data["example"])


def main():
    parser = argparse.ArgumentParser(
        description="Setup answer folder for a new day of advent of code"
    )
    parser.add_argument("day", type=int, help="The day of the advent to setup")

    args = parser.parse_args()
    data = extract_data_from_url(args.day)
    create_folder(data)


if __name__ == "__main__":
    main()
