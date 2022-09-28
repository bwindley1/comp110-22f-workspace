"""Exercise 5 Tests."""

__author__: str = "730568755"


from exercises.ex05.utils import only_evens, concat


def test_only_evens_empty() -> None:
    """Test if inputting an empty list returns an empty list."""
    xs: list[int] = []
    assert only_evens([]) == []


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