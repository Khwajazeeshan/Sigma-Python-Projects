# Table of any number By Using For and While Loop............!!!!!!!!!!!!!

print("\n*****Enter a Table Number:*****\n ")
a = int(input())
print("\n***Enter the limit of Table:***\n")
b = int(input())
i = 1
while i <= b:
    print("\n ", a, "*", i, "=", a * i, )
    i = i + 1
print()

for i in range(b):
    print(a, "*", i + 1, "=", a * (i + 1))
    
