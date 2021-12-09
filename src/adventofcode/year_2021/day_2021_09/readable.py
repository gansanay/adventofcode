from operator import mul
from functools import reduce

import numpy as np

from adventofcode.util.input_helpers import get_input_for_day

arr = np.array([list(line) for line in get_input_for_day(2021, 9)]).astype(int)

MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Array:
    def __init__(self, arr):
        self.array = arr

    def get_val(self, i, j):
        if 0 <= i < self.array.shape[0] and 0 <= j < self.array.shape[1]:
            return self.array[i, j]
        else:
            return np.inf

    def min_adj(self, i, j):
        lower = all(
            self.get_val(i + move[0], j + move[1]) > self.array[i, j] for move in MOVES
        )
        if lower:
            return self.array[i, j] * lower
        else:
            return -1

    def sum_local_min(self):
        s = list()
        for i in range(self.array.shape[0]):
            for j in range(self.array.shape[1]):
                m = self.min_adj(i, j)
                if m >= 0:
                    s.append(1 + m)
        return sum(s)

    def can_visit(self, row, col):
        rows, cols = self.array.shape

        return (0 <= row < rows) and (0 <= col < cols) and (self.visited[row][col] != 1)

    def DFS(self, row, col):
        self.visited[row][col] = 1

        n_visits = 1
        for move in MOVES:
            if self.can_visit(row + move[0], col + move[1]):
                n_visits += self.DFS(row + move[0], col + move[1])
        return n_visits

    def connected_components(self):
        connected = list()

        self.visited = np.zeros_like(self.array)
        self.visited[np.where(arr == 9)] = 1

        for i in range(self.array.shape[0]):
            for j in range(self.array.shape[1]):
                if not self.visited[i, j]:
                    connected.append(self.DFS(i, j))

        return connected


def part1():
    a = Array(arr)
    return a.sum_local_min()


def part2():
    a = Array(arr)
    basins_sizes = a.connected_components()
    return reduce(mul, sorted(basins_sizes)[-3:], 1)


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
