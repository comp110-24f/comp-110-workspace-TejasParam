"""visualize concatenation"""

__author__ = "730767370"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"

print(concat(string1=x, string2=y))
get_coords(xs=x, ys=y)
