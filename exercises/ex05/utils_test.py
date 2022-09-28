"""Exercise 5 Tests."""

__author__: str = "730568755"


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Test if inputting an empty list returns an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_two_items() -> None:
    """Test if inputting 1 odd item and 1 even item returns the even item."""
    xs: list[int] = [3, 8]
    assert only_evens(xs) == [8]


def test_only_evens_many_items() -> None:
    """Test if inputting many odd and even items returns only the evens."""
    xs: list[int] = [1, 3, 2, 7, 4, 10]
    assert only_evens(xs) == [2, 4, 10]


def test_concat_empty() -> None:
    """Test if inputting empty lists results in an empty list."""
    xy: list[int] = []
    xz: list[int] = []
    assert concat(xy, xz) == []


def test_concat_one_empty_one_full() -> None:
    """Test if the full list will concat with empty list."""
    xy: list[int] = []
    xz: list[int] = [1, 2, 3, 4]
    assert concat(xy, xz) == [1, 2, 3, 4]


def test_concat_both_full() -> None:
    """Test if second list correctly concatenates with first list."""
    xy: list[int] = [23, 45, 900]
    xz: list[int] = [321, 5, 240, 12]
    assert concat(xy, xz) == [23, 45, 900, 321, 5, 240, 12]


def test_sub_negative_start() -> None:
    """Test if given a negative start value it will start from beginning of list."""
    xt: list[int] = [1, 3, 5, 7, 9, 10]
    start: int = -32
    end: int = 4
    assert sub(xt, start, end) == [1, 3, 5, 7]


def test_sub_full_list() -> None:
    """Test if given the start value of 0 and end value of length of list it returns full list."""
    xt: list[int] = [1, 2, 3, 4, 5]
    start: int = 0
    end: int = 5
    assert sub(xt, start, end) == [1, 2, 3, 4, 5]


def test_sub_partial_list() -> None:
    """Test if given start and end values between the length of list it returns correct sublist."""
    xt: list [int] = [3, 65, 23, 12, 45]
    start: int = 1
    end: int = 3
    assert sub(xt, start, end) == [65, 23]