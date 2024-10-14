"""Function utilities"""

__author__ = "730767370"


def all(numbers: list[int], check_int: int) -> bool:
    """Check if all numbers in list are same as given int"""

    if len(numbers) == 0:
        return False

    # check each element
    for x in numbers:
        if x != check_int:
            return False
    return True


def max(input: list[int]) -> int:
    """Determine max value of a list"""

    # check if length is valid
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    max: int = input[0]

    # update max if needed
    for x in input:
        if x > max:
            max = x
    return max


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Determine if two lists are equal"""
    # check if lengths are the same
    if len(input1) != len(input2):
        return False

    # check if each index has same element
    for i in range(len(input1)):
        if input1[i] != input2[i]:
            return False
    return True


def extend(input1: list[int], input2: list[int]) -> None:
    """Add items from one list on to another"""
    # append each item from second list to first list
    for i in input2:
        input1.append(i)
