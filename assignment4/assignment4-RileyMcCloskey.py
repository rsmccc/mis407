# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:38:15 2015

@author: rsmccloskey
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

import pandas as pd
import xlrd

def f(x):
    return ss.norm.cdf(x, loc = 18, scale = 0.09)

# Read Excel worksheet

wb = xlrd.open_workbook('../../ClassWork/SuperstoreSales.xlsx')
sheet = wb.sheet_by_index(0) ## orders
df1 = pd.read_excel(wb, sheetname='Orders', engine='xlrd')
returns = wb.sheet_by_name('Returns')
users = wb.sheet_by_name('Users')


quantity = []
sales = []
for i in range(sheet.nrows):
    if i > 0:
      quantity.append(int(sheet.cell(i,4).value))
      sales.append(int(sheet.cell(i,5).value))
    
def summary(data):
    print('Count: %d' % (np.ma.size(data)))
    print('Max: %d' % (np.amax(data)))
    print('Min: %d' % (np.amin(data)))
    print('Mean: %d' % (np.mean(data)))
    print('Stdev: %d' % (np.std(data)))

print('QUANTITY')
summary(quantity)

print('\nSALES')
summary(sales)

plt.hist(quantity, bins =(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50))
plt.hist(sales, bins = (0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000))
