#!/usr/bin/env python
# coding: utf-8

# In[209]:


get_ipython().system('ls')


# In[267]:


import pandas as pd


# In[211]:


get_ipython().system(' pip install xlrd')


# In[268]:


#Read xls with xlrd
import xlrd

xlrd_book = xlrd.open_workbook("Nike.xls", on_demand=True)
with pd.ExcelFile(xlrd_book) as xls:
    df = pd.read_excel(xls, "Worksheet")


# In[269]:


df.head()


# In[270]:


# Make the first row the new header
new_header = df.iloc[0]
df = df[1:] 
df.columns = new_header


# In[271]:


df.head()


# In[272]:


# Rows and columns
df.shape


# In[274]:


# Check to see missing values and what columns can be removed
df.info


# In[275]:


# Remove columns that are not needed
df = df.drop(columns=['Nike, Inc. Brand(s)', 'Events', 'Region', 'Contact Name', 'Contact Phone', 'Contact Fax', 'Contact Email', 'Subcons'])
df.head()


# In[277]:


# Correct spelling of Vietnam
df.loc[
    df['Country/Region'].str.contains('^Viet', na=False),
    'Country/Region'
] = 'Vietnam'


# In[278]:


df.head()


# In[279]:


# Check types
df.dtypes


# In[280]:


# Change objects to floats
df['Total Workers'] = df['Total Workers'].astype(float)
df['Line Workers'] = df['Line Workers'].astype(float)


# In[281]:


# Remove %
import numpy as np
df['% Female Workers'] = df['% Female Workers'].str.replace('%', '')
df['% Migrant Workers'] = df['% Migrant Workers'].str.replace('%', '')


# In[282]:


# Change objects to floats
df['% Female Workers'] = df['% Female Workers'].astype(float)
df['% Migrant Workers'] = df['% Migrant Workers'].astype(float)


# In[283]:


# See which factories have no workers listed
df[df['Total Workers'] == 0.0]


# In[284]:


# Remove those rows
df = df.drop([173, 294])


# In[311]:


# Number of factories in each country
df['Country/Region'].value_counts()


# In[285]:


# Number of workers in each country
df.groupby(by='Country/Region')['Total Workers'].sum().sort_values(ascending=False)


# In[287]:


# Percent of workers in each Chinese factory
df[df['Country/Region'] == 'China Mainland']['% Migrant Workers'].value_counts()


# In[288]:


# Create column listing number of migrant workers using % Migrant Workers and Total Workers
df['Migrant Workers'] = ((df['% Migrant Workers'] * df['Total Workers']) / 100).round(2)


# In[289]:


# Number of migrant workers in China 
df[df['Country/Region'] == 'China Mainland']['Migrant Workers'].value_counts()


# In[305]:


# Number of migrant workers in China greater than zero
df[(df['Country/Region'] == 'China Mainland') & (df['Migrant Workers'] > 0.00)]


# In[292]:


# Find factory mentioned in WaPo article
df[df['Factory Name'] == 'QINGDAO TAEKWANG SHOES CO., LTD']


# In[293]:


# Who are the suppliers in China?
df[df['Country/Region'] == 'China Mainland']['Supplier Group'].value_counts()


# In[307]:


# Countries with most migrant workers
df.groupby(by='Country/Region')['Migrant Workers'].sum().sort_values(ascending=False)


# In[310]:


# Number of factories in each country by what they manufacture 
df.groupby(by='Product Type')['Country/Region'].value_counts()


# In[ ]:




