# Guess The Number Game Between User And Computer.........//////////
import random

print("\n\t***~~~YOUR NUMBER SHOULD BE BETWEEN (1-1000)~~~***")

while True:
    user = int(input("\nEnter Your Number:\t"))
    if 0 < user <= 1000:
        comp = int(random.randint(1, 1000))
        print(f"Computer Number IS:\t{comp}")
        if user < comp:
            print("\n\t*****Your Number Is Less than Computer Number*****")
        elif user > comp:
            print("\n\t*****Your Number Is Higher than Computer Number*****")
        else:
            print("\n\t*****Both Numbers Are Equals*****")
    else:
        print("\nYOUR NUMBER SHOULD BE BETWEEN (1-1000)\n\t***Try Again***")