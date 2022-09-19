"""Example implementing a list utility function."""

# Function named contains
# We will have 2 parameters: needle (str), haystack (list[str])
# Return type bool
def contains(needle: str, haystack: list[str]) -> bool:

# Gameplan:
# 1. Start with the first index
    i: int = 0
# 2. Loop through every index
    while i < len(haystack):
        #   2.A Test if item at index equal to needle
        if haystack[i] == needle:
            return True
        #   2.A True return True! We found it!
        i += 1
# 3. Return False
    return False
