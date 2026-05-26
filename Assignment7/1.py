""" 1) Convert a series of date-strings to a timeseries?
"""
import pandas as pd
l = ["2006-10-24", "2005-09-11", "2006-03-11", "2006-01-20"]

result = pd.Series(l)
print(result)

print(pd.to_datetime(result))
