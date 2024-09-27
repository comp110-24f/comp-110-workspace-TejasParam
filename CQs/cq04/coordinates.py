"""Coordinates of Strings"""

__author__ = "730767370"


def get_coords(xs: str, ys: str) -> None:
    """Print all combinations of characters from 2 strings"""
    i: int = 0
    while i < len(xs):
        j: int = 0
        while j < len(ys):
            print("(", xs[i], ",", ys[j], ")")
            j += 1
        i += 1
