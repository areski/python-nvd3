#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import discreteBarChart
from nvd3 import pieChart
from nvd3 import multiBarChart
import random

#Open File for test
output_file = open('test1.html', 'w')

type = "discreteBarChart"
chart = discreteBarChart(name=type, height=400, width=400)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
xdata = ["A", "B", "C", "D", "E", "F", "G"]
ydata = [3, 12, -10, 5, 35, -7, 2]

extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
chart.add_serie(name="discrete Bar", y=ydata, x=xdata, extra=extra_serie)
chart.set_custom_tooltip_flag(True)
chart.build_custom_tooltip()
chart.buildhtml()
output_file.write(chart.htmlcontent)
#---------------------------------------

type = "pieChart"
chart = pieChart(name=type, height=400, width=400)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
ydata = [3, 4, 0, 1, 5, 7, 3]

chart.add_serie(y=ydata, x=xdata)
chart.buildhtml()
output_file.write(chart.htmlcontent)
#---------------------------------------

type = "multiBarChart"
chart = multiBarChart(name=type, height=350)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
nb_element = 10
xdata = range(nb_element)
ydata = [random.randint(1, 10) for i in range(nb_element)]
ydata2 = map(lambda x: x * 2, ydata)
ydata3 = map(lambda x: x * 3, ydata)
ydata4 = map(lambda x: x * 4, ydata)

chart.add_serie(y=ydata, x=xdata)
chart.add_serie(y=ydata2, x=xdata)
#chart.add_serie(y=ydata3, x=xdata)
chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------

#close Html file
output_file.close()
