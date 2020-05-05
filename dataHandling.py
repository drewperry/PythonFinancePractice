import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# Gets data
start = dt.datetime(2000, 1, 1)
end = dt.datetime(2020, 4, 30)

# Pulls data and puts into csv
df = web.DataReader('AAPL', 'yahoo', start, end)
df.to_csv('aapl.csv')

# Reads in csv and prints
# You can read json, sql, etc
df2 = pd.read_csv('aapl.csv', parse_dates=True, index_col=0)
print(df2.head())

print(df[['Open', 'High']])
# Only plots Adj column
df2['Adj Close'].plot()
plt.show()