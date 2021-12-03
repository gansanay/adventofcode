# Advent of Code 2021, Day 01
# Attempting to share small, instructive, PEP8-compliant solutions!
# Any comments? Find me on:
#    - Twitter: @gansanay
#    - LinkedIn: https://linkedin.com/in/gansanay
import numpy as np


def diff(x):
    """Differences between subsequent values of a numpy.array"""
    return x[1:] - x[:-1]


def count_pos(x):
    """Number of positive values in a numpy.array"""
    return (x > 0).sum()


def rolling_sum(x, n):
    """Rolling sum of a numpy.array every n values"""
    return np.convolve(x, np.ones(n), "valid")


lengths = np.loadtxt("aoc_input_01.txt")

# Part 1
length_diffs = diff(lengths)
part1 = count_pos(length_diffs)
print(f"Solution for part 1: {part1}")

# Part 2
by_three = rolling_sum(lengths, 3)
by_three_diffs = diff(by_three)
part2 = count_pos(by_three_diffs)
print(f"Solution for part 2: {part2}")
