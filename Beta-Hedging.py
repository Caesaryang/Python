
# coding: utf-8

# In[106]:

import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import pandas as pd
import pandas_datareader as pdr
import statsmodels.formula.api as smf


# In[95]:

#we're setting a start and end datetime object
#this will be the range of dates that we're going to grab stock pricing information foR
start = dt.datetime(2016, 1, 1)
end = dt.datetime(2016, 12, 31)


# In[96]:

def get(tickers, startdate, enddate):
  def data(ticker):
    return (pdr.get_data_yahoo(ticker, start, end))
  datas = map (data, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))


# In[97]:

tickers = ['AAPL','SPY']
all_data = get(tickers, start, end)


# In[98]:

# Isolate the `Adj Close` values and transform the DataFrame
daily_close_px = all_data[['Adj Close']].reset_index().pivot('Date', 'Ticker', 'Adj Close')

daily_close_px.head()


# In[99]:

# Calculate the daily percentage change for `daily_close_px`
daily_pct_change = daily_close_px.pct_change()

# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)

daily_pct_change.head()


# In[100]:

daily_pct_change.plot(figsize=(14,8))
plt.ylabel("Daily Return")
plt.legend()
plt.show()


# In[101]:

# Import the OLS model
# Set SPY as my dependent variable, AAPL return as my independent variables
# Print out my OLS model stats result
results = smf.ols('AAPL ~ SPY', data=daily_pct_change).fit()
print(results.summary())


# In[102]:

results.params


# In[115]:

plt.figure(figsize=(14,8))
plt.xlabel('SPY daily return')
plt.ylabel('AAPL daily return')
plt.title('Linear Model & Scatter Plot')
plt.plot(daily_pct_change['SPY'], daily_pct_change['AAPL'], '.',
         daily_pct_change['SPY'], results.predict(daily_pct_change['SPY']), '-')


# In[103]:

alpha = results.params[0]
beta = results.params[1]


# In[104]:

print ('alpha: ' + str(alpha))
print ('beta: ' + str(beta))


# In[105]:

# Construct a portfolio with beta hedging
portfolio = -1*beta*daily_pct_change['SPY'] + daily_pct_change['AAPL']
portfolio.name = "AAPL + Beta Hedge"

daily_pct_change['AAPL'].plot(figsize=(14,8)) 
daily_pct_change['SPY'].plot(figsize=(14,8))
portfolio.plot(figsize=(14,8))
plt.ylabel("Daily Return")
plt.legend()
plt.show()

