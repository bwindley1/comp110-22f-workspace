"""Create your own adventure exercise!"""

__author__: str = 730568755


points: int
player: str
UNC_MASCOT: str = "\U0001F40F"
CLEMSON_MASCOT: str = "\U0001F43A"
NCSU_MASCOT: str = "\U0001F405"
GT_MASCOT: str = "\U0001F41D"


def greet()-> None:
    """A message to explaine game and aquire players name."""
    global player
    print("Welcome to UNC Basketball Trivia! \nA game that will test your knowledge about various UNC Basketball stats and facts.")
    player = input("In order to continue, what name would you like to be referred to as?: ")


def normalmode()-> None:
    """One of the directions the game can take."""
    global points
    print(f"\nExcellent choice {player}! Let's start with something easy.")
    q1: str = f"What is the animal of UNC's beloved mascot? \n A. {NCSU_MASCOT}\n B. {GT_MASCOT}\n C. {UNC_MASCOT}\n D. {CLEMSON_MASCOT}\n"
    a1: str = input(f"{q1}Choose one by typing A, B, C, or D: ")
    if a1 == "C":
        points += 1
        print("Nice!")
    else: 
        print("Realllly?! Wrong!!")
    print(f"You have {points} points.")

    print("\nNow let's up the notch slightly.")
    q2: str = "How many National Championships does UNC have? \n A. 4\n B. 8\n C. 5\n D. 6\n"
    a2: str = input(f"{q2}Choose one by typing A, B, C, or D: ")
    if a2 == "D":
        points += 1
        print("Sweet!")
    else: 
        print("Lame!! Wrong!")
    print(f"You have {points} points.")

    print("\nStill to easy. Turn it up!")
    q3: str = "What jersey number did the almighty Tyler Hansbrough wear?\n A. 45\n B. 50\n C. 60\n D. 30\n"
    a3: str = input(f"{q3}Choose one by typing A, B, C, or D: ")
    if a3 == "B":
        points += 1 
        print("Solid!")
    else:
        print("Boooo! Wrong!")
    print(f"You have {points} points.")

    print("\nFinal question!")
    q4: str = "Identify the year in which UNC Did NOT win a national championship.\n A. 2005\n B. 1982\n C. 2016\n D. 1993\n"
    a4: str = input(f"{q4}Choose one by typing A, B, C, or D: ")
    if a4 == "C":
        points += 1
        print("Correct! I apologize for sparking that memory.")
    else:
        print("Seriously! You don't remember?")


def hardmode(x: int)-> int:
    """One of the directions the game can take."""
    hardpoints: str = x
    from random import randint
    print(f"\nOh so you think you're tough {player}? For choosing hardmode, you will benefit from receiving a random number of points between 1-3 for correclty answering a question!.\n")
    q1: str = "Who is the all time leader in assists at UNC? \n A. Ed Cota\n B. Phil Ford\n C. Kendall Marshall\n D. Kenny Smith\n"
    a1: str = input(f"{q1}Choose one by typing A, B, C, or D: ")
    if a1 == "A":
        hardpoints += randint(1, 3)
        print("Alright!")
    else:
        print("Incorrect!")
    print(f"You have {hardpoints} points.")

    print("\nNext one!")
    q2: str = "How many Final Four appearances does UNC have?\n A. 18\n B. 23\n C. 20\n D. 21\n"
    a2: str = input(f"{q2}Choose one by typing A, B, C, or D: ")
    if a2 == "D":
        hardpoints += randint(1, 3)
        print("Correct!")
    else:
        print("Wrong!")
    print(f"You have {hardpoints} points.")

    print("\nMoving on!")
    q3: str = "How many UNC players have been inducted into the College Basketball Hall of Fame?\n A. 2\n B. 6\n C. 4\n D. 7\n"
    a3: str = input(f"{q3}Choose one by typing A, B, C, or D: ")
    if a3 == "C":
        hardpoints += randint(1, 3)
        print("Wow! Great Job!")
    else:
        print("Sorry. Good try")
    print(f"You have {hardpoints} points.")

    print("\nFinal Question!")
    q4: str = "Where does UNC rank among other programs in all-time wins?\n A. 3rd\n B. 5th\n C. 1st\n D. 2nd\n"
    a4: str = input(f"{q4}Choose one by typing A, B, C, or D: ")
    if a4 == "A":
        hardpoints += randint(1, 3)
        print("You know your stuff!")
    else:
        print("Wrong!")
    return hardpoints


def gameloop() -> None:
    """Gives player a choice to keep playing or quit."""
    print("\nCongrats on completeing a run through of UNC Basketball Trivia!")
    global points
    playing: bool = True
    while playing == True:
        mode: str = input("\nIf you would like to stop playing, type 'Neither'. If you wish to continue to hardmode, type 'Hard'. If you wish to continue to normalmode, type 'Normal': ")
        if mode == "Normal":
            normalmode()
            print(f"\nYou have {points} points!")
        if mode == "Hard":
            points = hardmode(points)
            print(f"\nYou have {points} points!")
        if mode == "Neither":
            print(f"\nWell {player}, this concludes your game. You ended with {points} points!")
            playing = False


def main()-> None:
    """Function holding all the elements of game."""
    greet()
    print(f"\nGreat! So {player}, we have two different modes for you to choose from. If you consider yourself a UNC Basketball connoisseur we have a hard mode. Otherwise if your not sure of your skills, you can stick with our normal mode. If your not interested in the game you can defer.")
    mode: str = input("Type Hard, Normal, or Neither to choose: ")
    global points
    points = 0
    if mode == "Hard":
        points = hardmode(points)
        print(f"\nYou have {points} points!")
        gameloop()
    if mode == "Normal":
        normalmode()
        print(f"\nYou have {points} points!")
        gameloop()
    if mode == "Neither":
        print(f"Well {player}, this concludes your game. You ended with {points} points!")
        exit()


if __name__ == "__main__":
    main()