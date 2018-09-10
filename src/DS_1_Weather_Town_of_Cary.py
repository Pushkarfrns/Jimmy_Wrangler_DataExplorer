
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[46]:


df=pd.read_csv('C:\\Users\\Sony\\Desktop\\rdu-weather-history.csv')


# In[47]:


df


# In[48]:


df.shape


# In[49]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.head()


# In[9]:


print(df.columns)


# In[10]:


print(df.info())


# In[11]:


df[def.snowfall>0]


# In[12]:


df[df.snowfall>0]


# In[13]:


df[df.snow>0]


# In[14]:


df[df.snowfall==Yes]


# In[15]:


df[df.snowfall=='Yes']


# In[16]:


df[df.snowdepth>0]


# In[18]:


type(df.date[0])


# In[109]:


df=pd.read_csv('C:\\Users\\Sony\\Desktop\\rdu-weather-history.csv',parse_dates=['date'])


# In[81]:


df


# In[52]:


type(df.date[0])


# In[112]:


df.set_index('date',inplace=True)


# In[84]:


df.head()


# In[54]:


df['avgwindspeed'].isnull()


# In[55]:


new_df = df.interpolate()


# In[56]:


new_df['avgwindspeed'].isnull()


# In[36]:


new_df.to_csv('test.csv')


# In[57]:


new_df = df.interpolate(method="time")


# In[38]:


new_df


# In[43]:


dt = pd.date_range("2013-01-01","2018-09-04")
idx = pd.DatetimeIndex(dt)
df=df.reindex(idx)


# In[61]:


print(new_df.info())


# In[63]:


new_df = new_df.interpolate(method="time")


# In[64]:


new_df


# In[65]:


print(new_df.info())


# In[69]:


new_df.corr()


# In[71]:


df_dict = new_df.to_dict()


# In[72]:


print (pd.json.dumps( df_dict ))


# In[73]:


df_dict


# In[77]:


df.describe()


# In[79]:


print(df.info())


# In[85]:


df.head()


# In[86]:


dt = pd.date_range("2013-01-01","2018-09-04")
idx = pd.DatetimeIndex(dt)
df=df.reindex(idx)


# In[89]:


print(df.info())


# In[93]:


print(df.info())


# In[94]:


df.set_index('date',inplace=True)


# In[95]:


print(df.info())


# In[98]:


df.shape


# In[99]:


df.set_index('date',inplace=True)


# In[100]:


df.shape


# In[101]:


print(df.info())


# In[102]:


dt = pd.date_range("2013-01-01","2018-09-04")
idx = pd.DatetimeIndex(dt)
df=df.reindex(idx)


# In[104]:


df.shape


# In[113]:


print(df.info())


# In[114]:


new_df = df.interpolate()


# In[117]:


print(new_df.info())


# In[118]:


from sklearn import preprocessing


# In[119]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[120]:


df['temperaturemin'].plot(kind='bar')


# In[125]:


print(df.info())


# In[132]:


x = new_df[['temperaturemin']].values.astype(float)


# In[127]:


min_max_scaler = preprocessing.MinMaxScaler()


# In[128]:


x_scaled = min_max_scaler.fit_transform(x)


# In[129]:


df_normalized = pd.DataFrame(x_scaled)


# In[130]:


df_normalized


# In[133]:


new_df.drop(['fogheavy','fog', 'mist', 'rain', 'fogground', 'ice', 'glaze', 'drizzle', 'snow', 'freezingrain', 'smokehaze', 'thunder', 'highwind', 'hail', 
            'blowingsnow', 'dust', 'freezingfog'], axis=1, inplace= True)


# In[135]:


new_df.shape


# In[137]:


new_df


# In[138]:


df.describe()


# In[140]:


new_df.info()


# In[142]:


mean_normalized_df=(new_df-new_df.mean())/new_df.std()


# In[143]:


mean_normalized_df


# In[146]:


min_max_normalized_df=(new_df-new_df.min())/(new_df.max()-new_df.min())


# In[147]:


min_max_normalized_df


# In[148]:


min_max_normalized_df.to_csv('DS1_weather_TownOfCaryProcessedData.csv')

