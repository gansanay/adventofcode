# Advent of Code 2021, Day 03
# Attempting to share small, instructive, PEP8-compliant solutions!
# Any comments? Find me on:
#    - Twitter: @gansanay
#    - LinkedIn: https://linkedin.com/in/gansanay
import numpy as np

from adventofcode.util.input_helpers import get_input_for_day_as_str


class Board(object):
    """A Bingo board to play with the giant squid around the submarine

    Args:
        board_array (numpy.array): 2D array representing the initial board configuration
    """

    def __init__(self, board_array):
        self.board_array = board_array
        self.hits_array = np.zeros_like(self.board_array)
        self.latest_hit = None

    def hit_num(self, picked):
        """Hit the picked number if it exists in the board

        Args:
            picked (int): picked number
        """
        hit_location = np.where(self.board_array == picked)
        if len(hit_location[0]) > 0:
            self.hits_array[hit_location] = 1
            self.latest_hit = picked

    def has_won(self):
        """Check if the current board position is a winning one

        Returns:
            bool: True if the board has won
        """
        return (self.hits_array.sum(axis=0).max() == self.hits_array.shape[1]) | (
            self.hits_array.sum(axis=1).max() == self.hits_array.shape[0]
        )

    def unmarked_sum(self):
        return (self.board_array * (1 - self.hits_array)).sum()

    def score(self):
        return self.unmarked_sum() * self.latest_hit


class Game(object):
    """A game of Bingo"""

    def __init__(self):
        input_str = get_input_for_day_as_str(2021, 4)
        self.picked_nums = [
            int(k) for k in input_str.split("\n\n")[0].strip().split(",")
        ]
        rest = input_str.split("\n\n")[1:]
        input_boards = np.array(
            [[row.split() for row in board.split("\n")] for board in rest]
        ).astype(int)

        self.played_boards = list()
        for b in input_boards:
            self.played_boards.append(Board(b))

        self.winning_boards_scores = list()

    def run(self, verbose=False):
        for num in self.picked_nums:
            for i, board in enumerate(self.played_boards):
                board.hit_num(num)
                if board.has_won():
                    if verbose:
                        print(
                            f"Winning board {i}! Score: {board.score()}. {len(self.played_boards) - 1} remaining"
                        )
                    self.winning_boards_scores.append(board.score())
                    self.played_boards.pop(i)

    def first_winner_score(self):
        return self.winning_boards_scores[0]

    def last_winner_score(self):
        return self.winning_boards_scores[-2]


def part1():
    g = Game()
    g.run()
    return g.first_winner_score()


def part2():
    g = Game()
    g.run()
    return g.last_winner_score()


if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
