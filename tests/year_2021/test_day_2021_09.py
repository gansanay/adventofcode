from adventofcode.year_2021.day_2021_09 import readable


def test_readable_part_one():
    answer = readable.part1()
    assert answer == 562


def test_readable_part_two():
    answer = readable.part2()
    assert answer == 1076922
