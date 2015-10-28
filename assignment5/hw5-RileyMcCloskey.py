# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:29:32 2015

@author: rsmccloskey
"""

import numpy as np

#1.	Read the first sheet of the excel file into a data frame, named df. Maintain Order Date field as the index.

import pandas as pd
import xlrd

wb = xlrd.open_workbook('/Users/rsmccloskey/Development/python/ClassWork/SuperstoreSales.xlsx')

df = pd.read_excel(wb, sheetname='Orders', index_col='Order Date', engine='xlrd')

#2.	Print the names of all columns.
print ('\nColumn Names')
for col in df.columns:
  print (col)

#3.	For the columns that have duplicate or repeating values, print the unique values for those columns.
## Order (Priority, Ship Mode, Province, Region, Customer Segment, Product Category, Product Sub-Category, Product Container

dCols = ['Order Priority', 'Ship Mode', 'Province', 'Region', 'Customer Segment', 'Product Category', 
         'Product Sub-Category', 'Product Container']

for col in dCols:
  uCol = pd.unique(df[col].ravel())
  print ('\n' + col)
  for val in uCol:
    print ('\t' + val)

#4.	By Product Category, show the mean sales and mean profit.

sales = df['Sales'].groupby(df['Product Category'])
profit = df['Profit'].groupby(df['Product Category'])

print ('\nMean Sales by Product Category')
print (sales.mean())
print ('\nMean Profit by Product Category')
print (profit.mean())

#5.	Order sales collected by Customer Segment.

print ('\nSales by Customer Segment')
print (df['Sales'].groupby(df['Customer Segment']).sum())

#6.	What is the average time it takes to ship an order?

df['Order Date'] = np.copy(df.index)

df['Lead Time'] = df['Ship Date'] - df['Order Date']

print ('\nAverage time to ship an order')
print (df['Lead Time'].mean())

#7.	What is the average cost per sales for each customer segment?
print ('\nAverage Shipping Cost per Sale by Customer Segment')
print (df['Shipping Cost'].groupby(df['Customer Segment']).mean())


