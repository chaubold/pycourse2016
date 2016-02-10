# -*- coding: utf-8 -*-
"""
Created on Wed Feb  10 8:16:08 2016

@author: chaubold
"""
import numpy as np


def doStuffThatTakesLong():
    value = 0.0
    for i in range(1,10**3):
        value = value + np.sqrt(np.abs(np.sin(np.log(i))))

# this only works when run in the ipython console on the right
# (e.g. by choosing Run->Run Selection or Current Line)
#%timeit doStuffThatTakesLong()

# if you need to execute several lines, use double %, 
# then it applies to the whole code block you run
# (e.g. select and then press F9)
#%%timeit
#value = 0.0
#for i in range(1,10**3):
#    value = value + np.sqrt(np.log(np.sin(np.log(i))))

import timeit
# using the timeit module:
# you only use either a string of pure python statements 
# (no own functions/variables will be known!):
timeit.timeit('sum(range(10**7))', number=3)

# or you can pass in a function that doesn't expect any arguments
# and time that.
# NOTE: the method will be calles 'number' times 
# and the runtime averaged
timeit.timeit(doStuffThatTakesLong, number=3)

# what can we do if we want to time a method 
# that takes arguments?
def doStuffWithArguments(numIterations):
    value = 0.0
    for i in range(1,numIterations):
        value = value + np.sqrt(np.abs(np.sin(np.log(i))))

#timeit.timeit(doStuffWithArguments, number=3)
# gives: TypeError: doStuffWithArguments() missing 1 required 
#        positional argument: 'numIterations'

# write a small wrapper method that specifies arguments!
def wrapper():
    doStuffWithArguments(10**4)

# time that
timeit.timeit(wrapper, number=3)