#!/usr/bin/env python
# coding: utf-8

# ###  Task4 _28th May  .....by Dr.Tanuja S.Dhope

# In[ ]:


q1 :
ineruon 
ineruon ineruon 
ineruon ineruon ineruon
ineruon ineruon ineruon ineruon

q2 - 

          ineruon
    ineruon      ineruon
ineruon		ineruon 	ineruon
	ineruon		 ineruon
		  ineruon

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

q3 : Try to extract all the list entity 
q4 : Try to extract all the dict enteties
q5 : Try to extract all the tuples entities
q6 : Try to extract all the numerical data it may b a part of dict key and values 
q7 : Try to give summation of all the numeric data 
q8 : Try to filter out all the odd values out all numeric data which is a part of a list 
q9 : Try to extract "ineruon" out of this data
q10 : Try to find out a number of occurances of all the data 
q11 : Try to find out number of keys in dict element
q12 : Try to filter out all the string data 
q13 : Try to Find  out alphanum in data
q14 : Try to find out multiplication of all numeric value in the individual collection inside dataset


# In[ ]:





# #### Q1 :
# #### ineruon 
# #### ineruon ineruon 
# #### ineruon ineruon ineruon
# #### ineruon ineruon ineruon ineruon

# In[1]:


count=4
for i in range (count):
    for j in range(0,i+1):
        print('ineuron',end="     ")
    print('\n')
    


# In[2]:


n = 4 
for i in range(4) :
    for j in range(0 ,i+1) : 
        print("star" , end = "     ")
    print("\n")


# #### Q2 - 
# 
# ######                      ineruon
# ####             ineruon      ineruon
# ####      ineruon  ineruon 	ineruon
# ####      	 ineruon		 ineruon
# #### 	                ineruon

# In[3]:


for i in range(6):
    if i<=3:
        n=i
    else:
        n=6-i
    print(("ineuron "* n).center(20," "))


# In[ ]:





# 

# In[4]:


l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]


# In[5]:


l


# ### Q3 : Try to extract all the list entity 

# In[6]:


for i in l:
    if type(i)==list:
        print(i)


# ### Q4 : Try to extract all the dict enteties

# In[7]:


for i in l:
    if type(i)==dict:
        print(i)


# ### Q5 : Try to extract all the tuples entities

# In[8]:


for i in l:
    if type(i)==tuple:
        print(i)


# ### Q6 : Try to extract all the numerical data it may b a part of dict key and values 

# In[ ]:





# In[9]:


l1=[]
for i in l:
    if type(i)==list or type(i)==tuple or type(i)==set:
        for j in i:
            if type(j)==int:
                l1.append(j)
                
    if type(i)==dict:
        for k in i.values():
                if type(k)==int :
                    l1.append(k)
print(l1) 


# In[10]:


### Q7 : Try to give summation of all the numeric data


# In[11]:


sum=0
for i in l1:
    sum+=i
sum


# ### Q8 : Try to filter out all the odd values out all numeric data which is a part of a list

# In[12]:


for i in l1:
    if i%2==0:
        pass
    else:
        print(i,end=" ")


# ### Q9 : Try to extract "ineruon" out of this data

# In[13]:


l2=[]
for i in l:
    if type(i)==list: 
        for j in i:
            if type(j)== str and (j=='ineuron'):
                l2.append(j)
                
    if type(i)==dict:
        for k in i.values():
                 if type(k)== str and (k=='ineuron'):
                    l2.append(k)
print(l2) 


# ### Q10 : Try to find out a number of occurances of all the data 

# In[14]:


l3=[]
for i in l:
    if type(i) == list or type(i) == tuple or type(i) == set:
        for j in i:
            if type(j) == int or  type(j) == str :
                l3.append(j)            
    if type(i)==dict:
        for k in i.values():
                if type(k)==int or type(j)==str :
                    l3.append(k)

print(l3) 


# In[ ]:





# In[15]:


l4 = []
for i in l:
    if type(i) == list or type(i) == tuple or type(i) == set :
        for j in i :
            if type(j) == int or type(j) == str:
                l4.append(j)
    if type(i) == dict :
        for k in i.items() : 
            for g in k :
                if type(g) == int  or type(g) == str:
                    l4.append(g)
l4                    
                    


# In[16]:


l5 = []
for i in l:
    if type(i) == list or type(i) == tuple or type(i) == set :
        for j in i :
            if type(j) == int or type(j) == str:
                l5.append(j)
    if type(i) == dict :
        for k in i.values() : 
                if type(k) == int  or type(k) == str:
                    l5.append(k)
l5   


# In[17]:


for i in set(l5):
    print(i,":",l5.count(i))


# ### Q11 : Try to find out number of keys in dict element

# In[18]:



count=0
for i in l:
    if type(i) == dict :
        for k in i.keys() : 
                count+=1
count  


# ### Q12 : Try to filter out all the string data 

# In[19]:


l6= []
for i in l:
    if type(i) == list or type(i) == tuple or type(i) == set :
        for j in i :
            if  type(j) == str:
                l6.append(j)
    if type(i) == dict :
        for k in i.values() : 
                if type(k) == str:
                    l6.append(k)
l6         


# In[20]:


### Q13 : Try to Find  out alphanum in data


# In[21]:


for i in l4:
     if type(i) == str:
            if i.isalnum():
                print(i)


# ### Q14 : Try to find out multiplication of all numeric value in  the individual collection inside dataset 

# In[38]:


### individual 
l7= []
num=1
for i in l:
    if type(i) == list:
        for j in i :
                if  type(j) == int:
                    num*=j
l7.append(num)                 
l7
num=1
for i in l:
    if type(i) == tuple:
        for j in i :
                if  type(j) == int:
                    num*=j
l7.append(num)                 
l7    
num=1
for i in l:
    if type(i) == set:
        for j in i :
                if  type(j) == int:
                    num*=j
l7.append(num)                 
l7    
num=1
for i in l:
    if type(i) == dict:
        for k in i.values():
                if  type(k) == int:
                    num*=k
l7.append(num)                 
l7                 


# In[57]:


### individual 
l7= []
num=1
for i in l:
    if type(i) == list or type(i) == tuple or type(i) == set:
        for j in i :
                if  type(j) == int:
                    num*=j
        print(type(i),num)
        num=1
    if type(i) == dict:
        for k in i.values():
                if  type(k) == int:
                    num*=k
        print(type(i),num)
        num=1
        
### Colletively
num1=1
for i in l4:
     if  type(i) == int:
            num1*=i
num1           


# In[ ]:



                


# In[ ]:





# In[ ]:





# In[ ]:




