
# coding: utf-8

# In[9]:


import pandas as pd 


# In[87]:


df=pd.read_excel('C:\\Users\\Sony\\Desktop\\Introduction to Data Science\\hw1\\cpd-crash-incidents_cary.xlsx', 'Sheet',parse_dates=['date'])


# In[73]:


df.shape


# In[74]:


print(df.info())


# In[28]:


df.shape


# In[29]:


df


# In[88]:


df.set_index('date',inplace=True)


# In[89]:


df


# In[42]:


df.shape


# In[43]:


df.shape


# In[44]:


df.shape


# In[45]:


df


# In[47]:


df.describe()


# In[49]:


print(df.info())


# In[90]:


df.fillna('No Information', inplace=True)


# In[91]:


df


# In[61]:


df


# In[92]:


print(df.info())


# In[66]:


g=df.groupby('date')


# In[67]:


g


# In[69]:


for date, data in g:
    print("date:",date)
    print("\n")
    print("date:",data)


# In[70]:


g.max()


# In[71]:


g.describe()


# In[93]:


new_df_Road_Configuration=df.groupby('date')['Road_Configuration' ].apply(list)


# In[94]:


new_df_Road_Configuration


# In[95]:


new_df_Road_Conditions=df.groupby('date')['Road_Conditions' ].apply(list)


# In[96]:


new_df_Road_Conditions


# In[97]:


new_df_Road_Conditions=df.groupby('date')['Road_Conditions' ].apply(list)


# In[98]:


new_df_Road_Conditions


# In[99]:


new_df_vehicleconcat1=df.groupby('date')['vehicleconcat1' ].apply(list)


# In[100]:


new_df_vehicleconcat1


# In[103]:


df1 = pd.concat([new_df_Road_Configuration,new_df_Road_Conditions],axis=1)


# In[106]:


df_grouped=pd.concat([df1,new_df_vehicleconcat1],axis=1)


# In[107]:


df_grouped


# In[109]:


print(df_grouped.info())


# In[112]:


df_grouped.corr()


# In[114]:


df_grouped['# No Of accidents'] = df_grouped['Road_Configuration'].apply(lambda x: len(x.split(',')))


# In[115]:


df_grouped['# No Of accidents'] = df_grouped['Road_Configuration'].apply(lambda x : len(str(x).split(',')))


# In[116]:


df_grouped


# In[128]:


df=pd.read_excel('C:\\Users\\Sony\\Desktop\\Introduction to Data Science\\hw1\\cpd-crash-incidents_cary.xlsx', 'Sheet',parse_dates=['date']) 


# In[118]:


print(df.info())


# In[129]:


df.set_index('date',inplace=True)


# In[120]:


print(df.info())


# In[130]:


df.fillna('No Information', inplace=True)


# In[122]:


print(df.info())


# In[131]:


new_df_Road_Configuration=df.groupby('date')['Road_Configuration' ].apply(list)
new_df_Road_Conditions=df.groupby('date')['Road_Conditions' ].apply(list)
new_df_vehicleconcat1=df.groupby('date')['vehicleconcat1' ].apply(list)


# In[132]:


df1 = pd.concat([new_df_Road_Configuration,new_df_Road_Conditions],axis=1)
df_grouped=pd.concat([df1,new_df_vehicleconcat1],axis=1)


# In[125]:


df_grouped


# In[133]:


df_grouped['# No Of accidents'] = df_grouped['Road_Conditions'].apply(lambda x : len(str(x).split(',')))


# In[134]:


df_grouped


# In[135]:


min_max_normalized_df.to_csv('DS1_weather_TownOfCaryProcessedData.csv')

