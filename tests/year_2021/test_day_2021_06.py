from adventofcode.year_2021.day_2021_06 import readable


def test_readable_part_one():
    answer = readable.part1()
    assert answer == 365862


def test_readable_part_two():
    answer = readable.part2()
    assert answer == 1653250886439
