#!/usr/bin/env python
# coding: utf-8

"""
4.1 사용자 정의 함수
(p.48 ~ p.52)
"""

# In[1]: p.49
def double(num):
    print(num, '의 제곱:', num*num)
double(3)


# In[2]:
def hello():
    print('Hello!')
hello()


# In[3]: p.50
def double(num):
    return num*num
result = double(3)
print('%d의 제곱: %d' % (3, result))


# In[4]:
def double(n):
    square = n * n
    return square
print(double(7))


# In[5]:
def add(a, b):
    sum = a + b
    return sum
print(add(3, 5))


# In[6]: p.51
def add_sub(a, b):
    sum = a + b
    diff = a - b
    return sum, diff
print(add_sub(3, 5))


# In[7]:
def swap(a, b):  # 함수 swap 정의
    temp = a
    a = b
    b = temp
a=3
b=5
swap(a, b)
print('a =', a, ', b =', b)


# In[8]:
def swap(a, b):
    return b, a
a=3
b=5
a, b = swap(a, b)
print('a=', a, 'b=', b)

