import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import mplfinance as mpf
import matplotlib.dates as mdates

style.use('ggplot')

df = pd.read_csv('../aapl.csv', parse_dates=True, index_col=0)

# Can resample to D, Min, S, etc
# Significantly shrinks size of data set
# ohlc means open, high, low, close
df_ohlc = df['Adj Close'].resample('10D').mean()
df_volume = df['Volume'].resample('10D').sum()

mpf.plot(df, type='candle', style='charles',
         title='Apple Stock',
         ylabel='High',
         ylabel_lower='Low',
         figratio=(10,5),
         figscale=1,
         mav=30,
         volume=True)
