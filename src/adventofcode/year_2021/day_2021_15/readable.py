from queue import PriorityQueue

import numpy as np

from adventofcode.util.input_helpers import get_input_for_day

data = np.array(list(map(list, get_input_for_day(2021, 15)))).astype(int)

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dijkstra(arr, start, goal):
    visited = set()
    cost = {start: 0}
    parent = {start: None}
    todo = PriorityQueue()

    todo.put((0, start))
    while todo:
        while not todo.empty():
            _, vertex = todo.get()
            if vertex not in visited:
                break
        else:
            break
        visited.add(vertex)
        if vertex == goal:
            break
        for move in MOVES:
            if (
                0 <= vertex[0] + move[0] < arr.shape[0]
                and 0 <= vertex[1] + move[1] < arr.shape[1]
            ):
                neighbor = (vertex[0] + move[0], vertex[1] + move[1])
                distance = arr[neighbor]

                if neighbor in visited:
                    continue
                old_cost = cost.get(neighbor, float("inf"))
                new_cost = cost[vertex] + distance
                if new_cost < old_cost:
                    todo.put((new_cost, neighbor))
                    cost[neighbor] = new_cost
                    parent[neighbor] = vertex

    return parent


def make_path(parent, goal):
    if goal not in parent:
        return None
    v = goal
    path = []
    while v is not None:
        path.append(v)
        v = parent[v]
    return path[::-1]


def plus_one_mod_nine(arr):
    plus_one = (arr + 1) % 10
    plus_one[plus_one == 0] = 1
    return plus_one


def part1():
    goal = (data.shape[0] - 1, data.shape[1] - 1)
    parent = dijkstra(data, (0, 0), goal)
    path = make_path(parent, goal)
    return sum([data[loc] for loc in path]) - data[path[0]]


def part2():
    n, p = data.shape
    larger_data = np.zeros((5 * n, 5 * p))
    larger_data[:n, :p] = data
    for row in range(1, 5):
        larger_data[row * n : (row + 1) * n, :p] = plus_one_mod_nine(
            larger_data[(row - 1) * n : row * n, :p]
        )
    for col in range(1, 5):
        larger_data[:, col * p : (col + 1) * p] = plus_one_mod_nine(
            larger_data[:, (col - 1) * p : col * p]
        )
    larger_data = larger_data.astype(int)

    goal = (larger_data.shape[0] - 1, larger_data.shape[1] - 1)
    parent = dijkstra(larger_data, (0, 0), goal)
    path = make_path(parent, goal)
    return sum([larger_data[loc] for loc in path]) - larger_data[path[0]]


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
