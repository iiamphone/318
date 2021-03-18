#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[6]:


data ={'Name':["John","Anna","Peter","Linda"],
      'Location':["New York","Paris","Berlin","London"],
      'Age':[24,13,53,33]
      }
data_pandas =pd.DataFrame(data)
display(data_pandas)


# In[7]:


display(data_pandas[data_pandas.Age>30])


# In[8]:


from sklearn.datasets import load_iris
iris_dataset = load_iris()
iris_dataset.keys()


# In[9]:


iris_dataset['feature_names']


# In[10]:


iris_dataset['target_names']


# In[11]:


type (iris_dataset['data'])


# In[12]:


iris_dataset['data'].shape


# In[13]:


iris_dataset['data'][:5]


# In[ ]:




