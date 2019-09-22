#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('istherecorrelation.csv', delimiter=';')

data[['WO [x1000]']] = data[['WO [x1000]']].apply(lambda x: x.str.replace(',','.'))
data[['WO [x1000]']]= pd.to_numeric(data['WO [x1000]'], errors = 'coerce')

x = data['WO [x1000]']
y = data['NL Beer consumption [x1000 hectoliter]']
year = data['Year']
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

plt.plot(x,p(x),"r--")
plt.scatter(x,y)
plt.xlabel('WO students (x1000)')
plt.ylabel('NL beer consumption (x 100 kiloliter)')

plt.savefig('figure_beer.png', DPI = 300)


