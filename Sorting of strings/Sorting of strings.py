
# coding: utf-8

# In[1]:


import sys


# In[2]:


input_variable = [x for x in input("Please Enter Strings (give spaces in between two strings): ").split()]


# In[3]:


def sorting_Of_strings(x):
    
    k = sorted(x,key=len)
    return k


# In[4]:


sorting_Of_strings (input_variable)

