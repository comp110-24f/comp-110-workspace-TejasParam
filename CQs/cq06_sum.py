"""Summing the elements of a list using a for loop"""

__author__ = "730767370"


def w_sum(vals: list[float]) -> float:
    """Sum of a list using while loop"""
    index: int = 0
    sum: float = 0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sum of a list using for loop"""
    sum: float = 0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sum of a list using for loop with range"""
    sum: float = 0
    for index in range(0, len(vals), 1):
        sum += vals[index]
    return sum
