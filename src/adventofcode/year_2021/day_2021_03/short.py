# Advent of Code 2021, Day 03
# Attempting to share small, instructive, PEP8-compliant solutions!
# Any comments? Find me on:
#    - Twitter: @gansanay
#    - LinkedIn: https://linkedin.com/in/gansanay
import numpy as np

from adventofcode.util.input_helpers import get_input_for_day

data = np.loadtxt(get_input_for_day(2021, 3), dtype='str')
matrix = np.array([list(e) for e in data]).astype(int)


def int_from_bin_list(lst):
    return int("".join(str(x) for x in lst), 2)


def consumption_rate(m, rate):
    gammas = [int((m[:, i].sum() > m.shape[0]-m[:, i].sum()) == (rate == 'gamma'))
              for i in range(m.shape[1])]
    return int_from_bin_list(gammas)


def rating(m, molecule):
    rest = m.copy()
    for i in range(m.shape[1]):
        ones_count = rest[:, i].sum()
        zeros_count = rest.shape[0]-ones_count
        e = int((ones_count >= zeros_count) == (molecule == 'o2'))
        rest = rest[np.where(rest[:, i] == e)]
        if len(rest) == 1:
            return int_from_bin_list(rest[0])


def part1():
    return consumption_rate(matrix, 'gamma') * consumption_rate(matrix, 'epsilon')


def part2():
    return rating(matrix, 'o2') * rating(matrix, 'co2')


if __name__ == '__main__':
    print(f'Solution for part 1: {part1()}')
    print(f'Solution for part 2: {part2()}')
