import numpy as np

from adventofcode.util.input_helpers import get_input_for_day_as_str

data = np.array([int(t) for t in get_input_for_day_as_str(2021, 7).split(",")])


def fuel(pos):
    """Linear fuel consumption for a target position"""
    return int(abs(data - pos).sum())


def fuel_cumulative(pos):
    """Cumulative fuel consumption for a target position"""
    return int(np.sum([k * (k + 1) / 2 for k in abs(data - pos)]))


def part1():
    # By definition of the median of a set of values
    return fuel(np.median(data))


def part2():
    # The mean of a set minimizes the cumulative fuel but is not an integer,
    # use the minimum fuel consumption between the two adjacent integers
    m = np.mean(data)
    return min((fuel_cumulative(np.floor(m)), fuel_cumulative(np.ceil(m))))
