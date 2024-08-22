# simple Calculator Using Match Case Statement And If Else Statement..................!!!!!!
print('\nThis Is My First Program In Python: \nSimple Calculator In Python:\n\n')

print("Enter two numbers:\n")
a = int(input())
b = int(input())

print("enter operator")
c = input()

# By Using Match Case......
match c:
    case "+":
        print("the sum of these number is ", a + b)
    case "-":
        print("the subtraction of these number is ", a - b)
    case "%":
        print("the modulus of these number is ", a % b)
    case "/":
        print("the division of these number is ", a / b)
    case "*":
        print("the multiplication of these number is ", a * b)
    case _:
        print("Wrong Operator")

# By Using If_else Statement.....

if c == "+":
    print("the sum of these number is ", a + b)
elif c == "-":
    print("the subtraction of these number is ", a - b)
elif c == "*":
    print("the multiplication of these number is ", a * b)
elif c == "/":
    print("the division of these number is ", a / b)
elif c == "%":
    print("the modulus of these number is ", a % b)
else:
    print("Wrong operator")
