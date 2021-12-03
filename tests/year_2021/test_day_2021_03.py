import pytest

from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_2021_03 import readable, short

def test_readable_part_one():
    answer = readable.part1()
    assert answer == 4138664


def test_readable_part_two():
    answer = readable.part2()
    assert answer == 4273224


def test_short_part_one():
    answer = short.part1()
    assert answer == 4138664


def test_short_part_two():
    answer = short.part2()
    assert answer == 4273224
