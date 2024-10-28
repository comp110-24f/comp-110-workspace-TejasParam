"""Unit tests for utils.py functions"""

__author__ = "730767370"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_case_one() -> None:
    """Test case 1 of only_evens"""
    nums: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(input=nums) == [2, 4, 6]


def test_only_evens_case_two() -> None:
    """Test case 2 only_evens"""
    nums = [-1, -2, 0]
    assert only_evens(input=nums) == [-2, 0]


def test_only_evens_case_three() -> None:
    """Test case 3 only_evens"""
    nums = [1, 2, 3, 4]
    only_evens(input=nums)
    assert nums == [1, 2, 3, 4]


def test_sub_case_one() -> None:
    """Test case 1 sub"""
    nums = [10, 20, 30, 40]
    assert sub(input_list=nums, start=1, end=3) == [20, 30]


def test_sub_case_two() -> None:
    """Test case 2 sub"""
    nums = [1, 2, 3, 4]
    assert sub(input_list=nums, start=4, end=2) == []


def test_sub_case_three() -> None:
    """Test case 3 sub"""
    nums = [10, 234, 356, 647]
    sub(input_list=nums, start=2, end=3)
    assert nums == [10, 234, 356, 647]


def test_add_at_index_case_one() -> None:
    """Test case 1 add_at_index"""
    nums = [9, 10, 12, 13]
    add_at_index(input_list=nums, element=11, index=2)
    assert nums == [9, 10, 11, 12, 13]


def test_add_at_index_raises_indexerror() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    nums = [345, 567, 234, 78, 45]
    with pytest.raises(IndexError):
        add_at_index(input_list=nums, index=-1, element=12)


def test_add_at_index_test_3() -> None:
    """Test case 3 add_at_index"""
    nums = [20, 19, 18, 16]
    add_at_index(input_list=nums, element=17, index=3)
    assert nums == [20, 19, 18, 17, 16]
