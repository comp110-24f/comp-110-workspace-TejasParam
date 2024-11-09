"""File to define Fish class."""

__author__ = "730767370"


class Fish:
    """Class to simulate Fish."""

    age: int

    def __init__(self):
        """Initialize Fish attributes."""
        self.age = 0

    def one_day(self):
        """Increase age by 1."""
        self.age += 1
