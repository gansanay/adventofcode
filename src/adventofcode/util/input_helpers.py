import os
from typing import List

from adventofcode.config import ROOT_DIR


def get_input_for_day(year: int, day: int) -> List[str]:
    """
    Get the input for the year/day as list of strings
    """
    input_file = os.path.join(ROOT_DIR, 'inputs', str(year), f'day_{day:02}.txt')
    return _get_input(input_file)


def get_input_for_day_as_str(year: int, day: int) -> str:
    input_file = os.path.join(ROOT_DIR, 'inputs', str(year), f'day_{day:02}.txt')
    return _read_file(input_file)


def _read_lines(file_name) -> List[str]:
    """
    Reads file to list of string
    """
    with open(file_name) as file:
        lines = file.readlines()

    return lines


def _get_input(file_name) -> List[str]:
    """
    Strips new lines from input file and returns it as list of string
    """
    lines = _read_lines(file_name)
    return [line.strip() for line in lines]


def _read_file(file_name) -> str:
    """
    Reads file to string
    """
    with open(file_name) as file:
        content = file.read()

    content = content.rstrip('\n')
    return content
