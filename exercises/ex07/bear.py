"""File to define Bear class."""

__author__ = "730767370"


class Bear:
    """Class to simulate bears."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize attributes."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Update age and hunger."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Update bears hunger."""
        self.hunger_score += num_fish
