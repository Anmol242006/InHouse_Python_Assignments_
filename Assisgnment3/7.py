"""
7. Write a Python function to Print Even Numbers from a Given List"""


def checkEvenNumber(lst):
  for i in lst:
    if(i%2 == 0):
      print(i,end=" ")
      
lst = [2,3,3,21,3,22,2,4]
checkEvenNumber(lst)