# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:24:39 2015

@author: rsmccloskey
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

import pandas as pd
import xlrd

## Reference wrkfile.py

# Make a normal distribution with mean of 18 and standard deviation of 0.09

# ss.norm(loc = 18, scale = 0.09)
# to get the cumulative distribution function
# ss.norm.cdf(x, loc = 18, scale = 0.09)

def f(x):
    return ss.norm.cdf(x, loc = 18, scale = 0.09)

# Read Excel worksheet

wb = xlrd.open_workbook('../../ClassWork/SuperstoreSales.xlsx')
sheet = wb.sheet_by_index(0) ## orders
df1 = pd.read_excel(wb, sheetname='Orders', engine='xlrd')
returns = wb.sheet_by_name('Returns')
users = wb.sheet_by_name('Users')


myList = []
for i in range(sheet.nrows):
    if i > 0:
      myList.append(int(sheet.cell(i,0).value))
    
def summary(data):
    print('Max: %d' % (np.amax(data)))
    print('Min: %d' % (np.amin(data)))
    print('Mean: %d' % (np.mean(data)))
    print('Stdev: %d' % (np.std(data)))

summary(myList)

plt.hist(myList, bins =(30, 35, 40, 45, 50, 55, 60))


