
# coding: utf-8

# In[1]:


import sys
import string


# In[3]:


m_user = eval(input("Please enter any number of your choice :"))
n_user = eval(input("Please enter any number of your choice :"))


# In[4]:


def chartoascii(p,q):
    
    for i in range(p,(q+1)):
        
        div = i
        
        string = ""
        
        while div>0:
            
            mod=(div-1)%26
            string=chr(65+mod)+string
            div=int((div-mod)/26)
            
        print (string)
        
    return None

chartoascii(m_user,n_user)

