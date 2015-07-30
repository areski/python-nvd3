#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import stackedAreaChart

# Open File for test
output_file = open('test_StackedAreaChart.html', 'w')

chart = stackedAreaChart(name='stackedAreaChart', height=400, width=400)

xdata = [100, 101, 102, 103, 104, 105, 106]
ydata = [6, 11, 12, 7, 11, 10, 11]
ydata2 = [8, 20, 16, 12, 20, 28, 28]

extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " min"}}
chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie)
chart.add_serie(name="Serie 2", y=ydata2, x=xdata, extra=extra_serie)
chart.buildhtml()

output_file.write(chart.htmlcontent)

output_file.close()
