#!/usr/bin/env python
# coding: utf-8

# In[98]:


def studentfunction(student_name):
    marks = {'Andy':88, 'Amy': 66, 'James': 90, 'Jules': 55, 'Arthur': 77}
    grade = 'N/A'
    for student in marks:
        if student == student_name:
            grade = marks[student]
    if grade != 'N/A':
        return grade
    else: 
        print('cannnot find student name')


# In[99]:


studentfunction('Jules')


# In[100]:


studentfunction('Lexie')


# In[114]:


def averagegrade(marks):
    cnt = 0
    for student in marks:
        cnt = cnt+ marks[student]
    return cnt/len(marks)
marks = {'Andy':88, 'Amy': 66, 'James': 90, 'Jules': 55, 'Arthur': 77}
averagegrade(marks)


# In[123]:


def numberfunction(n):
    num = 8
    while n < num:
        print(n, n**2)
        n+=1
        break
    else:
        print("greater than", num)


# In[125]:


numberfunction(4)
numberfunction(9)


# In[78]:


def integers(num):
    n= 1
    sum = 0
    while n<=num:
        sum = sum+n
        n=n+1
    print(sum)


# In[79]:


integers(30)


# In[126]:


def questionfour(num):
    sum = 0
    for n in range(num):
        sum = sum +n
        print(sum)
questionfour(33)


# In[179]:


import numpy as np
lst = []
for i in range(99):
    lst.append(i+1)
def lstfunc(lst):
    return sum(lst)/len(lst), sum(lst), np.std(lst)
lstfunc(lst)
#my notebook is not letting me call range so i had to use this way instead


# In[187]:


def minimal(v1, v2, v3, v4):
    current_min = v1
    if v2 < current_min:
        current_min = v2
    if v3 < current_min:
        current_min = v3
    if v4 < current_min:
        current_min = v4
    return current_min
minfunc(9,3,4,1)


# In[186]:


def concat(str1, str2, str3):
    string = str1 + str2 + str3
    print(string)
    return string
concat('lex', 'iz', 'blizz')

