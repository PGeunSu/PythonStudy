#!/usr/bin/env python
# coding: utf-8

"""
2.2 변수의 연산
(p.14 ~ p.20)
"""

# In[1]: p.15
a = 3  # 정수형
b = 3.5  # 실수형
a + b


# In[2]: p.16
a = 3
b = 5
a > b  # a는 b보다 크다.


# In[3]:
a < b  # a는 b보다 작다.


# In[4]:
a >= b  # a는 b보다 크거나 같다.


# In[5]:
a <= b  # a는 b보다 작거나 같다.


# In[6]:
a == b  # a는 b와 같다.


# In[7]:
a != b  # a는 b와 같지 않다.


# In[8]: p.18
a = 3
b = 5
(a > 0) and (a > b)  # a는 0보다 크고 a는 b보다 크다.


# In[9]:
a = 3
b = 5
(a > 0) or (a > b)  # a는 0보다 크거나 a는 b보다 크다.


# In[10]:
a = 3
not a  # 0이 아닌 수는 모두 True이기 때문에 a는 값이 3이므로 True이며 반대로 하여 False를 출력


# In[11]:
not (a > 0)  # not은 뒤에 저장된 값의 반대로, a가 0보다 크다는 참인데 반대로 하여 Flase를 출력

