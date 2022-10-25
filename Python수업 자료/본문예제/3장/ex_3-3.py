#!/usr/bin/env python
# coding: utf-8

"""
3.3 break/continue
(p.46)
"""

# In[1]: p.46
sum = 0
for i in range(100):
    sum += i
    if (sum > 100):
        break
print('sum=', sum, ', i=', i)


# In[2]:
sum = 0
for i in range(100):
    if (sum > 100):
        continue
    sum += i
print('sum =', sum, ', i =', i)

