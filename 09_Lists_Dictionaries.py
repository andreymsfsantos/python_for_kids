#!/usr/bin/env python
# coding: utf-8

# In[1]:


# three listis
fruit = ['apple', 'banana', 'kiwi', 'dragonfruit']
years = [2012, 2013, 2014, 2015]
students_in_class = [30, 22, 28, 33]
computer_class = ['Cynthia', 78, 42, 'Raj', 98, 24, 35, 'Kadeem', 'Rachel']


# In[2]:


print(type(fruit), type(years), type(students_in_class), type(computer_class))


# In[3]:


print('fruit:             ',type(fruit))
print('years:             ',type(years))
print('students_in_classt:',type(students_in_class))
print('computer_class:    ',type(computer_class))


# In[4]:


# Index:
#               ['apple', 'banana', 'kiwi', 'dragondfruit'] -
# Left to right     0         1        2           3        -
# Right to left    -4        -3       -2          -1        -
#------------------------------------------------------------
len(fruit) # lenght


# In[5]:


# List's Elements
fruit[1:len(fruit)]


# In[6]:


# Adding itemns to the list
fruit.append('orange')
print(fruit)


# In[7]:


# Removing itemns to the list
fruit.remove('dragonfruit') # or fruit.remove(fruit[3])
print(fruit)


# In[8]:


# List and Loops
colors = ['green', 'yellow', 'red']


# In[9]:


for color in colors:
    print('I see ' + color + '.')


# ## Dictionaries

# In[10]:


numbers = {'one': 1, 'two': 2, 'three': 3}


# In[13]:


print(numbers['one'])


# In[15]:


items = {'arrows': 200, 'rocks': 25, 'food': 15, 'lives': 2}


# In[16]:


type(items)


# In[17]:


items['fireball'] = 10


# In[18]:


print(items)


# In[20]:


# Changing the value of an existing item
items.update({'rocks': 10})
print(items)


# In[21]:


# Removing items from the dictionary
del items['lives']
print(items)


# In[ ]:




