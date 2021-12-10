import numpy as np

from adventofcode.util.input_helpers import get_input_for_day

data = get_input_for_day(2021, 10)

openers = "[{(<"
closers = "]})>"

PENALTIES = {")": 3, "]": 57, "}": 1197, ">": 25137}

COMPLETION = {")": 1, "]": 2, "}": 3, ">": 4}


def check(inp):
    stack = []
    penalty = 0
    autocomplete = 0
    for i in inp:
        if i in openers:
            stack.append(i)
        elif i in closers:
            pos = closers.index(i)
            if (len(stack) > 0) and (openers[pos] == stack[-1]):
                stack.pop()
            else:
                penalty = PENALTIES[i]
                return ["Illegal", penalty]
    if len(stack) == 0:
        return ["Complete", 0]
    else:
        for i in stack[::-1]:
            autocomplete *= 5
            pos = openers.index(i)
            autocomplete += COMPLETION[closers[pos]]
        return ["Incomplete", autocomplete]


def part1():
    penalty = 0
    for line in data:
        r, p = check(line)
        if r == "Illegal":
            penalty += p
    return penalty


def part2():
    autocomplete = list()
    for line in data:
        r, p = check(line)
        if r == "Incomplete":
            autocomplete.append(p)
    return int(np.median(autocomplete))


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
