"""
5. Write a Python program to reverse a string."""

def reverseString(string1):
  newString = ""
  
  for i in range(len(string1)-1 ,-1,-1):
    newString += string1[i]
  print(newString)
  
string1 = input("Enter String: ")
reverseString(string1)

