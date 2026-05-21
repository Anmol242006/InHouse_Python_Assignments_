"""1. Write a Python function to find the maximum of three numbers."""


def greatestNumber(a, b, c):
    if a >= b and a >= c:
        print(a, "is the greatest")
    elif b >= a and b >= c:
        print(b, "is the greatest")
    else:
        print(c, "is the greatest")


a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
c = int(input("Enter third Number: "))

greatestNumber(a, b, c)