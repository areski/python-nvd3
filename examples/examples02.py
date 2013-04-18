#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import lineChart, scatterChart, multiBarHorizontalChart
import math
import random

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
chart.set_custom_tooltip_flag(True)
chart.build_custom_tooltip()
chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------
"""
type = "scatterChart"
chart = scatterChart(name=type, height=350, date=False)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
nb_element = 50
xdata = [i + random.randint(1, 10) for i in range(nb_element)]
ydata = [i * random.randint(1, 10) for i in range(nb_element)]
ydata2 = map(lambda x: x * 2, ydata)
ydata3 = map(lambda x: x * 5, ydata)

kwargs1 = {'shape': 'circle'}
kwargs2 = {'shape': 'cross'}
kwargs3 = {'shape': 'triangle-up'}

chart.add_serie(name="serie 1", y=ydata, x=xdata, **kwargs1)
chart.add_serie(name="serie 2", y=ydata2, x=xdata, **kwargs2)
chart.add_serie(name="serie 3", y=ydata3, x=xdata, **kwargs3)

chart.buildhtml()
"""
output_file.write(chart.htmlcontent)
#---------------------------------------



#close Html file
output_file.close()
