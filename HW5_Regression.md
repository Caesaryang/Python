

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt
```


```python
# Load data
# Rename all the columns 
# View the dataset
df = pd.read_excel('HW5.xls')
df.columns = ['GPA', 'SAT_Math', 'SAT_Verbal', 'HS_Math', 'HS_English']
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GPA</th>
      <th>SAT_Math</th>
      <th>SAT_Verbal</th>
      <th>HS_Math</th>
      <th>HS_English</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.97</td>
      <td>321</td>
      <td>247</td>
      <td>2.30</td>
      <td>2.63</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.74</td>
      <td>718</td>
      <td>436</td>
      <td>3.80</td>
      <td>3.57</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.19</td>
      <td>358</td>
      <td>578</td>
      <td>2.98</td>
      <td>2.57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.60</td>
      <td>403</td>
      <td>447</td>
      <td>3.58</td>
      <td>2.21</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.98</td>
      <td>640</td>
      <td>563</td>
      <td>3.38</td>
      <td>3.48</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.65</td>
      <td>237</td>
      <td>342</td>
      <td>1.48</td>
      <td>2.14</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.89</td>
      <td>270</td>
      <td>472</td>
      <td>1.67</td>
      <td>2.64</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2.38</td>
      <td>418</td>
      <td>356</td>
      <td>3.73</td>
      <td>2.52</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2.66</td>
      <td>443</td>
      <td>327</td>
      <td>3.09</td>
      <td>3.20</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.96</td>
      <td>359</td>
      <td>385</td>
      <td>1.54</td>
      <td>3.46</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3.14</td>
      <td>669</td>
      <td>664</td>
      <td>3.21</td>
      <td>3.37</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1.96</td>
      <td>409</td>
      <td>518</td>
      <td>2.77</td>
      <td>2.60</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2.20</td>
      <td>582</td>
      <td>364</td>
      <td>1.47</td>
      <td>2.90</td>
    </tr>
    <tr>
      <th>13</th>
      <td>3.90</td>
      <td>750</td>
      <td>632</td>
      <td>3.14</td>
      <td>3.49</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2.02</td>
      <td>451</td>
      <td>435</td>
      <td>1.54</td>
      <td>3.20</td>
    </tr>
    <tr>
      <th>15</th>
      <td>3.61</td>
      <td>645</td>
      <td>704</td>
      <td>3.50</td>
      <td>3.74</td>
    </tr>
    <tr>
      <th>16</th>
      <td>3.07</td>
      <td>791</td>
      <td>341</td>
      <td>3.20</td>
      <td>2.93</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2.63</td>
      <td>521</td>
      <td>483</td>
      <td>3.59</td>
      <td>3.32</td>
    </tr>
    <tr>
      <th>18</th>
      <td>3.11</td>
      <td>594</td>
      <td>665</td>
      <td>3.42</td>
      <td>2.70</td>
    </tr>
    <tr>
      <th>19</th>
      <td>3.20</td>
      <td>653</td>
      <td>606</td>
      <td>3.69</td>
      <td>3.52</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Draw scatterplots for joint relationships and histograms for univariate distributions:
