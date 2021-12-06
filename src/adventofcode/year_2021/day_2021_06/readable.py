# Advent of Code 2021, Day 06
# Attempting to share small, instructive, PEP8-compliant solutions!
# Any comments? Find me on:
#    - Twitter: @gansanay
#    - LinkedIn: https://linkedin.com/in/gansanay
from collections import Counter

from adventofcode.util.input_helpers import get_input_for_day_as_str

data = [int(t) for t in get_input_for_day_as_str(2021, 6).split(",")]


class Ocean:
    """An ocean ready to be filled with lantern fish

    Using a dictionary to count fishes of each age gives
    us a O(n) implementation for the two parts of the challenge.
    """

    def __init__(self, data):
        self.fishes = {k: 0 for k in range(9)}
        for k, v in dict(Counter(data)).items():
            self.fishes[k] += v

    def time_step(self):
        to_add = self.fishes[0]

        for i in range(1, 9):
            self.fishes[i - 1] = self.fishes[i]

        self.fishes[6] += to_add
        if to_add > 0:
            self.fishes[8] = to_add
        else:
            self.fishes[8] = 0

    def n_fishes(self):
        return sum(self.fishes.values())


def part1():
    ocean = Ocean(data)
    for _ in range(80):
        ocean.time_step()
    return ocean.n_fishes()


def part2():
    ocean = Ocean(data)
    for _ in range(256):
        ocean.time_step()
    return ocean.n_fishes()


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
