"""Dictionary Function Tests for Ex07!"""

__author__: str = "730568755"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Test if inputting empty list returns empty list."""
    x: dict[str, str] = {}
    assert invert(x) == {}


def test_invert_key_value() -> None:
    """Test if given a key and a value it flips them."""
    x: dict[str, str] = {"cow": "cat"}
    assert invert(x) == {"cat": "cow"}


def test_invert_multiple_key_value() -> None:
    """Test if given multiple items in a dict it flips the keys and values."""
    x: dict[str, str] = {"purple": "yellow", "green": "blue"}
    assert invert(x) == {"yellow": "purple", "blue": "green"}


def test_count_empty() -> None:
    """Test if given a empty list it will return an empty dictionary."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_single() -> None:
    """Test if given one item in a list it returns a dict containing the item and value 1."""
    xs: list[str] = ["cow"]
    assert count(xs) == {"cow": 1}


def test_count_multiple() -> None:
    """Test if given multiple items it returns the items as keys and the amount of times it's in the list as the value."""
    xs: list[str] = ["cow", "tow", "row", "cow", "row"]
    assert count(xs) == {"cow": 2, "tow": 1, "row": 2}


def test_favorite_color_empty() -> None:
    """Test if given a empty dict it returns an empty dict."""
    y: dict[str, str] = {}
    assert favorite_color(y) == {}


def test_favorite_color_majority() -> None:
    """Test if given a dict of favorite colors it returns the color that was chosen the most."""
    y: dict[str, str] = {"Bob": "yellow", "Job": "blue", "Hob": "green", "Kob": "blue"}
    assert favorite_color(y) == "blue"


def test_favorite_color_tie() -> None:
    """Test if given equally amount of favorite colors it returns the color that appeared first."""
    y: dict[str, str] = {"Bob": "green", "Job": "yellow", "Cob": "blue"}
    assert favorite_color(y) == "green"