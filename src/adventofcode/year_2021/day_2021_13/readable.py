import numpy as np

from adventofcode.util.input_helpers import get_input_for_day

points = np.loadtxt(get_input_for_day(2021, 13), delimiter=",", max_rows=1000).astype(
    int
)

folds = [line[11:].split("=") for line in get_input_for_day(2021, 13)[-12:]]


class Paper:
    def __init__(self, points):
        points[:, 0], points[:, 1] = points[:, 1], points[:, 0].copy()
        self.array = np.zeros((points[:, 0].max() + 1, points[:, 1].max() + 1))
        for loc in points:
            self.array[tuple(loc)] = 1
        self.folds = [self.array.copy()]

    def fold_x(self, xpos):
        arr = self.folds[-1]
        fold_down = arr[:, :xpos]
        folding_part = arr[:, -xpos:]
        folding_part_r = folding_part.T[::-1].T
        res = fold_down + folding_part_r
        return res

    def fold_y(self, ypos):
        arr = self.folds[-1]
        fold_down = arr[:ypos, :]
        folding_part = arr[-ypos:, :]
        res = fold_down + folding_part[::-1]
        return res

    def fold(self, axis, pos):
        if axis == "x":
            self.folds.append(self.fold_x(int(pos)))
        else:
            self.folds.append(self.fold_y(int(pos)))


def part1():
    p = Paper(points)
    p.fold(folds[0][0], folds[0][1])
    return len(np.where(p.folds[-1] > 0)[0])


def part2():
    p = Paper(points)
    for axis, pos in folds:
        p.fold(axis, pos)
    return p.folds[-1].astype(int)
