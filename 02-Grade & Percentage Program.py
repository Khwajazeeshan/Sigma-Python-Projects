# Find Percentage And Grade Program.......Using for And  While Loop And If Else Statement.....!!!!!

# i = 0
# while i <= 5:
for i in range(5):
    print("\n***Enter your marks***\n")
    a = int(input())
    if a < 0:
        print("You Enter Wrong Number....!!!!!!\nPlease Try Again!!!")
    elif a <= 400:
        print("You Fail\nYour Percentage is 33%\nYour Grade Is F ")
    elif 401 <= a <= 500:
        print("Congratulations!!! You Pass\nYour Percentage is 45%\nYour Grade Is D")
    elif 501 <= a <= 600:
        print("Congratulations!!! You Pass\nYour Percentage is 55%\nYour Grade Is C")
    elif 601 <= a <= 700:
        print("Congratulations!!! You Pass\nYour Percentage is 65%\nYour Grade Is C+")
    elif 701 <= a <= 800:
        print("Congratulations!!! You Pass\nYour Percentage is 75%\nYour Grade Is B")
    elif 801 <= a <= 950:
        print("Congratulations!!! You Pass\nYour Percentage is 85%\nYour Grade Is B+")
    elif 951 <= a <= 1050:
        print("Congratulations!!! You Pass\nYour Percentage is 95%\nYour Grade Is A")
    elif 1051 <= a <= 1100:
        print("Congratulations!!! You Pass\nYour Percentage is 100%\nYour Grade Is A+")
    else:
        print("Your Number is Greater then Total Number!!!\nPlease Try Again...!!!")
    print(4)
    # i = i + 1
