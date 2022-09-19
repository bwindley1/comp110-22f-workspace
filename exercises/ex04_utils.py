"""ex_04 'list' Utility Functions."""

__author__: str = "730568755"


def all(list: list[int], number: int) -> bool:
    """Find if list contains only one number."""
    i: int = 0
    while i < len(list):
        if number != list[i]:
            return False
        i += 1
    if len(list) == 0:
        return False
    return True


def max(input: list[int]) -> int:
    """Find the largest value in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1
    largest: int = input[0]
    while i < len(input):
        if largest < input[i]:
            largest = input[i]
        i += 1
    return largest


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Determine if values in both lists are equal to each other."""
    i: int = 0
    while i < len(first_list and second_list):
        if first_list[i] != second_list[i]:
            return False
        i += 1
    if len(first_list) != len(second_list):
        return False
    return True