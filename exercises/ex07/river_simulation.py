"""Simulate river using bear, fish, and river classes."""

__author__ = "730767370"


from exercises.ex07.river import River

my_river: River = River(num_fish=10, num_bears=2)

my_river.view_river()
my_river.one_river_week()
