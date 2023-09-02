import random

dice_drawing = {
    1: (
        "-----",
        "|   |",
        "| o |",
        "|   |",
        "-----",
    ),
    2: (
        "-----",
        "|o  |",
        "|   |",
        "|  o|",
        "-----",
    ),
    3: (
        "-----",
        "|o  |",
        "| o |",
        "|  o|",
        "-----",
    ),
    4: (
        "-----",
        "|o o|",
        "|   |",
        "|o o|",
        "-----",
    ),
    5: (
        "-----",
        "|o o|",
        "| o |",
        "|o o|",
        "-----",
    ),
    6: (
        "-----",
        "|o o|",
        "|o o|",
        "|o o|",
        "-----",
    ),

}


def roll_dice():

    roll = input("Roll the dice? (Yes/No): ").lower()

    while roll == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f"Dice rolled {dice1} and {dice2} is result \n")
        print("\n " .join(dice_drawing[dice1]))
        print("\n " .join(dice_drawing[dice2]))

        roll = input("Wanna roll again? (Yes/No)").lower()
    else:
        print("Ok then byeeeee")


roll_dice()
