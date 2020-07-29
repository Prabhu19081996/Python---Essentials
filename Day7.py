#!/usr/bin/env python
# coding: utf-8

# In[11]:


def zero(list):
    a = [0 for i in range(list.count(0))]
    x = [ i for i in list if i != 0]
    x.extend(a)
    return(x)
w=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
w.sort()
y=print(w)
x= zero(y)
print(x)


# In[ ]:



test_tup = (7, 8, 9, 1, 10, 7) 

# printing original tuple 
print("The original tuple is : " + str(test_tup)) 

# Tuple elements inversions 
# Using list() + sum() 
res = sum(list(test_tup)) 

# printing result 
print("The summation of tuple elements are : " + str(res)) 


# In[16]:


test_list1 = [(2, 4), (6, 7), (5, 1)] 
print("The original list 1 : " + str(test_list1))  
print(a[0]+a[1] for x in range(test_list1)) 


# In[17]:


# Python3 code to demonstrate 
# swap of key and value 
	
# initializing dictionary 
old_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69, 'G': 67, 'H': 23} 

new_dict = dict([(value, key) for key, value in old_dict.items()]) 
	
# Printing original dictionary 
print ("Original dictionary is : ") 
print(old_dict) 

print() 

# Printing new dictionary after swapping keys and values 
print ("Dictionary after swapping is : ") 
print("keys: values") 
for i in new_dict: 
	print(i, " : ", new_dict[i]) 


# In[27]:


old_dict =  {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"} 
new_dict = dict([(value, key) for key, value in old_dict.items()])  
print ("Original dictionary is : ") 
print(old_dict) 
print(new_dict) 
print() 
print ("Dictionary after swapping is : ") 
print("keys: values") 
for i in new_dict: 
  print(i, ": ", new_dict[i])

    


# In[28]:


test_list = [(1, 6), (3, 4), (5, 8)]  
print ("The original list is : " + str(test_list)) 
res = [sum(i[0]+i[1] for i in test_list)]
print ("The position summation of tuples  : " + str(res))


# In[ ]:




