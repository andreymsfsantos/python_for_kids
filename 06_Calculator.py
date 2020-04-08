#!/usr/bin/env python
# coding: utf-8

#  # First Calc

# In[1]:


def addition():
    first=float(input('I wiil add two numbers. Please, put the first number and press ENTER '))
    second=float(input('Now put the second number and press ENTER '))
    print(first + second)
def subtraction():
    first = float(input('I wiil subtract two numbers. Please, put on the first number and press ENTER '))
    second = float(input('Now put the second number and press ENTER '))
    print(first - second)
def multiplication():
    first = float(input('I) wiil multiply two numbers. Please, put on the first number and press ENTER '))
    second = float(input('Now put the second number and press ENTER '))
    print(first * second)
def division():
    first = float(input('I) wiil divide two numbers. Please, put on the first number and press ENTER '))
    second = float(input('Now put the second number and press ENTER '))
    print(first / second)


#  ## Condotional Statements

# In[2]:


def calc_run():
    op = input("Choose just one signal operation (+ - * /) and press ENTER ")
    if op == '+':
        addition()
    elif op == '-':
        subtraction()
    elif op == '*':
        multiplication()
    elif op == '/':
        division()
    else:print('just use signal: (+ - * /), try again!')


# In[ ]:


calc_run()


# In[ ]:




