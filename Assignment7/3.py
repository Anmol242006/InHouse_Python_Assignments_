""""""

import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['Anmol', 'Riya']
})

df2 = pd.DataFrame({
    'ID': [3, 4],
    'Name': ['Karan', 'Simran']
})

df3 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Marks': [85, 90, 78, 88]
})

print("DataFrame df1:")
print(df1)

print("\nDataFrame df2:")
print(df2)

print("\nDataFrame df3:")
print(df3)


# Step 1: Vertically Concatenate df1 and df2

concat_df = pd.concat([df1, df2], axis=0)

print("\nConcatenated DataFrame:")
print(concat_df)

# Step 2: Merge concatenated DataFrame with df3

merged_df = pd.merge(concat_df, df3, on='ID', how='inner')

print("\nMerged DataFrame using merge():")
print(merged_df)

# Step 3: Join using index

# Set ID as index
left_df = concat_df.set_index('ID')
right_df = df3.set_index('ID')

joined_df = left_df.join(right_df)

print("\nJoined DataFrame using join():")
print(joined_df)

# Difference Between join() and merge()

print("\nDifference Between join() and merge()")
print("--------------------------------------")
print("merge() -> Combines DataFrames using common columns.")
print("join()  -> Combines DataFrames using indexes.")
print("merge() is more flexible and similar to SQL joins.")
print("join() is simpler for index-based operations.")
