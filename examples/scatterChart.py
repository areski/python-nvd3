#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import scatterChart
import random

#Open File for test
output_file = open('test_scatterChart.html', 'w')

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

extra_serie = {"tooltip": {"y_start": "", "y_end": " calls"}}
chart.add_serie(name="serie 1", y=ydata, x=xdata, extra=extra_serie, **kwargs1)
chart.add_serie(name="serie 2", y=ydata2, x=xdata, extra=extra_serie, **kwargs2)
chart.add_serie(name="serie 3", y=ydata3, x=xdata, extra=extra_serie, **kwargs3)

chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------

#close Html file
output_file.close()
