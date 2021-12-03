# Advent of Code 2021, Day 01
# Attempting to share small, instructive, PEP8-compliant solutions!
# Any comments? Find me on:
#    - Twitter: @gansanay
#    - LinkedIn: https://linkedin.com/in/gansanay
import numpy as np

from adventofcode.util.input_helpers import get_input_for_day


def diff(x):
    """Differences between subsequent values of a numpy.array"""
    return x[1:] - x[:-1]


def count_pos(x):
    """Number of positive values in a numpy.array"""
    return (x > 0).sum()


def rolling_sum(x, n):
    """Rolling sum of a numpy.array every n values"""
    return np.convolve(x, np.ones(n), "valid")


lengths = np.loadtxt(get_input_for_day(2021, 1))


def part1():
    length_diffs = diff(lengths)
    return count_pos(length_diffs)


def part2():
    by_three = rolling_sum(lengths, 3)
    by_three_diffs = diff(by_three)
    return count_pos(by_three_diffs)


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
