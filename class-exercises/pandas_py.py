# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:26:51 2015

@author: rsmccloskey
"""

# more panda exploration

import pandas as pd
import xlrd

wb = xlrd.open_workbook('/Users/rsmccloskey/Development/python/ClassWork/SuperstoreSales.xlsx')

orders = pd.read_excel(wb, sheetname='Orders', index_col='Order Date', engine='xlrd')

print (orders)