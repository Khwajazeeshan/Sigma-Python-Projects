# STONE PAPER SCISSOR GAME IN PYTHON................./////////////////
import random

print("\n\t***** STONE PAPER SCISSOR GAME *****\n")
print("Chose Any One Option:\n1:STONE\n2:PAPER\n3:SCISSOR")
i = 0
j = 0
z = 0
while True:
    z = z + 1
    print()
    user = input(f"{z})Enter Your Choise:\t")
    if user == "1":
        print("\tYou Chose \"STONE\"")
    elif user == "2":
        print("\tYou Chose \"PAPER\"")
    elif user == "3":
        print("\tYou Chose \"SCISSOR\"")
    else:
        print("!!!!! WRONG INPUT !!!!!")
        break
    comp = random.randint(1, 3)
    if comp == 1:
        print("\tCOMPUTER CHOSE:\n", "\t", comp, "\"STONE\"")
    elif comp == 2:
        print("\tCOMPUTER CHOSE:\n", "\t", comp, "\"PAPER\"")
    else:
        print("\tCOMPUTER CHOSE:\n", "\t", comp, "\"SCISSOR\"")

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
