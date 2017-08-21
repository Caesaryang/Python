
# coding: utf-8

# In[44]:

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt


# In[45]:

# Load data
# Rename all the columns 
# View the dataset
df = pd.read_excel('HW5.xls')
df.columns = ['GPA', 'SAT_Math', 'SAT_Verbal', 'HS_Math', 'HS_English']
df


# In[46]:

# Draw scatterplots for joint relationships and histograms for univariate distributions:
sns.set(style="ticks", color_codes=True)
sns.pairplot(df, kind="reg")
plt.show()


# In[47]:

# Import the OLS model
# Set GPA as my dependent variable, all the other columns as independent variables
# Print out my OLS model stats result
results = smf.ols('GPA ~ SAT_Math + SAT_Verbal + HS_Math + HS_English', data=df).fit()
print(results.summary())


# In[48]:

# Drop the irrelevant "intercept" and print out the t-values result
t = results.tvalues
t = t.drop(['Intercept'],axis=0)
t


# In[49]:

# Find out the variables that are statiscally significant
print (t[t > 2])


# In[50]:

tmax_key = t.idxmax()
tmax_value = t.loc[tmax_key]
print ("The most significant variable is", tmax_key, ", and its t-value is", tmax_value)

tmin_key = t.idxmin()
tmin_value = t.loc[tmin_key]
print ("The most insignificant variable is", tmin_key, ", and its t-value is", tmin_value)


# In[51]:

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


# In[52]:

# Import the improved OLS model
# Set GPA as my dependent variable, all the other columns as independent variables
# Print out my OLS model stats result
lm = smf.ols('GPA ~ SAT_Math + SAT_Verbal + HS_Math - 1', data=df).fit()
print(lm.summary())


# In[53]:

# Using the improved OLS model to predict 1Q_GPA
# Append the predicted result into the original data table
Predicted_GPA = lm.predict(predict_df)
predict_df['Predicted_GPA'] = pd.Series(Predicted_GPA, index = predict_df.index)
predict_df


# In[54]:

# Generate a new column into the original data table based on the value of Predicted_GPA
predict_df['Admission'] = np.where(predict_df['Predicted_GPA'] > 3, 'Yes', 'No')
predict_df

