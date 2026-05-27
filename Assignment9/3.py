"""3) Import an meaningful csv file for data analysis and perform data cleaning, and analysis for meaningful output"""

import pandas as pd

# Import CSV file
df = pd.read_csv("students.csv")

print("First 5 Rows:")
print(df.head())

# Data Cleaning
print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df["Age"] = df["Age"].astype(int)

# Data Analysis
print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

print("\nStudents Scoring More Than 80:")
print(df[df["Marks"] > 80])

print("\nAverage Marks by Gender:")
print(df.groupby("Gender")["Marks"].mean())
