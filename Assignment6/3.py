"""3)Data iteration
	Different ways to iterate over rows in Pandas Dataframe 
	Selecting rows in pandas DataFrame based on conditions 
	Select any row from a Dataframe using iloc[]
	Limited rows selection with given column
	Drop rows from the dataframe based on certain condition applied on a column 
	Insert row at given position in Pandas Dataframe 
	Create a list from rows in Pandas dataframe 
"""

import pandas as pd

data = {
    "ID": [1, 2, 3, 4],
    "Name": ["Anmol", "Rahul", "Priya", "Karan"],
    "Marks": [90, 75, 95, 60],
    "City": ["Jaipur", "Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 1) Different ways to iterate over rows

print("\nUsing iterrows():")
for index, row in df.iterrows():
    print(index, row["Name"], row["Marks"])

print("\nUsing itertuples():")
for row in df.itertuples():
    print(row.ID, row.Name, row.Marks)

# 2) Selecting rows based on conditions

print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])

# 3) Select any row using iloc[]

print("\nRow at index 2 using iloc:")
print(df.iloc[2])

# 4) Limited rows selection with given column

print("\nFirst 2 rows with Name and Marks columns:")
print(df.loc[0:1, ["Name", "Marks"]])

# 5) Drop rows based on condition

# Remove students with Marks less than 70
df_filtered = df[df["Marks"] >= 70]

print("\nDataFrame after dropping rows with Marks < 70:")
print(df_filtered)

# 6) Insert row at given position

new_row = {
    "ID": 5,
    "Name": "Simran",
    "Marks": 88,
    "City": "Chennai"
}

# Insert at index position 2
upper = df.iloc[:2]
lower = df.iloc[2:]

new_df = pd.concat([upper, pd.DataFrame([new_row]), lower]
                   ).reset_index(drop=True)

print("\nDataFrame after inserting new row:")
print(new_df)

# 7) Create list from rows in DataFrame

rows_list = df.values.tolist()

print("\nList created from DataFrame rows:")
print(rows_list)
