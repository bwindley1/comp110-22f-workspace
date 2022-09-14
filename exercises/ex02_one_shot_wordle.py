"""One Shot Wordle Exercise."""

__author__ = "730568755"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
# depending on the length of the secret word the input will ask for that length guess
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
match: int = 0
box: str = ""

while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")
# if the length of guess is incorrect it will ask for a new input while changing the new input to the current guess.

if len(guess) == len(secret):
    # if guess is correct length it will go into long then block
    while match < len(secret):
        if guess[match] == secret[match]:
            box += GREEN_BOX
# if guess index 0 is equal to secret index 0 it will concatenate green block
        if guess[match] != secret[match]:
            # if index 0 of guess is not equal to secret index 0 it will go into while loop
            char_exists: bool = False
            alternate: int = 0
            while not char_exists and alternate < len(secret):
                # if both expressions are True it will go into while loop to search if guess index 0 character is within any index of secret
                if guess[match] == secret[alternate]:
                    char_exists = True
                alternate += 1   
# if index 0 of guess is equal to index 0 of secret then char_exists becomes True which cancels the while loop but still incremates alternate by 1.
            if char_exists:
                box += YELLOW_BOX 
# if char_exists is True it will concatenate a yellow block.
            else:
                box += WHITE_BOX
# if char_exists is False it will concatenate a white block.
        match += 1

print(box)

if guess == secret:
    print("Woo! You got it!")
# if guess is right, wooooo!!! you win!!
else:
    print("Not quite. Play again soon!")
# if guess is wrong, boooo!!! you lose!!