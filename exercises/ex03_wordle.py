"""EX03 - Structured Wordle."""

__author__ = "730568755"


def contains_char(word: str, char: str) -> bool:
    """Finds character whithin indicies."""
    assert len(char) == 1
    i: int = 0
    char_exists: bool = False
    while not char_exists and i < len(word):
        if word[i] == char:
            char_exists = True
        if word[i] != char:
            char_exists = False
        i += 1
    if char_exists:
        return True
    else:
        return False

def emojified(guess: str, secret: str) -> str:
    """Apply a emoji based off contains_char bools."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    box: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            box += GREEN_BOX
        if guess[i] != secret[i]:
            contains_char(secret, guess[i])
            if contains_char(secret, guess[i]) == True:
                box += YELLOW_BOX
            if contains_char(secret, guess[i]) == False:
                box += WHITE_BOX 
        i += 1
    return(box)