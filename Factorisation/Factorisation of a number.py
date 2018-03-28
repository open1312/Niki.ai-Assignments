
# coding: utf-8

# In[1]:


import sys
from math import sqrt; from itertools import count, islice


# In[2]:


threshold = 100000
input_variable = eval(input("Please Enter some number: "))


# In[3]:


def prime_number(n):
    
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


prime_number(input_variable)


# In[4]:


def factorial():
    
    if threshold <= input_variable:
        
        print ("Please enter some smaller number than 1,00,000!!!")
        
    else :
        
        for i in range(2, input_variable+1):
            
            if input_variable%i ==0:
                
                print ("The factors of",input_variable,"is :", i)
            
factorial()

