#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import lineWithFocusChart
import random
import datetime
import time


start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
nb_element = 100

#Open File for test
output_file = open('test_lineWithFocusChart.html', 'w')
#---------------------------------------
type = "lineWithFocusChart"
chart = lineWithFocusChart(name=type, color_category='category20b', date=True, x_axis_date_format="%d %b %Y %H")
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

xdata = range(nb_element)
xdata = map(lambda x: start_time + x * 1000000000, xdata)
ydata = [i + random.randint(-10, 10) for i in range(nb_element)]

ydata2 = map(lambda x: x * 2, ydata)
ydata3 = map(lambda x: x * 3, ydata)
ydata4 = map(lambda x: x * 4, ydata)

extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"},
               "date_format": "%d %b %Y %H:%M:%S %p"}
#extra_serie = None
chart.add_serie(name="serie 1", y=ydata, x=xdata, extra=extra_serie)
chart.add_serie(name="serie 2", y=ydata2, x=xdata, extra=extra_serie)
chart.add_serie(name="serie 3", y=ydata3, x=xdata, extra=extra_serie)
chart.add_serie(name="serie 4", y=ydata4, x=xdata, extra=extra_serie)

chart.buildhtml()

output_file.write(chart.htmlcontent)

#close Html file
output_file.close()
