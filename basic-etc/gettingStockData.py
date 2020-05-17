import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

# Style of plot
style.use('ggplot')

# Dates to extract data
start = dt.datetime(2000, 1, 1)
end = dt.datetime(2020, 4, 30)

# Data frame for TSLA stock from yahoo
df = web.DataReader('TSLA', 'yahoo', start, end)
print(df.head(6))
