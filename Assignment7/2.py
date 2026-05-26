"""2)Create two DataFrames, df1 and df2, with a common column (e.g., 'ID'). 

>Perform an inner merge on this common column and display the resulting DataFrame.
>Perform a left join of df1 and df2 on the 'ID' column. Explain how missing values are handled in the resulting DataFrame. Right Join and Index-Based Join.
>Perform a right join using pd.merge() on a common column, then perform a join using df.join() based on the index. Compare the results. Merging with Multiple Keys.

"""

import pandas as pd

# Create first DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Anmol', 'Riya', 'Karan', 'Simran']
})

# Create second DataFrame
df2 = pd.DataFrame({
    'ID': [2, 3, 4, 5],
    'Marks': [85, 90, 78, 88]
})

print("DataFrame df1:")
print(df1)

print("\nDataFrame df2:")
print(df2)


# INNNER JOIN

inner_merge = pd.merge(df1, df2, on='ID', how='inner')

print("\nInner Merge Result:")
print(inner_merge)


# LEFT JOIN

left_join = pd.merge(df1, df2, on='ID', how='left')

print("\nLeft Join Result:")
print(left_join)

# RIGHT JOIN

right_join = pd.merge(df1, df2, on='ID', how='right')

print("\nRight Join Result:")
print(right_join)

# Set ID as index
df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')

index_join = df1_index.join(df2_index, how='inner')

print("\nIndex-Based Join Result:")
print(index_join)

# Create DataFrames with multiple common columns
df3 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Department': ['IT', 'HR', 'IT', 'Finance'],
    'Salary': [50000, 40000, 60000, 55000]
})

df4 = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Department': ['IT', 'HR', 'Marketing', 'Finance'],
    'Bonus': [5000, 3000, 4000, 3500]
})

print("\nDataFrame df3:")
print(df3)

print("\nDataFrame df4:")
print(df4)
