"""4. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument."""

def factorial(number):
  if(number == 0):
    return 1
  return number*factorial(number-1)

number = int(input("Enter Number: "))
print(factorial(number))

