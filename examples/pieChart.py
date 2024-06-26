#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Examples for Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from nvd3 import pieChart


# Open File for test
output_file = open('test_pieChart.html', 'w')

chart_name = "pieChart"
chart = pieChart(name=chart_name, color_category='category20c', height=400, width=400, extras="d3.selectAll('#piechart .nv-slice').style('opacity', 0.5);")
chart.set_containerheader("\n\n<h2>" + chart_name + "</h2>\n\n")
chart.callback = '''
                    function(){
                    d3.selectAll(".nv-pie .nv-pie .nv-slice").on('click',
                        function(d){
                        console.log("piechart_callback_test: clicked on slice " + JSON.stringify(d['data']));
                        console.log('/app/fruit?type='.concat(d['data']['label']));
                    }
                '''

extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
ydata = [3, 4, 0, 1, 5, 7, 3]

chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
chart.buildhtml()
output_file.write(chart.htmlcontent)
# ---------------------------------------

# close Html file
output_file.close()