sns.set(style="ticks", color_codes=True)
sns.pairplot(df, kind="reg")
plt.show()
```


![png](output_2_0.png)



```python
# Import the OLS model
# Set GPA as my dependent variable, all the other columns as independent variables
# Print out my OLS model stats result
results = smf.ols('GPA ~ SAT_Math + SAT_Verbal + HS_Math + HS_English', data=df).fit()
print(results.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                    GPA   R-squared:                       0.853
    Model:                            OLS   Adj. R-squared:                  0.814
    Method:                 Least Squares   F-statistic:                     21.72
    Date:                Wed, 02 Aug 2017   Prob (F-statistic):           4.25e-06
    Time:                        09:11:33   Log-Likelihood:                0.79507
    No. Observations:                  20   AIC:                             8.410
    Df Residuals:                      15   BIC:                             13.39
    Df Model:                           4                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept      0.1615      0.438      0.369      0.717      -0.771       1.094
    SAT_Math       0.0020      0.001      3.439      0.004       0.001       0.003
    SAT_Verbal     0.0013      0.001      2.270      0.038    7.67e-05       0.002
    HS_Math        0.1894      0.092      2.062      0.057      -0.006       0.385
    HS_English     0.0876      0.176      0.496      0.627      -0.289       0.464
    ==============================================================================
    Omnibus:                        0.673   Durbin-Watson:                   2.284
    Prob(Omnibus):                  0.714   Jarque-Bera (JB):                0.120
    Skew:                           0.185   Prob(JB):                        0.942
    Kurtosis:                       3.086   Cond. No.                     5.56e+03
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 5.56e+03. This might indicate that there are
    strong multicollinearity or other numerical problems.



```python
# Drop the irrelevant "intercept" and print out the t-values result
t = results.tvalues
t = t.drop(['Intercept'],axis=0)
t
```




    SAT_Math      3.439467
    SAT_Verbal    2.270444
    HS_Math       2.062090
    HS_English    0.496122
    dtype: float64




```python
# Find out the variables that are statiscally significant
print (t[t > 2])
```

    SAT_Math      3.439467
    SAT_Verbal    2.270444
    HS_Math       2.062090
    dtype: float64



```python
tmax_key = t.idxmax()
tmax_value = t.loc[tmax_key]
print ("The most significant variable is", tmax_key, ", and its t-value is", tmax_value)

tmin_key = t.idxmin()
tmin_value = t.loc[tmin_key]
print ("The most insignificant variable is", tmin_key, ", and its t-value is", tmin_value)
```

    The most significant variable is SAT_Math , and its t-value is 3.43946691293
    The most insignificant variable is HS_English , and its t-value is 0.496122306692



```python
# Generate and print the prediction dataset
predict_df = pd.DataFrame(
             [[680, 550, 3.8, 3.8],
              [650, 500, 3.0, 4],
              [450, 600, 2.5, 4.5],
              [503, 520, 3.25, 3.6],
              [750, 600, 3.95, 4]],
             index = ['Jacob', 'Kelly', 'Stuart', 'Jeremy', 'Linda'],
             columns = ['SAT_Math', 'SAT_Verbal', 'HS_Math', 'HS_English'])
predict_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SAT_Math</th>
      <th>SAT_Verbal</th>
      <th>HS_Math</th>
      <th>HS_English</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Jacob</th>
      <td>680</td>
      <td>550</td>
      <td>3.80</td>
      <td>3.8</td>
    </tr>
    <tr>
      <th>Kelly</th>
      <td>650</td>
      <td>500</td>
      <td>3.00</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>Stuart</th>
      <td>450</td>
      <td>600</td>
      <td>2.50</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>Jeremy</th>
      <td>503</td>
      <td>520</td>
      <td>3.25</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>Linda</th>
      <td>750</td>
      <td>600</td>
      <td>3.95</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Import the improved OLS model
# Set GPA as my dependent variable, all the other columns as independent variables
# Print out my OLS model stats result
lm = smf.ols('GPA ~ SAT_Math + SAT_Verbal + HS_Math - 1', data=df).fit()
print(lm.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                    GPA   R-squared:                       0.991
    Model:                            OLS   Adj. R-squared:                  0.990
    Method:                 Least Squares   F-statistic:                     656.4
    Date:                Wed, 02 Aug 2017   Prob (F-statistic):           9.11e-18
    Time:                        09:11:49   Log-Likelihood:               -0.35977
    No. Observations:                  20   AIC:                             6.720
    Df Residuals:                      17   BIC:                             9.707
    Df Model:                           3                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    SAT_Math       0.0023      0.000      5.034      0.000       0.001       0.003
    SAT_Verbal     0.0016      0.000      3.483      0.003       0.001       0.003
    HS_Math        0.2168      0.085      2.565      0.020       0.038       0.395
    ==============================================================================
    Omnibus:                        0.055   Durbin-Watson:                   1.899
    Prob(Omnibus):                  0.973   Jarque-Bera (JB):                0.281
    Skew:                           0.003   Prob(JB):                        0.869
    Kurtosis:                       2.419   Cond. No.                     1.02e+03
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 1.02e+03. This might indicate that there are
    strong multicollinearity or other numerical problems.



```python
# Using the improved OLS model to predict 1Q_GPA
# Append the predicted result into the original data table
Predicted_GPA = lm.predict(predict_df)
predict_df['Predicted_GPA'] = pd.Series(Predicted_GPA, index = predict_df.index)
predict_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SAT_Math</th>
      <th>SAT_Verbal</th>
      <th>HS_Math</th>
      <th>HS_English</th>
      <th>Predicted_GPA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Jacob</th>
      <td>680</td>
      <td>550</td>
      <td>3.80</td>
      <td>3.8</td>
      <td>3.284888</td>
    </tr>
    <tr>
      <th>Kelly</th>
      <td>650</td>
      <td>500</td>
      <td>3.00</td>
      <td>4.0</td>
      <td>2.960764</td>
    </tr>
    <tr>
      <th>Stuart</th>
      <td>450</td>
      <td>600</td>
      <td>2.50</td>
      <td>4.5</td>
      <td>2.557058</td>
    </tr>
    <tr>
      <th>Jeremy</th>
      <td>503</td>
      <td>520</td>
      <td>3.25</td>
      <td>3.6</td>
      <td>2.710301</td>
    </tr>
    <tr>
      <th>Linda</th>
      <td>750</td>
      <td>600</td>
      <td>3.95</td>
      <td>4.0</td>
      <td>3.559927</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Generate a new column into the original data table based on the value of Predicted_GPA
predict_df['Admission'] = np.where(predict_df['Predicted_GPA'] > 3, 'Yes', 'No')
predict_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SAT_Math</th>
      <th>SAT_Verbal</th>
      <th>HS_Math</th>
      <th>HS_English</th>
      <th>Predicted_GPA</th>
      <th>Admission</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Jacob</th>
      <td>680</td>
      <td>550</td>
      <td>3.80</td>
      <td>3.8</td>
      <td>3.284888</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>Kelly</th>
      <td>650</td>
      <td>500</td>
      <td>3.00</td>
      <td>4.0</td>
      <td>2.960764</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Stuart</th>
      <td>450</td>
      <td>600</td>
      <td>2.50</td>
      <td>4.5</td>
      <td>2.557058</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Jeremy</th>
      <td>503</td>
      <td>520</td>
      <td>3.25</td>
      <td>3.6</td>
      <td>2.710301</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Linda</th>
      <td>750</td>
      <td>600</td>
      <td>3.95</td>
      <td>4.0</td>
      <td>3.559927</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>


