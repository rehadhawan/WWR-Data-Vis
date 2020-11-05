#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import csv
path = r"C:\Users\reha_\Downloads\rainYearly.csv"
file = open(path)
df = pd.read_csv(file)
print (df)
result = df.dtypes
print(result)
df["ï»¿Year"] = df[ 'ï»¿Year'].astype(float)
df.dtypes


# In[15]:


path2 = r"C:\Users\reha_\Downloads\tempYearly.csv"
file1 = open(path2)
df1 = pd.read_csv(file1)
print (df1)
df1.dtypes


# In[16]:


left = pd.DataFrame(df)
right = pd.DataFrame(df1)
res = pd.merge(left, right, how = 'inner', on = 'ï»¿Year')
print (res)


# In[19]:


import matplotlib.pyplot as plt
res.plot(x="ï»¿Year", y=["Rainfall", "Temperature"], kind='line')
plt.show()


# In[ ]:




