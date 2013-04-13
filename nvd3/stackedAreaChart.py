#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from NVD3Chart import NVD3Chart


#TODO: Add extensive documentation on StackedAreaChart
#settings supported
#examples
class stackedAreaChart(NVD3Chart):
    """
    usage ::

        chart = nvd3.stackedAreaChart(name='stackedAreaChart', height=400, width=400)
        xdata = [100, 101, 102, 103, 104, 105, 106,]
        ydata = [6, 11, 12, 7, 11, 10, 11]
        ydata2 = [8, 20, 16, 12, 20, 28, 28]
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    js example::

        data_stackedAreaChart = [{
                  "values":[
                     {
                        "y":9,
                        "x":100
                     },
                     {
                        "y":5,
                        "x":101
                     },
                  ],
                  "key":"Serie 1",
                  "yAxis":"1"
               },
               {
                  "values":[
                     {
                        "y":18,
                        "x":100
                     },
                     {
                        "y":10,
                        "x":101
                     },
                  ],
                  "key":"Serie 2",
                  "yAxis":"1"
               }
            ]

        nv.addGraph(function() {
            var chart = nv.models.stackedAreaChart();
            chart.xAxis
                .tickFormat(d3.format(',.2f'))
            chart.yAxis
                .tickFormat(d3.format(',.2f'))
            d3.select('#stackedAreaChart svg')
                .datum(data_stackedAreaChart)
                .transition()
                .duration(500)
                .call(chart);
            return chart;
        });
    """
    def __init__(self, height=450, width=None, date=False, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        if date:
            self.create_x_axis('xAxis', format='%d %b %y', date=True)
        else:
            self.create_x_axis('xAxis', format=".2f")
        self.create_y_axis('yAxis', format=".2f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
