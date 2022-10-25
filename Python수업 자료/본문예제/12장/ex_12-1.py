#!/usr/bin/env python
# coding: utf-8

"""
12.1 빅데이터의 가공
(p.182 ~ p.185)
"""

# In[1]: p.182
import pandas as pd
import numpy as np
from numpy import NaN
data = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])
data.D[2] = 'NaN'
data


# In[2]: p.183
data.drop(['D'], axis=1)


# In[3]:
import pandas as pd
robots = [[24, 23680], [35, NaN], [46, 47350], [27, NaN]]


# In[4]:
import pandas as pd
from numpy import NaN
robots = [[24, 23680], [35, NaN], [46, 47350], [27, NaN]]
print(robots)


# In[5]: p.184
import pandas as pd
from numpy import NaN
robots = [[24, 23680], [35, NaN], [46, 47350], [27, NaN]]
data = pd.DataFrame(robots, columns=['max_speed', 'price'])
print(data)


# In[6]:
data.dropna(subset=['price'], axis=0, inplace=True)
print(data)


# In[7]: p.185
import pandas as pd
from numpy import NaN
robots = [[24, 23680], [35, NaN], [46, 47350], [27, NaN]]
data = pd.DataFrame(robots, columns=['max_speed', 'price'])
mean = data['price'].mean()
data.replace(NaN, mean)
print(data)


# In[8]:
data = data.replace(NaN, mean)  # 또는 data.replace(NaN, mean, inplace=True)
print(data)




