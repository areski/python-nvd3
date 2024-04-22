#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import multiBarChart
import random

# Open File for test
output_file = open('test_multiBarChart.html', 'w')

chart_name = "multiBarChart"
chart = multiBarChart(name=chart_name, height=350)
chart.set_containerheader("\n\n<h2>" + chart_name + "</h2>\n\n")
chart.callback = '''
                    function(){
                    d3.selectAll(".nv-bar").on('click',
                        function(d){
                        console.log("barchart_callback_test: clicked on bar " + JSON.stringify(d));
                        console.log('/app/call?x='.concat(d['x']));
                    }
                '''
nb_element = 10

# On multiBarChart the xdata needs to be numeric,
# if you want to use 'string' you should use discreteBarChart
xdata = list(range(nb_element))
ydata = [random.randint(1, 10) for i in range(nb_element)]
ydata2 = [x * 2 for x in ydata]

extra_serie = {"tooltip": {"y_start": "", "y_end": " call"}}
chart.add_serie(name="Count", y=ydata, x=xdata, extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(name="Duration", y=ydata2, x=xdata, extra=extra_serie)
chart.buildhtml()

output_file.write(chart.htmlcontent)
# ---------------------------------------

# close Html file
output_file.close()
