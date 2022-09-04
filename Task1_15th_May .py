#!/usr/bin/env python
# coding: utf-8

# #### Task1_15th_May  on String Manipulations  ..  by Dr.Tanuja S.Dhope
# 

# ### TASK1    s = "this is My First Python programming class and i am learNING python string and its function"
# ##### 1 . Try to extract data from index one to index 300 with a jump of 3 
# ##### 2. Try to reverse a string without using reverse function 
# ##### 3. Try to split a string after conversion of entire string in uppercase 
# ##### 4. try to convert the whole string into lower case 
# ##### 5 . Try to capitalize the whole string 
# ##### 6 . Write a diference between isalnum() and isalpha()
# ##### 7. Try to give an example of expand tab
# ##### 8 . Give an example of strip , lstrip and rstrip 
# ##### 9.  Replace a string charecter by another charector by taking your own example "sudhanshu"
# ##### 10 . Try  to give a defination of string center function with and exmple 
# ##### 11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
# ##### 12 . Python is a interpreted of compiled language give a clear ans with your understanding 
# ##### 13 . Try to write a usecase of python with your understanding .
# 

# 

# In[33]:


s = "this is My First Python programming class and i am learNING python string and its function"


# In[34]:


s


# #####  Q.1 . Try to extract data from index one to index 300 with a jump of 3 
# 
# 

# In[35]:



s[0:300:3]


# ##### Q.2. Try to reverse a string without using reverse function 

# In[36]:



s[::-1]


# ##### Q.3. Try to split a string after conversion of entire string in uppercase 

# In[37]:



n=s.upper()


# In[38]:


n.split('R')


# ###### Q.4. Try to convert the whole string into lower case 

# In[39]:



s.lower()


# ###### Q.5 . Try to capitalize the whole string 

# In[40]:



s.capitalize()


# In[ ]:





# In[41]:


s.title()  # for showing the difference


# In[ ]:





# ###### Q.6 . Write a diference between isalnum() and isalpha()
# #isalnum()  - function will return True if in the given string contains alpha or numerical value
# #isalpha()-function will return True if in the given string contains only  alpha charater else will return false

# ###### Q.7. Try to give an example of expand tab

# In[42]:



s1="hhe\tgge\thhe"
s1.expandtabs()


# ###### Q8 . Give an example of strip , lstrip and rstrip 

# In[43]:



s2='     mano javam    '
s2.strip()


# In[44]:


s2.lstrip()


# In[45]:


s2.rstrip()


# ###### Q.9.  Replace a string charecter by another charector by taking your own example "manojavam"

# In[46]:



s2=" I like to live in lonely island"
s2.replace('like','dislike')


# ###### Q.10 . Try  to give a defination of string center function with and exmple 

# In[47]:



s3=" I like to live in water"
s3.center(50,'@')
# center function reserves the 50 places and will write the given string in the center ,and inserting special charec as per in the 
# command to left and right of the given string.


# ###### Q.11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
# #complier scans the entire code then coverts into machine code
# #interpreter scans the code line by line ,converts into an intermediate code before machine code
# 

# ###### Q.12 . Python is a interpreted of compiled language give a clear ans with your understanding 
# yes  python automatically compiles your script to compiled code, so called byte code, before running it.
#  Internally this byte code gets converted by the python virtual machine(p.v.m) according to the underlying platform
#     (machine+operating system).
# 

# ###### Q13 . Try to write a usecase of python with your understanding .
# #1.Prediction of cricket score
# #2.Health care : disease detection and diagnosis, 
# #3.Crimanals Phsycology Analysis
# #4.Children behaviour analysis
# #5.popping the contents based on interest of person
# #6.In animal husbandary
# #7.AI based customer choice on decorative items
# #8.AI based e-farming 
# #9.E-garbage system management
# #10.Autonoumus vehicle,driverless car
# #11.Vision based biomatric signature
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




