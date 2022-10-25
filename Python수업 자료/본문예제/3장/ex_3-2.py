#!/usr/bin/env python
# coding: utf-8

"""
3.2 반복문
(p.38 ~ p.45)
"""

# In[1]: p.39
for i in range(3):
    print('안녕!')


# In[2]:
for _ in range(3):
    print('안녕!')


# In[3]:
for i in range(3):
    print(i)


# In[4]:
for i in range(2, 5):
    print(i)


# In[5]: p.40
for i in range(0, 7, 2):
    print(i)


# In[6]:
for i in range(6, -1, -2):
    print(i)


# In[7]: p.42
for i in range(3):
    for j in range(3):
        print('* ')


# In[8]:
for i in range(3):
    for j in range(3):
        print('* ', end='')


# In[9]: p.43
for i in range(3):
    for j in range(3):
        print('* ', end='')
    print('')


# In[10]:
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j, end=' ')
    print()


# In[11]: p.44
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j, end='\t')
    print()


# In[12]: p.45
i = 0
while (i<3):
    print(i)
    i = i+1

