
# coding: utf-8

# In[552]:

import datetime as dt
import numpy as np 
import pandas as pd 
import pandas_datareader.data as web 
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt 
from matplotlib import style
get_ipython().magic('matplotlib inline')

style.use('fivethirtyeight')


# In[553]:

start = dt.datetime(2017, 1, 1)
end = dt.datetime(2017, 6, 1)

# list of stocks in portfolio
tickers = ['AAPL', 'FB', 'MSFT', 'NKE']

# Number of assets in portfolio
noa = len(tickers)

# array of weights in portfolio
weight = np.array([[0.25, 0.25, 0.25, 0.25]])


# In[554]:

def get_return(tickers, start, end, log_return=True):
    '''Download the price from yahoo finance
       Calculate the log return and store them in to a dataframe
       replace NaN with 0, if any'''    
    data = web.DataReader(tickers, 'yahoo', start, end)['Adj Close']
    data = data.sort_index()    
    if log_return:
        daily_return = np.log(data.pct_change()+1)
    else:
        daily_return = data.pct_change()           
    daily_return.fillna(0, inplace=True)    
    return daily_return


# In[556]:

daily_return = get_return(tickers, start, end)
daily_return.head()


# In[557]:

def rand_weights(noa):
    ''' Produces some random weights that sum to 1 '''
    w = np.random.random(noa) 
    w /= np.sum(w)
    return w

rand_weights(noa)


# In[558]:

def random_portfolio(daily_return):
    ''' 
    Returns the mean and standard deviation of returns for a random portfolio
    '''
    P = np.asmatrix(daily_return.mean() * 252)
    W = np.asmatrix(rand_weights(noa))
    C = np.asmatrix(daily_return.cov() * 252)
    
    mu = W * P.T
    sigma = np.sqrt(W * C * W.T)
    
    return mu, sigma


# In[559]:

n_portfolios = 10000

means, stds = np.column_stack([
random_portfolio(daily_return) 
    for _ in range(n_portfolios)
])


# In[560]:

daily_return['Portfolio'] = daily_return.dot(weight.T)
daily_return['SPY'] = get_return('SPY', start, end)
daily_return.head()


# In[561]:

cum_daily_return = (1 + daily_return).cumprod()
cum_daily_return.tail()


# In[562]:

ndays = len(daily_return)
actual_return = (1 + daily_return).prod() - 1
annualized_return = (1 + actual_return) ** ( 252 / ndays ) - 1
annualized_stdev = daily_return.std() * np.sqrt(252)

results = smf.ols('Portfolio ~ SPY', data=daily_return).fit()

ra = annualized_return['Portfolio']
rm = annualized_return['SPY']
rf = 0.00 # you can change this number

beta = results.params[1]
alpha = ra - beta*(rm - rf)

sharpe_ratio = (ra-rf)/annualized_stdev['Portfolio']


# In[563]:

print('Portfolio_annualized_return: ' + str(annualized_return['Portfolio']))
print('Portfolio_annualized_stdev: ' + str(annualized_stdev['Portfolio']))
print('Benchmark_annualized_return: ' + str(annualized_return['SPY']))
print('Benchmark_annualized_stdev: ' + str(annualized_stdev['SPY']))
print('Portfolio Beta: ' + str(beta))
print('Alpha: ' + str(alpha))
print('Sharpe_ratio: ' + str(sharpe_ratio))


# In[564]:

plt.figure(figsize=(12, 8)) 
plt.scatter(stds, means, c=means / stds, marker='o') 
plt.grid(True) 
plt.xlabel('Expected Volatility') 
plt.ylabel('Expected Return') 
plt.title('Return and Standard Deviation of Randomly Generated Portfolios')
plt.colorbar(label='Sharpe ratio')
# this red star is our portfolio
plt.scatter(annualized_stdev['Portfolio'],annualized_return['Portfolio'],marker=(5,1,0),color='r',s=1000)
# this green star is the benchmark, SPY
plt.scatter(annualized_stdev['SPY'],annualized_return['SPY'],marker=(5,1,0),color='g',s=1000)


# In[565]:

cum_daily_return[['Portfolio','SPY']].plot(grid = True, figsize=(14,10)).axhline(y = 1, color = "black", lw = 1)
plt.ylabel("Cumulative Returns")
plt.legend()
plt.show()


# In[566]:

cum_daily_return.plot(grid = True, figsize=(14,10)).axhline(y = 1, color = "black", lw = 1)
plt.ylabel("Cumulative Returns")
plt.legend()
plt.show()


# In[ ]:



