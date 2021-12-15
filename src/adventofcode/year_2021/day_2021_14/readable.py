from collections import Counter

from adventofcode.util.input_helpers import get_input_for_day

data_str = get_input_for_day(2021, 14)
polymer_template = data_str[0]
insertions = dict([line.split(" -> ") for line in data_str[2:]])


def poly_element_count(template, insertions, iterations=10):
    element_counts = Counter(template)
    pair_counts = Counter(template[i : i + 2] for i in range(len(template) - 1))
    for _ in range(iterations):
        pair_counts_new = Counter()
        for pair, n in pair_counts.items():
            p1, p2 = pair
            insert = insertions[pair]
            pair_counts_new[p1 + insert] += n
            pair_counts_new[insert + p2] += n
            element_counts[insert] += n
        pair_counts = pair_counts_new

    return element_counts


def part1():
    c = poly_element_count(polymer_template, insertions)
    return max(list(c.values())) - min(list(c.values()))


def part2():
    c = poly_element_count(polymer_template, insertions, iterations=40)
    return max(list(c.values())) - min(list(c.values()))


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
