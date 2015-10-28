# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:07:54 2015

@author: rsmccloskey
"""

import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()
c.execute('SELECT * FROM person')
print (c.fetchall())

conn.close()

