"""Practice with while loops"""

__author__ = "730767370"


def num_instances(phrase: str, search_char: str) -> int:
    """Determine how many instances of search_char are in phrase"""
    index: int = 0
    count: int = 0
    # loop through string
    while index < len(phrase):
        # update count if needed
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
