#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 15:22:32 2017
@author: christophergreen
simplest scatter plots


import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (12*np.random.rand(N))**2 

plt.scatter(x, y, s=area, c=colors, alpha=0.8)
plt.show()


rand_data = np.random.rand(10,10)

print (rand_data)
"""

import numpy as np
import mathplot.plotly as plt

p = list(np.random.rand(50))
q = list(np.random.rand(50))


