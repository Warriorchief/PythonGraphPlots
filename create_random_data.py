#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 10:36:30 2017

@author: christophergreen
"""

import random
import math
import matplotlib.pyplot as plt
import numpy as np

def create_random_square_chart(square_dim):
    xouts=list(range(1,square_dim+1))
    youts=[]
    i=0
    while i<square_dim:
        youts.append(math.floor(random.randint(0,square_dim)))
        i+=1;
    #print ("xouts is:",xouts)
    #print ("youts is:", youts)
      
    area = np.pi * (15 * np.random.rand(square_dim))**2
    color = np.random.rand(square_dim)
    plt.scatter(xouts,youts,s=area,c=color)
    plt.xlabel("random xs")
    plt.ylabel("random ys")
    
    return plt.show()
    
create_random_square_chart(100) 


