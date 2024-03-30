#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json


# In[4]:


url= "https://data.covid19india.org/v4/min/timeseries.min.json"


# In[5]:


response=requests.get(url)


# In[25]:


dict_a=response.json()


# In[26]:


dict_a


# In[27]:


print(type(dict_a))

