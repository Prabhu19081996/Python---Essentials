#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
str="what we think we become; we are the Python programmers"
str1="we"
y=[i.start() for i in re.finditer(str1,str)]
print(y)


# In[2]:


string = 'prabhu'
print(string.islower()) 
  
string = 'Prabhu'
print(string.islower()) 


# In[3]:


string = 'PRABHA'
print(string.isupper()) 
  
string = 'Prabhu'
print(string.isupper())


# In[ ]:




