# Advent of Code 2021, Day 02
# Attempting to share small, instructive, PEP8-compliant solutions!
# Any comments? Find me on:
#    - Twitter: @gansanay
#    - LinkedIn: https://linkedin.com/in/gansanay

commands = list()
with open("aoc_input_02.txt", "r", encoding="utf-8") as f:
    for line in f.read().splitlines():
        c, v = line.split(" ")
        # ups and downs are just doing the same thing with opposite signs
        if c == "up":
            commands.append(["updown", -int(v)])
        elif c == "down":
            commands.append(["updown", int(v)])
        else:
            commands.append([c, int(v)])


class Submarine(object):
    """Abstraction for a submarine

    It's only defined by its original position and how we compute the answer.
    """

    def __init__(self):
        self.x = 0
        self.z = 0

    def answer(self):
        """Give the answer to the challenge (horizontal position x depth)

        Returns:
            int: The answer
        """
        return self.x * self.z


class SubmarineWithoutAim(Submarine):
    """A special submarine that moves following commands, without an aim."""

    def __init__(self):
        super().__init__()

    def move(self, command, value):
        """Move the submarine according to the command type and its value

        Args:
            command (str): The command given to the submarine, either 'forward' or 'updown'
            value (int): The number of space units to use for the command
        """
        if command == "forward":
            self.x += value
        elif command == "updown":
            self.z += value


class SubmarineWithAim(Submarine):
    """A special submarine, the moves of which depend on its changing aim."""

    def __init__(self):
        super().__init__()
        self.aim = 0

    def move(self, command, value):
        """Move the submarine according to the command type and its value, using the aim

        Args:
            command (str): The command given to the submarine, either 'forward' or 'updown'
            value (int): The number of space units to use for the command
        """
        if command == "forward":
            self.x += value
            self.z += self.aim * value
        elif command == "updown":
            self.aim += value


def part1():
    s = SubmarineWithoutAim()
    for c, v in commands:
        s.move(c, v)
    print(f"Solution for part 1: {s.answer()}")


def part2():
    s = SubmarineWithAim()
    for c, v in commands:
        s.move(c, v)
    print(f"Solution for part 2: {s.answer()}")
