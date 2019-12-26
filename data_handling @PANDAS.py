#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


df = pd.read_csv('ftp://192.168.10.254/pub/winter19-20/datasets/info.csv')


# In[8]:


df


# In[9]:


df.head(3)    #only top 3 lines


# In[10]:


df.head()    #by default top 5 rows


# In[12]:


#for any specific column

df['Country']


# In[13]:


df


# In[16]:


#index location value

#if only a particualr row

df.iloc[1:3]


# In[17]:


df.iloc[0:3,0:3]    #any specific row n column   range of rows and columns


# In[19]:


df.iloc[1:4,0:2]


# In[24]:


#if any randomn row and colunm is required

df.iloc[[3,5],[1,3]]


# In[25]:


#if without header   converted into numpy arry

df.iloc[[3,5],[1,3]].values


# In[28]:


max(df['Age'])


# In[31]:


min(df['Salary'])


# In[34]:


[i for i in dir(pd) if 'read' in i]


# In[ ]:




