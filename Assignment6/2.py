"""2) DataFrames
	Make a Pandas DataFrame with a two-dimensional Python list 
	Create DataFrame from Python dict 
	Create Pandas dataframe using list of lists 
	Create a Pandas dataframe using list of tuples 
	Create a Pandas DataFrame from List of Dicts"""

import pandas as pd
# 1) Make a Pandas DataFrame with a 2D List
data_2d = [
    [1, "Anmol", 21],
    [2, "Rahul", 22],
    [3, "Priya", 20]
]

df_2d = pd.DataFrame(data_2d, columns=["ID", "Name", "Age"])

print("DataFrame from 2D List:")
print(df_2d)


# 2) Create DataFrame from Python Dictionary

data_dict = {
    "Name": ["Anmol", "Rahul", "Priya"],
    "Age": [21, 22, 20],
    "City": ["Jaipur", "Delhi", "Mumbai"]
}

df_dict = pd.DataFrame(data_dict)

print("\nDataFrame from Dictionary:")
print(df_dict)


# 3) Create DataFrame using List of Lists


list_of_lists = [
    ["Math", 90],
    ["Science", 85],
    ["English", 88]
]

df_list = pd.DataFrame(list_of_lists, columns=["Subject", "Marks"])

print("\nDataFrame from List of Lists:")
print(df_list)


# 4) Create DataFrame using List of Tuples

list_of_tuples = [
    ("Laptop", 50000),
    ("Mobile", 20000),
    ("Tablet", 15000)
]

df_tuples = pd.DataFrame(list_of_tuples, columns=["Product", "Price"])

print("\nDataFrame from List of Tuples:")
print(df_tuples)


# 5) Create DataFrame from List of Dictionaries


list_of_dicts = [
    {"Name": "Anmol", "Marks": 90},
    {"Name": "Rahul", "Marks": 85},
    {"Name": "Priya", "Marks": 95}
]

df_dicts = pd.DataFrame(list_of_dicts)

print("\nDataFrame from List of Dictionaries:")
print(df_dicts)
