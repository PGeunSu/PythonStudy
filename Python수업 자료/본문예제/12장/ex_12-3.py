#!/usr/bin/env python
# coding: utf-8

"""
12.3 Data Formatting
(p.188 ~ p.191)
"""

# In[1]: p.188
import numpy as np
import pandas as pd
price = np.random.randint(100, size=8)*10000
cars = pd.DataFrame(price, columns=['price'])
cars


# In[2]: p.189
import numpy as np
import pandas as pd
price = np.random.randint(100, size=8)*10000
cars = pd.DataFrame(price, columns=['price'])

group_names = ['저급', '중급', '고급']
cars['Level'], mybin = pd.cut(cars['price'], 3, labels=group_names, retbins=True)
cars


# In[3]:
cars['Level'] = pd.cut(cars['price'], 3, labels=group_names)


# In[4]:
cars['Level'], mybin = pd.cut(cars['price'], 3, labels=group_names,
retbins=True)


# In[5]: p.190
print(mybin)


# In[6]:
import pandas as pd
import numpy as np
ary = [[1, 1.1, '손'], [2, 2.2, '날개'], [3, 3.3, '손']]
data = pd.DataFrame(ary, columns=['수온', '상온', 'hand'])
pd.get_dummies(data['hand'])


# In[7]: p.191
import pandas as pd
import numpy as np
ary = [[1, 1.1, '손'], [2, 2.2, '날개'], [3, 3.3, '손']]
data = pd.DataFrame(ary, columns=['수온', '상온', 'hand'])
data = pd.concat([data, pd.get_dummies(data['hand'])], axis=1, sort=False)
data


# In[8]:
import pandas as pd
import numpy as np
ary = [[1, 1.1, '손'], [2, 2.2, '날개'], [3, 3.3, '손']]
data = pd.DataFrame(ary, columns=['수온', '상온', 'hand'])
data = pd.concat([data, pd.get_dummies(data['hand'])], axis=1, sort=False)
data.drop(['hand'], axis=1, inplace=True)
data

