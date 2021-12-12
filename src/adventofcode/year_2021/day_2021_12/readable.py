import numpy as np

from adventofcode.util.input_helpers import get_input_for_day

data = [line.split("-") for line in get_input_for_day(2021, 12)]


class Caves:
    def __init__(self):
        self.remaining_visits = dict()
        self.graph = dict()
        self.path_count = 0
        self.small_caves = set()
        self.paths = set()

    def add_tunnel(self, edge):
        for n in edge:
            if n not in self.graph.keys():
                self.graph[n] = list()
                if n.isupper():
                    self.remaining_visits[n] = np.inf
                else:
                    if n not in ["start", "end"]:
                        self.small_caves.add(n)
                    self.remaining_visits[n] = 1

        self.graph[edge[0]].append(edge[1])
        self.graph[edge[1]].append(edge[0])

    def reset(self):
        self.path_count = 0
        for k in self.remaining_visits.keys():
            if k in self.small_caves:
                self.remaining_visits[k] = 1

    def get_paths_part1(self, verbose=False):
        self.print_all_paths_from_to("start", "end", verbose=verbose)
        return self.path_count

    def get_paths_part2(self, verbose=False):
        s = 0
        for cave in self.small_caves:
            self.reset()
            self.remaining_visits[cave] = 2
            self.print_all_paths_from_to("start", "end", verbose=verbose)
            s += self.path_count
        return s

    def print_all_paths_from_to(self, u, d, path=list(), verbose=False):
        vis = self.remaining_visits[u]
        self.remaining_visits[u] -= 1
        path.append(u)

        if u == d:
            if tuple(path) not in self.paths:
                if verbose:
                    print(path)
                self.paths.add(tuple(path))
                self.path_count += 1
        else:
            for i in self.graph[u]:
                if self.remaining_visits[i] > 0:
                    self.print_all_paths_from_to(i, d, path=path, verbose=verbose)

        path.pop()
        self.remaining_visits[u] = vis


def part1():
    c = Caves()
    for tunnel in data:
        c.add_tunnel(tunnel)
    return c.get_paths_part1()


def part2():
    c = Caves()
    for tunnel in data:
        c.add_tunnel(tunnel)
    return c.get_paths_part2()


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
