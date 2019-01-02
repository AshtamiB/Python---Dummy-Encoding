# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 03:43:20 2018

@author: Ashtami
"""

from statsmodels.tools import categorical
import numpy as np
a = np.array(['Type1', 'Type2', 'Type3', 'Type1', 'Type2', 'Type3'])
cat_encod = categorical(a, dictnames=False, drop=True) #a.values
print(a.reshape(-1,1))
print(cat_encod)