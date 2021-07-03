#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('ls')


# In[2]:


import pandas as pd


# In[211]:


get_ipython().system(' pip install xlrd')


# In[3]:


#Read xls with xlrd
import xlrd

xlrd_book = xlrd.open_workbook("Nike.xls", on_demand=True)
with pd.ExcelFile(xlrd_book) as xls:
    df = pd.read_excel(xls, "Worksheet")


# In[4]:


df.head()


# In[5]:


# Make the first row the new header
new_header = df.iloc[0]
df = df[1:] 
df.columns = new_header


# In[6]:


df.head()


# In[7]:


# Rows and columns
df.shape


# In[8]:


# Check to see missing values and what columns can be removed
df.info


# In[9]:


# Remove columns that are not needed
df = df.drop(columns=['Nike, Inc. Brand(s)', 'Events', 'Region', 'Contact Name', 'Contact Phone', 'Contact Fax', 'Contact Email', 'Subcons'])
df.head()


# In[10]:


# Correct spelling of Vietnam
df.loc[
    df['Country/Region'].str.contains('^Viet', na=False),
    'Country/Region'
] = 'Vietnam'


# In[11]:


df.head()


# In[12]:


# Check types
df.dtypes


# In[13]:


# Change objects to floats
df['Total Workers'] = df['Total Workers'].astype(float)
df['Line Workers'] = df['Line Workers'].astype(float)


# In[14]:


# Remove %
import numpy as np
df['% Female Workers'] = df['% Female Workers'].str.replace('%', '')
df['% Migrant Workers'] = df['% Migrant Workers'].str.replace('%', '')


# In[15]:


# Change objects to floats
df['% Female Workers'] = df['% Female Workers'].astype(float)
df['% Migrant Workers'] = df['% Migrant Workers'].astype(float)


# In[16]:


# See which factories have no workers listed
df[df['Total Workers'] == 0.0]


# In[17]:


# Remove those rows
df = df.drop([173, 294])


# In[18]:


# Number of factories in each country
df['Country/Region'].value_counts()


# In[19]:


# Number of workers in each country
df.groupby(by='Country/Region')['Total Workers'].sum().sort_values(ascending=False)


# In[20]:


# Percent of migrant workers in each Chinese factory
df[df['Country/Region'] == 'China Mainland']['% Migrant Workers'].value_counts()


# In[21]:


# According to Nike, % Migrant workers are calculated based on total Line Workers
# Create column listing number of migrant workers using % Migrant Workers and Line Workers
df['Migrant Workers'] = ((df['% Migrant Workers'] * df['Line Workers']) / 100).round(2)


# In[22]:


# Number of migrant workers in China 
df[df['Country/Region'] == 'China Mainland']['Migrant Workers'].value_counts()


# In[23]:


# Number of migrant workers in China greater than zero
df[(df['Country/Region'] == 'China Mainland') & (df['Migrant Workers'] > 0.00)]


# In[24]:


# Find factory mentioned in WaPo article
df[df['Factory Name'] == 'QINGDAO TAEKWANG SHOES CO., LTD']


# In[25]:


# Who are the suppliers in China?
df[df['Country/Region'] == 'China Mainland']['Supplier Group'].value_counts()


# In[26]:


# Countries with most migrant workers
df.groupby(by='Country/Region')['Migrant Workers'].sum().sort_values(ascending=False)


# In[27]:


# Number of factories in each country by what they manufacture 
df.groupby(by='Product Type')['Country/Region'].value_counts()


# In[ ]:





# In[ ]:




