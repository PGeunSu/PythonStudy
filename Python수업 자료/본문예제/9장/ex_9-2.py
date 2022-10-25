#!/usr/bin/env python
# coding: utf-8

"""
9.2 Numpy의 기초
(p.144 ~ p.157)
"""

# In[1]: p.144
x = [1, 3, 5]
x.mean()


# In[2]:
import numpy as np
x = np.array([1, 3, 5])
print(x.mean())  # 3.0 출력


# In[3]: p.145
print(x.shape)  # (3,) 출력


# In[4]:
a = np.array([[1, 2, 3], [2, 3, 4]])


# In[5]:
x = np.array([1, 3, 5])


# In[6]:
x = np.array([1, 3, 5, 7, 9, 11]).reshape(3, 2)
print(x)


# In[7]: p.146
y = np.ones([3, 4])
print(y)


# In[8]:
x = np.array([[1, 3, 5], [2, 4, 6]])
print(x[1])  # [2 4 6] 출력
print(x[1].mean())  # 4.0 출력
print(x.mean())  # 3.5 출력
print(x.shape)  # (2, 3) 출력


# In[9]:
list1 = [[1, 11], [2, 12], [3, 13]]
print(list1[:][1])  # 의도하지 않은 결과 출력
print(list1[:, 1])  # Error 발생


# In[10]: p.147
import numpy as np
list1 = [[1, 11], [2, 12], [3, 13]]
np_ary = np.array(list1)
print(np_ary[:, 1])


# In[11]:
import numpy as np
list1 = [[1, 11], [2, 12], [3, 13]]
print(np.array(list1[:, 1]))


# In[12]:
import numpy as np
list1 = np.array([[1, 11], [2, 12], [3, 13]])
print(list1[:, 1])


# In[13]: p.148
import numpy as np
list1 = [[1, 11], [2, 12], [3, 13]]
print(np.array(list1[:, 1]))


# In[14]:
import math
math.sqrt(2)


# In[15]:
math.sqrt([2, 3, 4])


# In[16]: p.149
import numpy as np
np.sqrt([2, 3, 4])


# In[17]:
import numpy as np
a = np.arange(15)
print(a)


# In[18]:
import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)


# In[19]: p.150
import numpy as np
zero_vector = np.zeros(3)
print(zero_vector)


# In[20]:
zero_matrix = np.zeros((4, 3))
print(zero_matrix)


# In[21]:
zero_vector = np.zeros(5)
zero_vector


# In[22]:
zero_matrix = np.zeros((5,3))
zero_matrix


# In[23]:
import numpy as np
my_array = np.zeros(15).reshape(3,5)
my_array += 4
my_array


# In[24]: p.151
ary = [[1,2], [3,4]]
print(ary.transpose())


# In[25]:
import numpy as np
ary = np.array([[1, 2], [3, 4]])
print(ary.transpose())


# In[26]: p.152
import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
z = x * y
print(z)


# In[27]:
s = [1, 2, 3]
t = s + 1
print(t)


# In[28]:
s = np.array([1, 2, 3])
t = s + 1
print(t)


# In[29]: p.153
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(X[1])  # [4 5 6] 출력 (X배열의 인덱스 1번의 내용을 출력)
print(X[:, 1])  # [2 5 8] 출력 (각 1차원 배열의 1번의 내용을 출력)


# In[30]:
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Y = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
print(X[:,1]+Y[:,1])


# In[31]: p.154
a = np.array([10, 20, 30, 40, 50, 60, 70])
i = [1, 3, 5]
print(a[i])


# In[32]: p.155
import numpy as np
a = np.array([10, 20, 30, 40, 50, 60, 70])
b = np.array(a[1:6:2])
print('b:', b)
b[1] = 10
print('b:', b)
print('a:', a)
type(b)


# In[33]:
a = np.array([10, 20, 30, 40, 50, 60, 70])
b = a > 50  # [False False False False True True True]의 값을 갖는 Numpy 배열이 b의 이름으로 저장됨.
print(b)


# In[34]:
ary = np.random.random(5)
print(ary)
print(np.all(ary >= 0.3))
print(np.any(ary > 0.7))


# In[35]: p.157
np.linspace(0, 12, 4)


# In[36]:
np.linspace(0, 12, 4, retstep=True)


# In[37]:
np.linspace(0, 12, 3, endpoint=False)


# In[38]:
np.logspace(np.log10(10), np.log10(100), 5)


# In[39]:
np.logspace(1, 2, 5)

