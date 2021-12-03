# Advent of Code 2021, Day 01
# Attempting to share small, instructive, PEP8-compliant solutions!
# Any comments? Find me on:
#    - Twitter: @gansanay
#    - LinkedIn: https://linkedin.com/in/gansanay
import numpy as np
import pandas as pd
# for the game of it, no pandas!
from itertools import groupby
import timeit  # for bragging purposes


commands = list()
with open('aoc_input_02.txt', 'r', encoding='utf-8') as f:
    for line in f.read().splitlines():
        c,v = line.split(' ')
        if c == 'up':
            commands.append(['updown', -int(v)])
        elif c == 'down':
            commands.append(['updown', int(v)])
        else:
            commands.append([c, int(v)])
commands = np.array(commands, dtype='object')

# Make it more challenging
million_commands = commands.copy()
for _ in range(99):
    million_commands = np.concatenate((million_commands, commands), axis=0)
million_commands[:, 1] = million_commands[:, 1].astype(int)


class Submarine(object):
    def __init__(self):
        self.x = 0
        self.z = 0

    def move(self, command, value):
        pass

    def move_to_last_position(commands):
        pass

    def answer(self):
        return self.x * self.z


class SubmarineWithoutAim(Submarine):
    def __init__(self):
        super().__init__()

    def move(self, command, value):
        if command == 'forward':
            try:
                self.x += int(value)
            except:
                print(command)
                print(value)
                assert False
        elif command == 'updown':
            self.z += int(value)

    def move_to_last_position(self, commands):
        values = []
        uniquekeys = []
        keyfunc = lambda x: x[0]
        for k, g in groupby(sorted(commands, key=keyfunc), keyfunc):
            values.append((np.sum([e[1] for e in g])))
            uniquekeys.append(k)
        compressed = dict(zip(uniquekeys, values))
        self.x = compressed['forward']
        self.z = compressed['updown']


class SubmarineWithAim(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def move(self, command, value):
        if command == 'forward':
            self.x += value
            self.z += self.aim * value
        elif command == 'updown':
            self.aim += value

    def move_to_last_position(self, commands):
        values = []
        uniquekeys = []
        keyfunc = lambda x: x[0]
        for k, g in groupby(commands, keyfunc):
            values.append((np.sum([e[1] for e in g])))
            uniquekeys.append(k)
        compressed = np.array(list(zip(uniquekeys, values)))
        forwards = compressed[np.where(compressed[:, 0] == 'forward'), 1][0].astype(int)
        updowns = compressed[np.where(compressed[:, 0] == 'updown'), 1][0].astype(int)
        self.x = np.sum(forwards)
        self.z = np.sum(forwards[1:]*np.cumsum(updowns))


def part1():
    s = SubmarineWithoutAim()
    for c, v in million_commands:
        s.move(c, v)
    #print(f'Solution for part 1: {s.answer()}')
    return s.answer()


def part1_bis():
    s = SubmarineWithoutAim()
    s.move_to_last_position(million_commands)
    #print(f'Solution for part 1: {s.answer()}')
    return s.answer()


def part2():
    s = SubmarineWithAim()
    for c, v in million_commands:
        s.move(c, v)
    #print(f'Solution for part 2: {s.answer()}')
    return s.answer()


def part2_bis():
    s = SubmarineWithAim()
    s.move_to_last_position(million_commands)
    #print(f'Solution for part 1: {s.answer()}')
    return s.answer()


if __name__ == "__main__":
    evals = 100
    print(f'Part 1 - Time: {timeit.timeit(part1, number=evals):.4f}s')
    print(f'Part 1 bis - Time: {timeit.timeit(part1_bis, number=evals):.4f}s')
    print(f'Part 2 - Time: {timeit.timeit(part2, number=evals):.4f}s')
    print(f'Part 2 bis - Time: {timeit.timeit(part2_bis, number=evals):.4f}s')
