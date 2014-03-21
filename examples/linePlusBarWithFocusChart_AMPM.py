#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import linePlusBarWithFocusChart

#Open File for test
output_file = open('test_linePlusBarWithFocusChart_AMPM.html', 'w')
#---------------------------------------
type = "linePlusBarWithFocusChart"
chart = linePlusBarWithFocusChart(name=type, x_is_date=False, x_axis_format="AM_PM")
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

xdata = [i for i in range(0, 24)]
ydata = [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 4, 3, 3, 5, 7, 5, 3, 16, 6, 9, 15, 4, 12]
ydata2 = [9, 8, 11, 8, 3, 7, 10, 8, 6, 6, 9, 6, 5, 4, 3, 10, 0, 6, 3, 1, 0, 0, 0, 1]
ydata3 = [9, 8, 15, 8, 4, 7, 20, 8, 4, 6, 0, 4, 5, 7, 3, 15, 30, 6, 3, 1, 0, 0, 0, 1]


extra_serie_1 = {
    "tooltip": {"y_start": "$ ", "y_end": ""},
    "date_format": "",
}
kwargs = {"bar": "true"}
chart.add_serie(name="serie 1", y=ydata, x=xdata, extra=extra_serie_1, **kwargs)

extra_serie_2 = {
    "tooltip": {"y_start": "$ ", "y_end": ""},
    "date_format": "",
}
chart.add_serie(name="serie 2", y=ydata2, x=xdata, extra=extra_serie_2)

extra_serie_3 = {
    "tooltip": {"y_start": "$ ", "y_end": ""},
    "date_format": "",
}
chart.add_serie(name="serie 3", y=ydata3, x=xdata, extra=extra_serie_3)

chart.buildhtml()

output_file.write(chart.htmlcontent)

#close Html file
output_file.close()
