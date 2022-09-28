"""Exercise 5."""

__author__: str = "730568755"


def only_evens(xs: list[int]) -> list[int]:
    """Return the list of only even its numbers."""
    if len(xs) == 0:
        return list()
    i: int = 0
    xx: list[int] = list()
    while i < len(xs):
        if xs[i] % 2 == 0:
            xx.append(xs[i])
        i += 1
    return xx


def concat(xy: list[int], xz: list[int]) -> list[int]:
    """Combine the two lists given to the function"""
    if len(xy) == 0 and len(xz) == 0:
        return list()
    i: int = 0
    xv: list[int] = list()
    while i < len(xy):
        xv.append(xy[i])
        i += 1
    i: int = 0
    while i < len(xz):
        xv.append(xz[i])
        i += 1
    return xv


def sub(xt: list[int], start: int, end: int) -> list[int]:
    """Make a list based on the start and end indexes given"""
    xv: list[int] = list()
    if start < 0:
        start = 0
    if end > len(xt):
        end = len(xt) - 1
    if len(xt) == 0 or start > len(xt) or end <= 0:
        return list() 
    i: int = start
    while start < len(xt[i:end]):
        xv.append(xt[start])
        start += 1
    return xv
