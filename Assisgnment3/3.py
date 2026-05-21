""" 3. Write a Python function to multiply all the numbers in a list. """

def multiplyNumberOfList(lst):
  multipltiedNumber = 1
  
  for number in lst:
    multipltiedNumber *= number
    
  print(multipltiedNumber)
    
lst = [2,3,2,2,1]
multiplyNumberOfList(lst)

