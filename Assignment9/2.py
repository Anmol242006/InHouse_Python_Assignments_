"""2) Explore more datetime function and uses in pandas """

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Date": ["2026-05-27", "2026-06-01", "2026-07-15"]
})

# Convert to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Extract datetime information
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Day_Name"] = df["Date"].dt.day_name()

# Current date and time
current = pd.Timestamp.now()

print("Current Date & Time:")
print(current)

print("\nDataFrame:")
print(df)

# Date operations
df["Next_7_Days"] = df["Date"] + pd.Timedelta(days=7)

print("\nAfter Adding 7 Days:")
print(df)

# Filtering dates
filtered = df[df["Date"] > "2026-06-01"]

print("\nFiltered Dates:")
print(filtered)
