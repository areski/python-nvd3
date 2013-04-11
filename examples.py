#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""
import nvd3
import random
import datetime
import time

#Open File for test
output_file = open('test.html', 'w')
#---------------------------------------
type = "lineChart"
chart = nvd3.lineChart(name=type, date=True, height=350)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)

nb_element = 100
xdata = range(nb_element)
xdata = map(lambda x: start_time + x * 1000000000, xdata)
ydata = [i + random.randint(1, 10) for i in range(nb_element)]
ydata2 = map(lambda x: x * 2, ydata)

chart.add_serie(y=ydata, x=xdata)
chart.add_serie(y=ydata2, x=xdata)
chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------
type = "lineWithFocusChart"
chart = nvd3.lineWithFocusChart(name=type, date=True)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
nb_element = 100
xdata = range(nb_element)
xdata = map(lambda x: start_time + x * 1000000000, xdata)
ydata = [i + random.randint(-10, 10) for i in range(nb_element)]
#ydata = [1, 2, 3, 4, 5, 3, 4, 5, 5, 3, 4, 5, 5, 3, 4, 5]
ydata2 = map(lambda x: x * 2, ydata)
ydata3 = map(lambda x: x * 3, ydata)
ydata4 = map(lambda x: x * 4, ydata)

# for w in Waves:
#     chart.add(w, x=Date)
chart.add_serie(y=ydata, x=xdata)
chart.add_serie(y=ydata2, x=xdata)
chart.add_serie(y=ydata3, x=xdata)
chart.add_serie(y=ydata4, x=xdata)
chart.buildhtml()

output_file.write(chart.htmlcontent)

#---------------------------------------
type = "stackedAreaChart"
chart = nvd3.stackedAreaChart(name=type, height=350)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
nb_element = 100
xdata = range(nb_element)
xdata = map(lambda x: 100 + x, xdata)
ydata = [i + random.randint(1, 10) for i in range(nb_element)]
ydata2 = map(lambda x: x * 2, ydata)

# for w in Waves:
#     chart.add(w, x=Date)
chart.add_serie(y=ydata, x=xdata)
chart.add_serie(y=ydata2, x=xdata)
chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------

type = "multiBarHorizontalChart"
chart = nvd3.multiBarHorizontalChart(name=type, height=350)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
nb_element = 10
xdata = range(nb_element)
ydata = [random.randint(-10, 10) for i in range(nb_element)]
ydata2 = map(lambda x: x * 2, ydata)
chart.add_serie(y=ydata, x=xdata)
chart.add_serie(y=ydata2, x=xdata)
chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------

type = "pieChart"
chart = nvd3.pieChart(name=type, height=400, width=400)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
ydata = [3, 4, 0, 1, 5, 7, 3]

chart.add_serie(y=ydata, x=xdata)
chart.buildhtml()

output_file.write(chart.htmlcontent)
#---------------------------------------

#close Html file
output_file.close()
