"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730568755"

five_char: str = input("Enter a 5-character word: " )
one_char: str = input("Enter a single character: " )

print("Searching for " + one_char + " in " + five_char)

if one_char == five_char[0]:
    print(one_char + " found at index 0")
if one_char == five_char[1]:
    print(one_char + " found at index 1")
if one_char == five_char[2]:
    print(one_char + " found at index 2")
if one_char == five_char[3]:
    print(one_char + " found at index 3")
if one_char == five_char[4]:
    print(one_char + " found at index 4")





