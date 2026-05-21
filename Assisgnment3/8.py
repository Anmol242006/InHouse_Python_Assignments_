"""
  8.Write a Python function that takes a number as a parameter and checks whether the number is prime or not."""


def checkPrimeNumber(number):

    if number <= 1:
        print(number, "is not a prime number")
        return

    flag = 0

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            flag = 1
            break

    if flag == 1:
        print(number, "is not a prime number")
    else:
        print(number, "is a prime number")


number = int(input("Enter Number: "))

checkPrimeNumber(number)