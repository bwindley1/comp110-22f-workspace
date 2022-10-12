"""Exercise 7 Dictionary Functions!"""

__author__: str = "730568755"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary."""
    result: dict[str, str] = {} 
    if len(x) == 0:
        return {}
    for key in x:
        if x[key] in result:
            raise KeyError("Can't have two of the same keys.")
        result[x[key]] = key
    return result


def favorite_color(y: dict[str, str]) -> str:
    """Return the color that appears most frequently."""
    color: str = ""
    counter: dict[str, int] = {}
    if len(y) == 0:
        return {}
    for key in y:
        if y[key] in counter:
            counter[y[key]] += 1
        else:
            counter[y[key]] = 1
    maximum: int = 0
    for item in counter:
        if maximum < counter[item]:
            maximum = counter[item]
            color = item 
    return color


def count(xs: list[str]) -> dict[str, int]:
    """Return a dict with key as unique value and value as the number of time it appeared."""
    result: dict[str, int] = {}
    if len(xs) == 0:
        return {}
    for item in xs:
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result