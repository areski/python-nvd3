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
output_file = open('test2.html', 'w')
#---------------------------------------
type = "lineChart"
chart = lineChart(name=type, date=False, height=350)

xdata = []
ydata = []
ydata2 = []

for i in range(0, 101):
    xdata.append(i)
    x = i * 0.1
    ydata.append(math.sin(math.pi * x))
    ydata2.append(0.5 * math.cos(math.pi * x))

extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}
chart.add_serie(y=ydata, x=xdata, name='sine', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=ydata2, x=xdata, name='cose', extra=extra_serie)

chart.buildhtml()

output_file.write(chart.htmlcontent)

#close Html file
output_file.close()
