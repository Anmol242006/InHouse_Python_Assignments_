"""
9. Write a Python function that accepts a string and counts the number of upper and lower case letters."""


def checkLowerAndUpperCase(string):
  nLower = 0
  nUpper = 0
  
  for i in string:
    if(i.islower()):
      nLower +=1
    else:
      nUpper +=1
  print("Total Lower: ",nLower," and Upper: ",nUpper)
  
string = input("Enter String: ")
checkLowerAndUpperCase(string)