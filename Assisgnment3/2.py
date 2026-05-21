""" 2. Write a Python function that takes a list and returns a new list with distinct elements from the first list. """

def distinctElements(lst):
    newList = []

    for item in lst:
        if item not in newList:
            newList.append(item)

    return newList


numbers = [1,2,3,21,22,3,1,2,2,3,42,12,321,2,21]

print(distinctElements(numbers))