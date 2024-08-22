# SNAKE WATER GUN GAME IN PYTHON................./////////////////
import random

print("\n\t***** SNAKE WATER GUN GAME *****\n")
print("Chose Any One Option:\n1:SNAKE\n2:GUN\n3:WATER")
i = 0
j = 0
z = 0
while True:
    z = z + 1
    print()
    user = input(f"{z})Enter Your Choise:\t")
    if user == "1":
        print("\tYou Chose \"SNAKE\"")
    elif user == "2":
        print("\tYou Chose \"GUN\"")
    elif user == "3":
        print("\tYou Chose \"WATER\"")
    else:
        print("!!!!! WRONG INPUT !!!!!")
        break
    comp = random.randint(1, 3)
    if comp == 1:
        print("\tCOMPUTER CHOSE:\n", "\t", comp, "\"SNAKE\"")
    elif comp == 2:
        print("\tCOMPUTER CHOSE:\n", "\t", comp, "\"GUN\"")
    else:
        print("\tCOMPUTER CHOSE:\n", "\t", comp, "\"WATER\"")

    if user == "1" and comp == 2:
        print("\t*** YOU LOSE ***")
        i = i + 1
    elif user == "2" and comp == 3:
        print("\t*** YOU LOSE ***")
        i = i + 1
    elif user == "3" and comp == 1:
        print("\t*** YOU LOSE ***")
        i = i + 1
    elif user == "1" and comp == 3:
        print("\t*** YOU WIN ***")
        j = j + 1
    elif user == "2" and comp == 1:
        print("\t*** YOU WIN ***")
        j = j + 1
    elif user == "3" and comp == 2:
        print("\t*** YOU WIN ***")
        j = j + 1
    else:
        print("\t!!! GAME DRAW !!!")
        print("\n ***** YOUR TOTAL POINT IS:\t", j, "*****")
        print("\n ***** COMPUTER TOTAL POINT IS:\t", i, "*****")
        break
