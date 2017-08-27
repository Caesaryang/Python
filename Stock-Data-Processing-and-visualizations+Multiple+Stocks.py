
# coding: utf-8

# In[53]:

import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import pandas_datareader as pdr


# In[54]:

#we're setting a visulization style
style.use('ggplot')


# In[55]:

#we're setting a start and end datetime object
#this will be the range of dates that we're going to grab stock pricing information foR
start = dt.datetime(2016, 1, 1)
end = dt.datetime(2016, 12, 31)


# In[56]:

def get(tickers, startdate, enddate):
  def data(ticker):
    return (pdr.get_data_yahoo(ticker, start, end))
  datas = map (data, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))


# In[57]:

tickers = ['AAPL', 'TSLA', 'BABA', 'GOOG']
all_data = get(tickers, start, end)


# In[58]:

# Isolate the `Adj Close` values and transform the DataFrame
daily_close_px = all_data[['Adj Close']].reset_index().pivot('Date', 'Ticker', 'Adj Close')

daily_close_px.head()


# In[59]:

# Calculate the daily percentage change for `daily_close_px`
daily_pct_change = daily_close_px.pct_change()

# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)

# Plot the distributions
daily_pct_change.hist(bins=50, sharex=True, figsize=(12,8))

# Show the resulting plot
plt.show()


# In[60]:

daily_pct_change.head()


# In[61]:

# Calculate the cumulative daily returns
cum_daily_return = (1 + daily_pct_change).cumprod()
cum_daily_return.head()


# In[62]:

# Plot the cumulative daily returns
cum_daily_return.plot(figsize=(12,8))

# Show the plot
plt.show()

