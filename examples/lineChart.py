#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import lineChart
import math

#Open File for test
output_file = open('test_lineChart.html', 'w')
#---------------------------------------
type = "lineChart"
chart = lineChart(name=type, date=False, x_axis_date_format="AM_PM")

xdata = []
ydata = []
ydata2 = []

ydata = [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 4, 3, 3, 5, 7, 5, 3, 16, 6, 9, 15, 4, 12]
ydata2 = [9, 8, 11, 8, 3, 7, 10, 8, 6, 6, 9, 6, 5, 4, 3, 10, 0, 6, 3, 1, 0, 0, 0, 1]
#ydata3 = [0, 0, 1, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 24):
    xdata.append(i)
#for i in range(0, 101):
#    xdata.append(i)
#    x = i * 0.1
#    ydata.append(math.sin(math.pi * x))
#    ydata2.append(0.5 * math.cos(math.pi * x))

kwargs1 = {'color': 'black'}
kwargs2 = {'color': 'red'}
extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}
chart.add_serie(y=ydata, x=xdata, name='sine',  extra=extra_serie, **kwargs1)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=ydata2, x=xdata, name='cose', extra=extra_serie, **kwargs2)

chart.buildhtml()

output_file.write(chart.htmlcontent)

#close Html file
output_file.close()
