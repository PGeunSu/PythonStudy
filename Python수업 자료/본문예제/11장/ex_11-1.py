#!/usr/bin/env python
# coding: utf-8

"""
11.1 Pandas의 기초
(p.172 ~ p.180)
"""

# In[1]: p.172
import pandas as pd
pd.Series([7, 3, 5, 8])


# In[2]:
x = pd.Series([7, 3, 5, 8], index=['서울', '대구', '부산', '광주'])
print(x)


# In[3]: p.173
x[['서울', '대구']]


# In[4]:
x.index


# In[5]:
x.values


# In[6]:
print(sorted(x.index))
print(sorted(x.values))


# In[7]:
sorted(x.values)


# In[8]:
x = x.reindex(sorted(x.index))
x


# In[9]:
x = pd.Series([3, 8, 5, 9], index=['서울', '대구', '부산', '광주'])
y = pd.Series([2, 4, 5, 1], index=['대구', '부산', '서울', '대전'])
x+y


# In[10]: p.174
medal = [1, 3, 2, 4, 2, 3]
x = pd.Series(medal)
print(pd.unique(x))


# In[11]:
medal = ['민준', '현우', '서연', '동현', '서연', '현우']
x = pd.Series(medal)
print(pd.unique(x))


# In[12]:
age = {'민준':23, '현우':43, '서연':12, '동현':45}
x = pd.Series(age)
x


# In[13]:
names = ['민준', '서연', '현우', '민서', '동현', '수빈']
pdata = pd.Series(names)
print(pdata)


# In[14]: p.175
a = pdata[3:6]
print(a.values)


# In[15]:
print(a)


# In[16]: p.176
data = {'age' : [23, 43, 12, 45],
        'name' : ['민준', '현우', '서연', '동현'],
        'height' : [175.3, 180.3, 165.8, 172.7]}
x = pd.DataFrame(data, columns = ['name', 'age', 'height'])
x


# In[17]:
x.name


# In[18]:
ary = [[1, 2], [3, 4], [5, 6]]
data = pd.DataFrame(ary, columns=['First', 'Second'])
data


# In[19]:
data.iloc[1]


# In[20]: p.177
data.iloc[:, -1]


# In[21]: 
ary = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
data = pd.DataFrame(ary, columns=['First', 'Second'])
data.head(3)


# In[22]:
data.tail(3)


# In[23]:
ary = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
data = pd.DataFrame(ary, columns=['First', 'Second'])
bools = [False, True, True, False, True]
data.Second[bools]


# In[24]: p.178
print(x.mean(axis=0))


# In[25]:
data = {'age' : [23, 43, 12, 45],
        'name' : ['민준', '현우', '서연', '동현'],
        'height' : [175.3, 180.3, 165.8, 172.7]}
x = pd.DataFrame(data, columns = ['name', 'age', 'height'])
index = [True, False, True, False]
print(x[index])


# In[26]: p.179
import pandas as pd
import numpy as np
ary = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
data = pd.DataFrame(ary, columns=['수온', '상온'])
data


# In[27]:
data['수온'] = data['수온'].astype('float')
data


# In[28]: p.180
import pandas as pd
food = pd.read_csv('food.csv')
food.head()


# In[29]:
import pandas as pd
accident = pd.read_csv('acci.csv')
accident


# In[30]:
import pandas as pd
accident = pd.read_csv('acci.csv', engine='python')
accident.head()

