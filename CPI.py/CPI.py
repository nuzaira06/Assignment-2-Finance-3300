"""
Part B: Consumer Price Index (CPI) analysis and inflation calculator.
Data source: Bank of Canada Valet API, STATIC_INFLATIONCALC series
(Statistics Canada monthly CPI for Canada, 1914 to present, 2002 = 100),
saved as cpi_calc.csv.
"""

import pandas as pd
import matplotlib.pyplot as plt

#Open  the CSV file and read the data into a DataFrame
df = pd.read_csv('cpi_calc.csv')
df['date'] = pd.to_datetime(df['date']) #This turns the date string into real dates

dates = df['date'].tolist()
cpi = df['cpi'].tolist()

for obs in data['observations']:
    dates.append(obs['d'])  #the date string
    cpi.append(float(obs['STATIC_INFLATIONCALC']['v'])) #convert the CPI value to a float and append it to the list

df = pd.DataFrame({'date': dates, 'cpi': cpi})
df['date'] = pd.to_datetime(df['date']) #This turns the date string into real dates

# to calculate the annual percentage change
df['annual_change'] = df['cpi'].pct_change(periods=12) * 100

# To Plot the CPI line
fig, ax1 = plt.subplots(figsize=(12, 6)) #create a figure and its axes

ax1.plot(df['date'], df['cpi'], label= 'CPI') #plot the CPI line
ax1.axhline(100, linestyle=':', color='black', label='Base level (100)') #plot dotted line at 100

ax1.set_xlabel('Year') #set the x-axis label
ax1.set_ylabel('CPI (2002 = 100)') #set the y-axis label
ax1.set_title('Consumer Price Index') #set the title of the plot

ax2 = ax1.twinx() #create a second y-axis on the right side of the plot
ax2.plot(df['date'], df['annual_change'], color='tab:red', alpha=0.5, label='Annual % Change') #plot the annual percentage change line
ax2.set_ylabel('Annual % Change') #set the y-axis label for the second y-axis

h1, l1 = ax1.get_legend_handles_labels() #handles (line samples) and labels from the left axis
h2, l2 = ax2.get_legend_handles_labels() #same from the right axis
ax1.legend(h1 + h2, l1 + l2, loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=3)  # legend below the plot
fig.tight_layout()   # make room for the legend

fig.savefig('cpi_graph.png') #save the figure to a file


def get_price():
    #Asks the user for input until they input a valid number (positive float) and $ and , are allowed. An edge case in case a user inputs $ or , in the input.
    while True:                                   # repeats until we return a valid value
        text = input("Enter the price of goods or services ($): ")
        text = text.replace('$', '').replace(',', '').strip() #allows for $ and , in the input.
        try:
            price = float(text)                   # fails if text isn't a number
            if price > 0:                           # condition for a valid price
                return price                      # if valid, we leave the loop
            print("Price must be greater than zero.")
        except ValueError:                        # for whenever float() fails
            print("Invalid number. Please try again.")

price1 = get_price()

first = df['date'].min()      # earliest month in the data
last = df['date'].max()       # latest month in the data

def get_date(prompt):
    # Asks until the user enters a valid YYYY-MM date that falls inside the data range.
    while True:
        text = input(prompt)
        try:
            date = pd.to_datetime(text, format='%Y-%m')
            if first <= date <= last:        # date is inside the data range
                return date
            print("Date must be between", first.strftime('%Y-%m'), "and", last.strftime('%Y-%m'))
        except ValueError:
            print("Invalid format. Use YYYY-MM, for example 1999-05.")

date1 = get_date("Enter the first date (YYYY-MM): ")
date2 = get_date("Enter the second date (YYYY-MM): ")

# Looks up the CPI value for each date and iloc turns it into a number
cpi1 = df.loc[df['date'] == date1, 'cpi'].iloc[0]
cpi2 = df.loc[df['date'] == date2, 'cpi'].iloc[0]

# Calculate the price in the second period and the percentage change
price2 = price1 * (cpi2 / cpi1)
pct_change = (price2 - price1) / price1 * 100

# Count the months between the two dates and convert it to years
months = (date2.year - date1.year) * 12 + (date2.month - date1.month)
years = months / 12

# Calculate the annual rate of change
if years != 0:
    annual_rate = ((price2 / price1) ** (1 / years) - 1) * 100
else:
    annual_rate = 0.0       # if same month is entered twice: no time has passed


#Output the results
print(f"\n${price1:,.2f} CAD in {date1.strftime('%B %Y')} has the same buying power as "
      f"${price2:,.2f} CAD in {date2.strftime('%B %Y')}.\n")
print(f"Percent change:      {pct_change:.2f}%")
print(f"Number of years:    {years:.2f}")
print(f"Average annual rate of inflation (%)/Decline in the value of money:  {annual_rate:.2f}%")
print(f"CPI in {date1.strftime('%B %Y')}:  {cpi1:.1f}")
print(f"CPI in {date2.strftime('%B %Y')}:  {cpi2:.1f}")

plt.show() #display the graph

#the monthly data are stored under the "observations" key and other output tests
# print(data.keys())
# print(data['observations'][:2])
# print(df.head())
# print(df.tail())
# print(df.dtypes)
# print(df.head(15))
# print("You entered:", price1)
# print("You entered:", date1)
# print("CPI at first date:", cpi1)
# print("CPI at second date:", cpi2)
# print("Price in second period:", price2)
# print("Percentage change:", pct_change)
# print("Difference in years:", years)
# print("Annual rate of change:", annual_rate)