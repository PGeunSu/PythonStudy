#!/usr/bin/env python
# coding: utf-8

"""
12.2 Binning/Normalization
(p.185 ~ p.188)
"""

# In[1]: p.186
import matplotlib.pyplot as plt
import numpy as np
x =np.random.randn(1000)
plt.hist(x, density=True, bins=np.linspace(-5, 5, 21))

