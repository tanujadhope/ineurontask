#!/usr/bin/env python
# coding: utf-8

# ### Task3_if else if  ...by Dr.Tanuja S.Dhope

# ##### a,b,c,d=10,11,12,13
# 
# 
# 
# ##### Q.1 write if else for checking all conditions of given value
# 
# ##### Q.2  What is the difference between:
# print(type(a) == int)
# print(type(a) is int) 
# 
# ##### Q.3. Write a Python program to display calendar?

# ##### Q.1 write if else for checking all conditions of given value
# 

# In[3]:


a,b,c,d=10,11,12,13


# In[4]:


a,b,c,d


# In[5]:


if a==10 or b==11 and c==12 and d==113: #### Case 1
    # this is equal to a==10 or (b==11 and c==12 and d==113)
    print('lets do something 1')
if (a==10 and b==11 ) or (c==12 and d==113):  #### Case 2
    # this is equal to (a==10 and b==11) or (c==12 and d==113)
    print('lets do something 2')
if a==10 and b==11 and c==12 and d==13 or a==9:   #### Case 3
    # this is equal to (a==10 and b==11 and c==12 and d==13) or a==9
    print('lets do something 3')
if a==9 or b==11 and c==12 and d==13:   #### Case 4
    print('lets do something 4')


# ##### Q.2  What is the difference between:
# print(type(a) == int)
# print(type(a) is int)  both are same

# In[8]:


print(type(a) == int)   # if type of a is integer ,it will return  true if a is integer else return false .it will return boolean value


# In[9]:


print(type(a) is int) # same as above


# ##### Q.3. Write a Python program to display calendar monthly/Yearly?
# 

# In[2]:


import calendar
value=int(input('please enter 1 for monthly else enter 2 for yearly: '))
if (value==1):
    yr=int(input('enter the year:  '))
    mm=int(input('enter the month: '))
    print(calendar.month(yr, mm))
elif(value==2):
    yr=int(input('enter the year:'))
    print(calendar.calendar(yr))
    
else:
    print('Wrong user entry')


# In[ ]:




