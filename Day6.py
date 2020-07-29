#!/usr/bin/env python
# coding: utf-8

# In[1]:


test_keys = [1,2,3,4,5,6,7,8,9]
test_values = ['a','b','c','d','e']
 
print(test_keys)
print(test_values)
res = {} 
for key in test_keys: 
    for value in test_values: 
        res[key] = value 
        test_values.remove(value) 
        break  
print(res)


# In[4]:


test_keys = [1,2,3,4,5]
test_values = ['a','b','c','d','e']
length=len(test_keys)
res = {test_keys[i]: test_values[i] for i in range(length)}
print(res)


# In[ ]:




