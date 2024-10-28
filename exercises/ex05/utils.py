"""Function utilities"""

__author__ = "730767370"


def only_evens(input: list[int]) -> list[int]:
    """Determine even values of a list"""
    new_list: list[int] = []
    for i in input:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


def sub(input_list: list[int], start: int, end: int) -> list[int]:
    """Return sublist based on given indices"""
    if start < 0:
        start = 0
    if end > len(input_list):
        end = len(input_list)
    if len(input_list) == 0 or start > end or end <= 0:
        return []
    new_list: list[int] = []
    for i in range(start, end):
        new_list.append(input_list[i])
    return new_list


def add_at_index(input_list: list[int], element: int, index: int) -> None:
    """Add element to list at specific index"""
    if index < 0 or index > len(input_list):
        raise IndexError("Index is out of bounds for the input list")
    input_list.append(element)
    i: int = len(input_list) - 1
    while i > index:
        input_list[i] = input_list[i - 1]
        i -= 1
    input_list[index] = element
