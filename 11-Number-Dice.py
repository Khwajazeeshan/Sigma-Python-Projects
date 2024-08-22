# Make A Dice Game In Which Who Cross The point Of 100 Won This Game........////////////
import random

print("\n\t\"Press Button From (A-Z) For Rolling the Dice\"\n")

z = 0
a = 0
b = 0

while True:
    z = z + 1
    user_input = input(f"{z}) Your Turn:\t")

    if len(user_input) == 1:
        if 'A' <= user_input <= 'Z' or 'a' <= user_input <= 'z':
            user_roll = random.randint(1, 6)
        else:
            print("Input is not between 'A' and 'Z'\nPlease try again.")
            continue
    else:
        print("Invalid input\nPlease enter a single alphabetical character.")
        continue

    a = a + user_roll
    print(f"\nYour Number Is: {user_roll}\t\tYour Total Point Is: \"{a}\"")

    comp_roll = random.randint(1, 6)
    b = b + comp_roll
    print(f"Computer Number Is: {comp_roll}\tComputer Total Point Is: \"{b}\"")

    if a >= 100:
        print("\n\t!!! CONGRATULATIONS !!!\n\t***** YOU WIN THE GAME *****")
        break
    elif b >= 100:
        print("\n\t!!! SORRY !!!\n***** YOU LOSE THE GAME & COMPUTER WINS THIS GAME *****")
        break
    else:
        print("")
