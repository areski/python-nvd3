#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import multiChart

# Open File for test
output_file = open('test_multiChart.html', 'w')
# ---------------------------------------
chart_name = "multiChart"
chart = multiChart(name=chart_name, x_is_date=False, x_axis_format="AM_PM")

xdata = [1,2,3,4,5,6]
ydata = [115.5,160.5,108,145.5,84,70.5]
ydata2 = [48624,42944,43439,24194,38440,31651]

kwargs1 = {'color': 'black'}
kwargs2 = {'color': 'red'}
extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}
chart.add_serie(y=ydata, x=xdata, type='line', yaxis=1, name='visits', extra=extra_serie, **kwargs1)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=ydata2, x=xdata, type='bar', yaxis=2,name='spend', extra=extra_serie, **kwargs2)

chart.buildhtml()

output_file.write(chart.htmlcontent)

# close Html file
output_file.close()
