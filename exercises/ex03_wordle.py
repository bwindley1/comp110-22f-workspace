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
    # This function determines if a character is whithin a certain word.


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
            if contains_char(secret, guess[i]) is True:
                box += YELLOW_BOX
            if contains_char(secret, guess[i]) is False:
                box += WHITE_BOX 
        i += 1
    return (box)
    # This function applies emojified boxes based off the contains_char function call.


def input_guess(expectedlength: int) -> str:
    """Prompt user for guess until length is correct."""
    guess: str = input(f"Enter a {expectedlength} character word: ")
    while len(guess) != expectedlength:
        guess = input(f"That wasn't {expectedlength} chars! Try again: ")
    return guess
    # This function determines if the users guess is the right length and asks for another guess if it's not.


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    won: bool = False
    turns: int = 1
    guess: str = ""
    while turns <= 6 and won is False:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            won = True
        if turns == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turns += 1
    # This function combines all the other functions above to create wordle game!


if __name__ == "__main__":
    main()