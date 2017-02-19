#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 01:08:10 2017

@author: christophergreen
"""

import random
import matplotlib.pyplot as plt
 
def how_long_to_equal(maxim):
    counter = 0
    while True:
        d = random.randint(1,maxim)
        e = random.randint(1,maxim)
        if d!=e:
            counter +=1
        else: 
            break
    #print("it took",counter,"trials.")
    return counter

def ave_time(maxim,numtrials):
    i=0
    outs=[]
    while i<numtrials:
        outs.append(how_long_to_equal(maxim))
        i+=1
    print("")
    print("outs is:",outs)
    return outs
    

y=ave_time(10**4,35)
N = len(y)
x = range(N)
width=1/3
plt.axhline(y=10**4,linewidth=3, xmin=0,xmax=N, color='blue')
plt.bar(x,y, width, color="red")
plt.xlabel('trial')
plt.ylabel('num guesses')

plt.title('trials needed to guess')

