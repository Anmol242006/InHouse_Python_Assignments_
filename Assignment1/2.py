# Input two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str3 = str1 + " " + str2

text = str3

print("\nConcatenated String:", text)

# String methods
print("\nlower():", text.lower())

print("upper():", text.upper())

print("title():", text.title())

print("swapcase():", text.swapcase())

print("capitalize():", text.capitalize())

print("casefold():", text.casefold())

print("center():", text.center(50, '*'))

print("count('l'):", text.count('l'))

print("endswith('l'):", text.endswith('l'))

print("find('l'):", text.find('l'))

print("isalnum():", text.isalnum())

print("isdigit():", text.isdigit())

print("isnumeric():", text.isnumeric())

print("isspace():", text.isspace())

print("replace('l','@'):", text.replace('l', '@'))