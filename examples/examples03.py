#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import multiBarHorizontalChart
import random

#Open File for test
output_file = open('test3.html', 'w')

type = "multiBarHorizontalChart"
chart = multiBarHorizontalChart(name=type, height=350)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
chart.set_custom_tooltip_flag(True)
chart.build_custom_tooltip(x_start='', x_end='', y_start='', y_end='')
nb_element = 10
xdata = range(nb_element)
ydata = [random.randint(-10, 10) for i in range(nb_element)]
ydata2 = map(lambda x: x * 2, ydata)
chart.add_serie(y=ydata, x=xdata)
chart.add_serie(y=ydata2, x=xdata)
chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------
#close Html file
output_file.close()
