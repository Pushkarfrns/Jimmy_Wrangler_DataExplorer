
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[43]:


df1=pd.read_csv('C:\\Users\\p860n111\\Desktop\\data science\\HW_1\\DS1\\DS1_weather_TownOfCaryProcessedData.csv',parse_dates=['date'])


# In[19]:


df1


# In[11]:


df1.shape


# In[12]:


df1.shape


# In[44]:


df2=pd.read_csv('C:\\Users\\p860n111\\Desktop\\data science\\HW_1\\DS2\\DS2_Crash_Report_ProcessedData.csv',parse_dates=['date'])


# In[18]:


df2


# In[15]:


df1.shape


# In[20]:


df3=pd.merge(df1,df2,on="date")


# In[22]:


df3.shape


# In[27]:


print(df1.info())


# In[28]:


print(df2.info())


# In[75]:


df1.set_index('date',inplace=True)


# In[76]:


df2.set_index('date',inplace=True)


# In[77]:


df1


# In[78]:


df2


# In[85]:


df_merged=pd.merge(df1,df2,on="date", how="inner")


# In[86]:


df_merged.shape


# In[71]:


df1.shape


# In[72]:


df2.shape


# In[87]:


df_merged


# In[83]:


print(df3.info())


# In[88]:


df3.to_csv('DS3_Merged_DS1andDS2.csv')

