#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor


# In[8]:


df = pd.read_csv('AnkaraHousesDatasetProduction.csv')


# In[9]:


y=df.loc[:, 'Price']
X=df.loc[:, df.columns != 'Price']


# In[10]:


RFReg=RandomForestRegressor(n_estimators=250, max_depth=14, min_samples_leaf=2, random_state=42)


# In[11]:


RFReg.fit(X, y)


# In[13]:


import pickle

pickle.dump(RFReg, open('model.pkl','wb'))


# In[14]:


model = pickle.load(open('model.pkl','rb'))


# In[ ]:
