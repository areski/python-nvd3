#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from NVD3Chart import NVD3Chart


#TODO: Add extensive documentation on lineChart
#settings supported
#examples
class lineChart(NVD3Chart):
    """
    usage ::

        chart = nvd3.lineChart(name='lineChart', height=400, width=400, date=True)
        xdata = [1365026400000000, 1365026500000000, 1365026600000000]
        ydata = [-6, 5, -1]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    js-code ::

        data_lineChart = [{
            "key" : "Serie 1",
            "values" : [
                { "x" : "1365026400000000",
                  "y" : -6
                },
                { "x" : "1365026500000000",
                  "y" : -5
                },
                { "x" : "1365026600000000",
                  "y" : -1
                },
              ],
            "yAxis" : "1"
        }]

        nv.addGraph(function() {
                var chart = nv.models.lineChart();
                chart.xAxis
                    .tickFormat(function(d) { return d3.time.format('%d %b %y')(new Date(d)) })
                chart.yAxis
                    .tickFormat(d3.format(',.2f'))
                d3.select('#lineChart svg')
                    .datum(data_lineChart)
                    .transition()
                    .duration(500)
                    .call(chart);
            return chart;
        });
    """
    def __init__(self, height=450, width=None, date=False, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        if date:
            self.create_x_axis('xAxis', format='%d %b %Y', date=True)
            self.set_custom_tooltip_flag(True)
        else:
            self.create_x_axis('xAxis', format="r")
        self.create_y_axis('yAxis', format=".02f")

        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
