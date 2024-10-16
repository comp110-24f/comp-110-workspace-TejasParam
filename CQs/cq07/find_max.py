"""Function to determine max int in a list aand remove all instances of it"""

__author__ = "730767370"


def find_and_remove_max(nums: list[int]) -> int:
    """Find max and remove it from list"""
    if len(nums) < 1:
        return -1

    # determine initial max and update as needed
    max: int = nums[0]
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]

    # remove all instances of max
    while nums.count(max) > 0:
        nums.remove(max)

    return max
