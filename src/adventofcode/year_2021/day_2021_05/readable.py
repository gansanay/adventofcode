import numpy as np

from adventofcode.util.input_helpers import get_input_for_day

data = get_input_for_day(2021, 5)
segments = np.array(
    [[pair.split(",") for pair in line.split(" -> ")] for line in data]
).astype(int)

xmax = segments[:, :, 0].max()
ymax = segments[:, :, 1].max()


class Line:
    def __init__(self):
        self.line = None


class StraightLine(Line):
    def __init__(self, coords):
        self.line = list()
        x_coords = (coords[0, 0], coords[1, 0])
        y_coords = (coords[0, 1], coords[1, 1])
        for x in range(min(x_coords), 1 + max(x_coords)):
            for y in range(min(y_coords), 1 + max(y_coords)):
                self.line.append([x, y])


class DiagonalLine(Line):
    def __init__(self, coords):
        self.line = list()
        x_coords = (coords[0, 0], coords[1, 0])
        y_coords = (coords[0, 1], coords[1, 1])
        delta_x = 1 if x_coords[1] > x_coords[0] else -1
        delta_y = 1 if y_coords[1] > y_coords[0] else -1
        for i in range(1 + abs(x_coords[1] - x_coords[0])):
            self.line.append([x_coords[0] + i * delta_x, y_coords[0] + i * delta_y])


class Board:
    def __init__(self, limits):
        self.limits = limits
        self.board = np.zeros((limits[0], limits[1]), dtype=int)

    def draw_line(self, line):
        for location in line.line:
            self.board[location[0], location[1]] += 1

    def overlaps(self):
        return len(np.where(self.board > 1)[0])


def part1():
    board = Board((1 + xmax, 1 + ymax))
    for seg in segments:
        if seg[0, 0] == seg[1, 0] or seg[0, 1] == seg[1, 1]:
            line = StraightLine(seg)
            board.draw_line(line)
    return board.overlaps()


def part2():
    board = Board((1 + xmax, 1 + ymax))
    for seg in segments:
        line = None
        if seg[0, 0] == seg[1, 0] or seg[0, 1] == seg[1, 1]:
            line = StraightLine(seg)
        else:
            line = DiagonalLine(seg)
        board.draw_line(line)
    return board.overlaps()


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
