
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[47]:


df=pd.read_csv('C:\\Users\\p860n111\\Desktop\\data science\\HW_1\\DS3_Merged_DS1_DS2\\DS3_Merged_DS1andDS2.csv',parse_dates=['date'])


# In[27]:


df


# In[48]:


df.set_index('date',inplace=True)


# In[29]:


df


# In[30]:


df.describe


# In[31]:


print(df.info())


# In[49]:


df.corr()


# In[14]:


import matplotlib.pyplot as plt


# In[33]:


plt.matshow(df.corr())


# In[50]:


import seaborn as sns
corr = df.corr()
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)


# In[51]:


df


# In[52]:


df["# No Of accidents"]=((df["# No Of accidents"]-df["# No Of accidents"].min())/(df["# No Of accidents"].max()-df["# No Of accidents"].min()))


# df

# In[53]:


df


# In[44]:





# In[54]:


df.corr()


# In[55]:


corr = df.corr()
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)


# In[56]:


df.std() 


# In[57]:


df.corr(method='kendall')


# In[58]:


df.corr(method='spearman')


# In[59]:


df['snowfall'].corr(df['# No Of accidents'], method='spearman')


# In[66]:



from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('C:\\Users\\p860n111\\Desktop\\data science\\HW_1\\DS3_Merged_DS1_DS2\\DS3_Merged_DS1andDS2.csv', header=0)
series.plot()
pyplot.show()


# In[67]:


from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('C:\\Users\\p860n111\\Desktop\\data science\\HW_1\\DS3_Merged_DS1_DS2\\DS3_Merged_DS1andDS2.csv', header=0)
series.plot(style='k.')
pyplot.show()


# In[69]:


from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('C:\\Users\\p860n111\\Desktop\\data science\\HW_1\\DS3_Merged_DS1_DS2\\DS3_Merged_DS1andDS2.csv', header=0)
series.hist()
pyplot.show()

