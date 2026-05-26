"""1) Practise Pandas Series
	Create a Pandas Series from Dictionary 
	Create a Pandas Series from Lists 
	Access the elements of a Series in Pandas """

import pandas as pd

# 1) Create a Pandas Series from Dictionary
student_marks = {
    "Anmol": 90,
    "Rahul": 85,
    "Priya": 95
}

series_dict = pd.Series(student_marks)

print("Series from Dictionary:")
print(series_dict)

# 2) Create a Pandas Series from List

numbers = [10, 20, 30, 40, 50]

series_list = pd.Series(numbers)

print("\nSeries from List:")
print(series_list)

# 3) Access Elements of a Series

print("\nAccess Elements:")

# Access by index
print("First Element:", series_list[0])

# Access multiple elements
print("Elements from index 1 to 3:")
print(series_list[1:4])

# Access dictionary series element
print("Marks of Priya:", series_dict["Priya"])
