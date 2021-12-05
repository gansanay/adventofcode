from adventofcode.year_2021.day_2021_05 import readable


def test_readable_part_one():
    answer = readable.part1()
    assert answer == 6856


def test_readable_part_two():
    answer = readable.part2()
    assert answer == 20666
