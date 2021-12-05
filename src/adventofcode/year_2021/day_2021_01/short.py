# noqa
import numpy as np
from adventofcode.util.input_helpers import get_input_for_day

n = np.loadtxt(get_input_for_day(2021, 1))


def part1():
    return ((n[1:] - n[:-1]) > 0).sum()


def part2():
    t = np.convolve(n, np.ones(3), "valid")
    return ((t[1:] - t[:-1]) > 0).sum()


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
