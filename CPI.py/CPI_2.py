"""
Part B: Consumer Price Index (CPI) analysis and inflation calculator.
Data source: Bank of Canada Valet API, STATIC_INFLATIONCALC series
(Statistics Canada monthly CPI for Canada, 1914 to present, 2002 = 100),
saved as cpi_calc.csv.
"""

import pandas as pd
import matplotlib.pyplot as plt

#Open  the CSV file and read the data into a DataFrame
df = pd.read_csv('cpi_calc.csv',skiprows=8) #skip the first 8 rows of the CSV file
df = df.rename(columns={'STATIC_INFLATIONCALC': 'cpi'})
df['date'] = pd.to_datetime(df['date']) #This turns the date string into real dates

dates = df['date'].tolist()
cpi = df['cpi'].tolist()
