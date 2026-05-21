""" 
6. Write a Python function to check whether a number falls within a given range. """


def checkNumber(number,start,end):
  if(number >= start and number <= end):
    print("Number is in the range (",start,',',end,')')
  else:
    print("number is not in range")

number = int(input("Enter Number: "))
start = int(input("Enter Starting of range: "))
end = int(input("Enter Ending of range: "))

checkNumber(number,start,end)