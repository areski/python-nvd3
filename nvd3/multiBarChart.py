#!/usr/bin/python
# -*- coding: utf-8 -*-
from NVD3Chart import NVD3Chart


class multiBarChart(NVD3Chart):
    """
    A multiple bar graph contains comparisons of two or more categories or bars.
    One axis represents a quantity and the other axis identifies a specific feature
    about the categories. Reading a multiple bar graph includes looking at extremes
    (tallest/longest vs. shortest) in each grouping.

    .. image:: ../_static/screenshot/multiBarChart.png

    Python Example::

        from nvd3 import multiBarChart
        chart = multiBarChart(name='multiBarChart', height=400, width=400)
        xdata = [0, 1, 3, 4]
        ydata = [6, 12, 9, 16]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    Javascript example::

        data_MultiBarChart = [{ "key" : "Serie 1",
           "values" : [
                { "x" : 0
                  "y" : 6
                },
                { "x" : 1,
                  "y" : 12
                },
                { "x" : 3,
                  "y" : 9
                },
              ],
            "yAxis" : "1"
        }]

        nv.addGraph(function() {
            var chart = nv.models.multiBarChart();
            chart.xAxis
                .tickFormat(d3.format(',.2f'))
            chart.yAxis
                .tickFormat(d3.format(',.2f'))
            d3.select('#MultiBarChart svg')
                .datum(data_MultiBarChart)
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
