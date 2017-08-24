
# coding: utf-8

# In[14]:

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


# In[15]:

#we're setting a visulization style
style.use('ggplot')


# In[16]:

#we're setting a start and end datetime object
#this will be the range of dates that we're going to grab stock pricing information foR
start = dt.datetime(2017, 1, 1)
end = dt.datetime(2017, 7, 31)


# In[18]:

#Select the ticker and source of stock data
df = web.DataReader('AAPL', "yahoo", start, end)


# In[20]:

#Adj Close is helpful, since it accounts for future stock splits, and gives the relative price to splits
#For this reason, the adjusted prices are the prices you're most likely to be dealing with.
df.tail()


# In[21]:

#We can save them easily to a csv in our wd
df.to_csv('AAPL.csv')


# In[22]:

#We can either read data from DataFrame or from a CSV file into a DataFrame:
df = pd.read_csv('AAPL.csv', parse_dates=True, index_col=0)


# In[26]:

##Now, we can graph it
df.plot()
plt.show()


# In[27]:

#Now, we can graph one specific column in the DataFrame
df['Adj Close'].plot()
plt.show()


# In[29]:

#Call one or more columns in the DataFrame
df[['High','Low']]

