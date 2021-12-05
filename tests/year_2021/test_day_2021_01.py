from adventofcode.year_2021.day_2021_01 import readable, short


def test_readable_part_one():
    answer = readable.part1()
    assert answer == 1616


def test_readable_part_two():
    answer = readable.part2()
    assert answer == 1645


def test_short_part_one():
    answer = short.part1()
    assert answer == 1616


def test_short_part_two():
    answer = short.part2()
    assert answer == 1645
