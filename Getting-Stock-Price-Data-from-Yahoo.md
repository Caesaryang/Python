

```python
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
```


```python
#we're setting a visulization style
style.use('ggplot')
```


```python
#we're setting a start and end datetime object
#this will be the range of dates that we're going to grab stock pricing information foR
start = dt.datetime(2017, 1, 1)
end = dt.datetime(2017, 7, 31)
```


```python
#Select the ticker and source of stock data
df = web.DataReader('AAPL', "yahoo", start, end)
```


```python
#Adj Close is helpful, since it accounts for future stock splits, and gives the relative price to splits
#For this reason, the adjusted prices are the prices you're most likely to be dealing with.
df.tail()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-07-26</th>
      <td>153.350006</td>
      <td>153.929993</td>
      <td>153.059998</td>
      <td>153.460007</td>
      <td>152.859726</td>
      <td>15781000</td>
    </tr>
    <tr>
      <th>2017-07-27</th>
      <td>153.750000</td>
      <td>153.990005</td>
      <td>147.300003</td>
      <td>150.559998</td>
      <td>149.971069</td>
      <td>32476300</td>
    </tr>
    <tr>
      <th>2017-07-28</th>
      <td>149.889999</td>
      <td>150.229996</td>
      <td>149.190002</td>
      <td>149.500000</td>
      <td>148.915207</td>
      <td>17213700</td>
    </tr>
    <tr>
      <th>2017-07-31</th>
      <td>149.899994</td>
      <td>150.330002</td>
      <td>148.130005</td>
      <td>148.729996</td>
      <td>148.148224</td>
      <td>19845900</td>
    </tr>
    <tr>
      <th>2017-08-01</th>
      <td>149.100006</td>
      <td>150.220001</td>
      <td>148.410004</td>
      <td>150.050003</td>
      <td>149.463058</td>
      <td>35368600</td>
    </tr>
  </tbody>
</table>
</div>




```python
#We can save them easily to a csv in our wd
df.to_csv('AAPL.csv')
```


```python
#We can either read data from DataFrame or from a CSV file into a DataFrame:
df = pd.read_csv('AAPL.csv', parse_dates=True, index_col=0)
```


```python
##Now, we can graph it
df.plot()
plt.show()
```


![png](output_7_0.png)



```python
#Now, we can graph one specific column in the DataFrame
df['Adj Close'].plot()
plt.show()
```


![png](output_8_0.png)



```python
#Call one or more columns in the DataFrame
df[['High','Low']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>High</th>
      <th>Low</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-03</th>
      <td>116.330002</td>
      <td>114.760002</td>
    </tr>
    <tr>
      <th>2017-01-04</th>
      <td>116.510002</td>
      <td>115.750000</td>
    </tr>
    <tr>
      <th>2017-01-05</th>
      <td>116.860001</td>
      <td>115.809998</td>
    </tr>
    <tr>
      <th>2017-01-06</th>
      <td>118.160004</td>
      <td>116.470001</td>
    </tr>
    <tr>
      <th>2017-01-09</th>
      <td>119.430000</td>
      <td>117.940002</td>
    </tr>
    <tr>
      <th>2017-01-10</th>
      <td>119.379997</td>
      <td>118.300003</td>
    </tr>
    <tr>
      <th>2017-01-11</th>
      <td>119.930000</td>
      <td>118.599998</td>
    </tr>
    <tr>
      <th>2017-01-12</th>
      <td>119.300003</td>
      <td>118.209999</td>
    </tr>
    <tr>
      <th>2017-01-13</th>
      <td>119.620003</td>
      <td>118.809998</td>
    </tr>
    <tr>
      <th>2017-01-17</th>
      <td>120.239998</td>
      <td>118.220001</td>
    </tr>
    <tr>
      <th>2017-01-18</th>
      <td>120.500000</td>
      <td>119.709999</td>
    </tr>
    <tr>
      <th>2017-01-19</th>
      <td>120.089996</td>
      <td>119.370003</td>
    </tr>
    <tr>
      <th>2017-01-20</th>
      <td>120.449997</td>
      <td>119.730003</td>
    </tr>
    <tr>
      <th>2017-01-23</th>
      <td>120.809998</td>
      <td>119.769997</td>
    </tr>
    <tr>
      <th>2017-01-24</th>
      <td>120.099998</td>
      <td>119.500000</td>
    </tr>
    <tr>
      <th>2017-01-25</th>
      <td>122.099998</td>
      <td>120.279999</td>
    </tr>
    <tr>
      <th>2017-01-26</th>
      <td>122.440002</td>
      <td>121.599998</td>
    </tr>
    <tr>
      <th>2017-01-27</th>
      <td>122.349998</td>
      <td>121.599998</td>
    </tr>
    <tr>
      <th>2017-01-30</th>
      <td>121.629997</td>
      <td>120.660004</td>
    </tr>
    <tr>
      <th>2017-01-31</th>
      <td>121.389999</td>
      <td>120.620003</td>
    </tr>
    <tr>
      <th>2017-02-01</th>
      <td>130.490005</td>
      <td>127.010002</td>
    </tr>
    <tr>
      <th>2017-02-02</th>
      <td>129.389999</td>
      <td>127.779999</td>
    </tr>
    <tr>
      <th>2017-02-03</th>
      <td>129.190002</td>
      <td>128.160004</td>
    </tr>
    <tr>
      <th>2017-02-06</th>
      <td>130.500000</td>
      <td>128.899994</td>
    </tr>
    <tr>
      <th>2017-02-07</th>
      <td>132.089996</td>
      <td>130.449997</td>
    </tr>
    <tr>
      <th>2017-02-08</th>
      <td>132.220001</td>
      <td>131.220001</td>
    </tr>
    <tr>
      <th>2017-02-09</th>
      <td>132.449997</td>
      <td>131.119995</td>
    </tr>
    <tr>
      <th>2017-02-10</th>
      <td>132.940002</td>
      <td>132.050003</td>
    </tr>
    <tr>
      <th>2017-02-13</th>
      <td>133.820007</td>
      <td>132.750000</td>
    </tr>
    <tr>
      <th>2017-02-14</th>
      <td>135.089996</td>
      <td>133.250000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2017-06-20</th>
      <td>146.869995</td>
      <td>144.940002</td>
    </tr>
    <tr>
      <th>2017-06-21</th>
      <td>146.070007</td>
      <td>144.610001</td>
    </tr>
    <tr>
      <th>2017-06-22</th>
      <td>146.699997</td>
      <td>145.119995</td>
    </tr>
    <tr>
      <th>2017-06-23</th>
      <td>147.160004</td>
      <td>145.110001</td>
    </tr>
    <tr>
      <th>2017-06-26</th>
      <td>148.279999</td>
      <td>145.380005</td>
    </tr>
    <tr>
      <th>2017-06-27</th>
      <td>146.160004</td>
      <td>143.619995</td>
    </tr>
    <tr>
      <th>2017-06-28</th>
      <td>146.110001</td>
      <td>143.160004</td>
    </tr>
    <tr>
      <th>2017-06-29</th>
      <td>145.130005</td>
      <td>142.279999</td>
    </tr>
    <tr>
      <th>2017-06-30</th>
      <td>144.960007</td>
      <td>143.779999</td>
    </tr>
    <tr>
      <th>2017-07-03</th>
      <td>145.300003</td>
      <td>143.100006</td>
    </tr>
    <tr>
      <th>2017-07-05</th>
      <td>144.789993</td>
      <td>142.720001</td>
    </tr>
    <tr>
      <th>2017-07-06</th>
      <td>143.500000</td>
      <td>142.410004</td>
    </tr>
    <tr>
      <th>2017-07-07</th>
      <td>144.750000</td>
      <td>142.899994</td>
    </tr>
    <tr>
      <th>2017-07-10</th>
      <td>145.949997</td>
      <td>143.369995</td>
    </tr>
    <tr>
      <th>2017-07-11</th>
      <td>145.850006</td>
      <td>144.380005</td>
    </tr>
    <tr>
      <th>2017-07-12</th>
      <td>146.179993</td>
      <td>144.820007</td>
    </tr>
    <tr>
      <th>2017-07-13</th>
      <td>148.490005</td>
      <td>145.440002</td>
    </tr>
    <tr>
      <th>2017-07-14</th>
      <td>149.330002</td>
      <td>147.330002</td>
    </tr>
    <tr>
      <th>2017-07-17</th>
      <td>150.899994</td>
      <td>148.570007</td>
    </tr>
    <tr>
      <th>2017-07-18</th>
      <td>150.130005</td>
      <td>148.669998</td>
    </tr>
    <tr>
      <th>2017-07-19</th>
      <td>151.419998</td>
      <td>149.949997</td>
    </tr>
    <tr>
      <th>2017-07-20</th>
      <td>151.740005</td>
      <td>150.190002</td>
    </tr>
    <tr>
      <th>2017-07-21</th>
      <td>150.440002</td>
      <td>148.880005</td>
    </tr>
    <tr>
      <th>2017-07-24</th>
      <td>152.440002</td>
      <td>149.899994</td>
    </tr>
    <tr>
      <th>2017-07-25</th>
      <td>153.839996</td>
      <td>151.800003</td>
    </tr>
    <tr>
      <th>2017-07-26</th>
      <td>153.929993</td>
      <td>153.059998</td>
    </tr>
    <tr>
      <th>2017-07-27</th>
      <td>153.990005</td>
      <td>147.300003</td>
    </tr>
    <tr>
      <th>2017-07-28</th>
      <td>150.229996</td>
      <td>149.190002</td>
    </tr>
    <tr>
      <th>2017-07-31</th>
      <td>150.330002</td>
      <td>148.130005</td>
    </tr>
    <tr>
      <th>2017-08-01</th>
      <td>150.220001</td>
      <td>148.410004</td>
    </tr>
  </tbody>
</table>
<p>146 rows × 2 columns</p>
</div>


