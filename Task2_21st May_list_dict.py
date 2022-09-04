#!/usr/bin/env python
# coding: utf-8

# ### Task2_21st May_Manipulations on list_dict  .....by Dr.Tanuja S.Dhope

# ### Task 
# 
# #####  l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
# ##### 1 . Try to reverse a list 
# ##### 2. try to access 234 out of this list 
# ##### 3 . try to access 456 
# ##### 4 . Try to extract only a list collection form list l 
# ##### 5 . Try to extract "sudh"
# ##### 6 . Try to list all the key in dict element avaible in list 
# ##### 7 . Try to extract all the value element form dict available in list

# In[1]:


l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]


# In[2]:


print(l)


# ##### Q.1 reverse the list

# In[3]:


l.reverse()


# In[4]:


l


# ##### Q.2.try to access 234 out of this list 

# In[5]:



l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
l


# In[6]:


l[7][0]


# In[14]:


l[8].keys


# In[7]:


list(l[8].keys())[1]


# In[11]:


list(l[8].values())[1]


# ##### Q.3. Try to access 456

# In[12]:



l[5][1]


# ##### Q.4.Try to extract only a list collection form list 

# In[14]:



l[5:7]


# ###### Q.5. Try to extract "sudh"

# In[17]:



l[8]['key1']


# ##### Q.6 . Try to list all the key in dict element avaible in list 

# In[18]:



list(l[8].keys())


# ##### Q.7 . Try to extract all the value element form dict available in list

# In[20]:



list(l[8].values())


# In[21]:


l[8].values()


# In[ ]:




