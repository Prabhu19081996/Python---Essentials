#!/usr/bin/env python
# coding: utf-8

# In[2]:


def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return(x)

print(move_zero([0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]))


# In[1]:


l1 = [1, 3, 4, 7]
l2 = [0, 2, 5, 6, 8, 9]
l1.extend(l2)
sorted(l1)


# In[ ]:




