# Assignment-2-Finance-3300
Analyzing Canada's Consumer Price Index (CPI) using Pandas, NumPy, and Matplotlib. The project visualizes historical CPI trends and annual percentage changes through graphs and develops an inflation calculator (Bank of Canada) that allows users to estimate changes in purchasing power and compare prices across different time periods.
The results can be checked against the Bank of Canada's [Inflation Calculator](https://www.bankofcanada.ca/rates/related/inflation-calculator/)

## Files
- `CPI_2.py` - the main program: loads the data, draws the graph, and runs the calculator.
- `cpi_calc.csv` - monthly CPI data, 1914 to present (Bank of Canada Valet API, series STATIC_INFLATIONCALC; 2002 = 100).
- `cpi_graph.png` - the graph produced by the program.

## How to run [Overview of section]
1. Install Python 3 and the required libraries: `pip install pandas matplotlib`
2. Download this repository and keep all files in the same folder.
3. Run `python CPI.py`.
4. Enter a price, then a first and second date in `YYYY-MM` format (for example `1914-09`)

## CPI Graph
![Canada CPI and annual percentage change](cpi_graph.png)
The blue line is the CPI (left axis, 2002 = 100). The red line is the annual
percentage change (right axis). The dotted line marks the base level of 100.

## Section 1
1. Importing pandas and matplotlib.pyplot
2. Open and read the CSV file by skipping first 8 rows and using datetime to turn data strings into real dates


