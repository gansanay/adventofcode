from collections import Counter
from itertools import permutations
import numpy as np

from adventofcode.util.input_helpers import get_input_for_day

datastr = get_input_for_day(2021, 8)

inputs_ = [line.split(" | ")[0] for line in datastr]
outputs_ = [line.split(" | ")[1] for line in datastr]

inputs = [line.split(" ") for line in inputs_]
outputs = [line.split(" ") for line in outputs_]

permuts = list(permutations(list("abcdefg")))

masks = [
    [True, True, True, True, True, True, False],  # 0
    [False, True, True, False, False, False, False],  # 1
    [True, True, False, True, True, False, True],  # 2
    [True, True, True, True, False, False, True],  # 3
    [False, True, True, False, False, True, True],  # 4
    [True, False, True, True, False, True, True],  # 5
    [True, False, True, True, True, True, True],  # 6
    [True, True, True, False, False, False, False],  # 7
    [True, True, True, True, True, True, True],  # 8
    [True, True, True, True, False, True, True],  # 9
]


def wordset(encoding):
    return frozenset(frozenset(np.array(list(encoding))[masks[i]]) for i in range(10))


def words(encoding):
    return dict(
        zip(
            list(frozenset(np.array(list(encoding))[masks[i]]) for i in range(10)),
            [str(k) for k in range(10)],
        )
    )


all_wordsets = dict(zip([wordset(p) for p in permuts], ["".join(p) for p in permuts]))


def get_encoding(input_line):
    """O(log n) search for the correct encoding among the 7! = 5040 permutations"""
    encoding = None
    possible_wordsets = list(all_wordsets.keys()).copy()
    for s in input_line:
        word = frozenset(s)
        possible_wordsets = [ws for ws in possible_wordsets if word in ws]
        if len(possible_wordsets) == 1:
            encoding = all_wordsets[possible_wordsets[0]]
            break
    return encoding


def part1():
    outputs_lenghts = [[len(c) for c in cols] for cols in outputs]
    c = Counter([item for sublist in outputs_lenghts for item in sublist])
    return c[2] + c[3] + c[4] + c[7]


def part2():
    values = list()
    for i in range(len(inputs)):
        input_line = inputs[i]
        output_line = outputs[i]
        output_list = list(frozenset(k) for k in output_line)
        encoding = get_encoding(input_line)
        values.append(int("".join([words(encoding)[s] for s in output_list])))
    return sum(values)


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
