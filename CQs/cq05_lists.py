"""Mutating functions"""

__author__ = "730767370"


def manual_append(list: list[int], num: int) -> None:
    """Append num to list"""
    list.append(num)


def double(list: list[int]) -> None:
    """Multiply every value in list by 2"""
    index: int = 0
    while index < len(list):
        list[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
