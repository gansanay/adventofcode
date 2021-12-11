import numpy as np

from adventofcode.util.input_helpers import get_input_for_day

data = np.array([list(line) for line in get_input_for_day(2021, 11)]).astype(int)


class Octopuses:
    def __init__(self, arr):
        self.array = arr.copy()
        self.n_flashes = 0

    def step(self):
        self.visited = np.zeros_like(self.array)
        self.n_step_flashes = 0
        self.array += 1
        for loc in self.tens():
            self.flash(tuple(loc))
        self.array[np.where(self.array >= 10)] = 0

    def all_flashed(self):
        return self.n_step_flashes == self.array.shape[0] * self.array.shape[1]

    def tens(self):
        return np.array(np.where(self.array == 10)).T

    def can_visit(self, loc):
        return 0 <= loc[0] < self.array.shape[0] and 0 <= loc[1] < self.array.shape[1]

    def flash(self, loc):
        if not self.visited[loc]:
            self.visited[loc] = 1
            self.n_flashes += 1
            self.n_step_flashes += 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if not (dx == 0 and dy == 0):
                        visit_loc = (loc[0] + dx, loc[1] + dy)
                        if self.can_visit(visit_loc):
                            self.array[visit_loc] += 1
                            if self.array[visit_loc] > 9:
                                self.flash(visit_loc)


def part1():
    o = Octopuses(data)
    for _ in range(100):
        o.step()
    return o.n_flashes


def part2():
    o = Octopuses(data)
    n_steps = 0
    while True:
        o.step()
        n_steps += 1
        if o.all_flashed():
            break
    return n_steps


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
