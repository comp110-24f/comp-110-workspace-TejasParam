"""Testing find_max"""

__author__ = "730767370"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_first_use_case() -> None:
    """Testing behavior of find_and_remove_max"""
    nums: list[int] = [1, 5, 4, 6, 7, 3, 7]
    assert find_and_remove_max(nums) == 7


def test_find_and_remove_max_second_use_case() -> None:
    nums: list[int] = [1, 5, 4, 6, 7, 3, 7]
    find_and_remove_max(nums)
    assert nums == [1, 5, 4, 6, 3]


def test_find_and_remove_max_third_use_case() -> None:
    assert find_and_remove_max([-1, -2, -3, -4, -5]) == -1
