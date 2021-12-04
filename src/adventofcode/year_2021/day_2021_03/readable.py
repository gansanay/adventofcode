# Advent of Code 2021, Day 03
# Attempting to share small, instructive, PEP8-compliant solutions!
# Any comments? Find me on:
#    - Twitter: @gansanay
#    - LinkedIn: https://linkedin.com/in/gansanay
import numpy as np

from adventofcode.util.input_helpers import get_input_for_day

data = np.loadtxt(get_input_for_day(2021, 3), dtype="str")
matrix = np.array([list(e) for e in data]).astype(int)


def int_from_bin_list(lst):
    """Convert a list of 0s and 1s into an integer

    Args:
        lst (list or numpy.array): list of 0s and 1s

    Returns:
        int: resulting integer
    """
    return int("".join(str(x) for x in lst), 2)


def consumption_rate(m, rate):
    """Compute the consumption rate for gamma and epsilon types

    Args:
        m (numpy.array): 2-dimensional array of Os and 1s
        rate (str): type of consumption rate, either 'gamma' or 'epsilon'

    Returns:
        int: consumption rate for the given type
    """
    gammas = list()
    for i in range(m.shape[1]):
        ones_count = m[:, i].sum()
        zeros_count = m.shape[0] - ones_count

        # TRUTH TABLE
        #            +-----------------+-----------------+
        #            | rate != 'gamma' | rate == 'gamma' |
        # +----------+-----------------+-----------------+
        # | 1s >= 0s |               1 |               0 |
        # | 1s < 0s  |               0 |               1 |
        # +----------+-----------------+-----------------+
        if (ones_count > zeros_count) == (rate == "gamma"):
            gammas.append(1)
        else:
            gammas.append(0)

    return int_from_bin_list(gammas)


def rating(m, molecule):
    """Compute the rating value for O2 and CO2

    Args:
        m (numpy.array): 2-dimensional array of Os and 1s
        molecule (str): either 'o2' or 'co2'

    Returns:
        int: rating value
    """
    remaining = m.copy()
    for i in range(m.shape[1]):
        ones_count = remaining[:, i].sum()
        zeros_count = remaining.shape[0] - ones_count

        #            +-------------------+------------------+
        #            | molecule == 'co2' | molecule == 'o2' |
        # +----------+-------------------+------------------+
        # | 1s >= 0s |                 1 |                0 |
        # | 1s < 0s  |                 0 |                1 |
        # +----------+-------------------+------------------+
        e = int((ones_count >= zeros_count) == (molecule == "o2"))
        remaining = remaining[np.where(remaining[:, i] == e)]
        if len(remaining) == 1:
            return int_from_bin_list(remaining[0])


def part1():
    return consumption_rate(matrix, "gamma") * consumption_rate(matrix, "epsilon")


def part2():
    return rating(matrix, "o2") * rating(matrix, "co2")


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
