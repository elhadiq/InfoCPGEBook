#!/usr/bin/env python
# coding: utf-8

# # Tp Reconaissance des chiffres

# In[1]:


from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1)


# In[2]:


# Le dataset principal qui contient toutes les images
print (mnist.data.shape)

# Le vecteur d'annotations associé au dataset (nombre entre 0 et 9)
print (mnist.target.shape)


# In[3]:


import numpy as np

sample = np.random.randint(70000, size=1000)
data = mnist.data.iloc[sample]
target = mnist.target.iloc[sample]


# In[4]:


from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(data, target, train_size=0.8)


# In[5]:


xtrain=xtrain.values
xtest=xtest.values
ytrain=ytrain.values
ytest=ytest.values


# In[6]:


from MyKNNLIB import *


# In[7]:


matrice=ConfusionMatrix(xtest,ytest,(xtrain,ytrain,d1,11))
print(matrice)

