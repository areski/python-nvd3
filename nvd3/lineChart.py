#!/usr/bin/python
# -*- coding: utf-8 -*-
from NVD3Chart import NVD3Chart


class lineChart(NVD3Chart):
    """
    A line chart or line graph is a type of chart which displays information
    as a series of data points connected by straight line segments.

    .. image:: ../_static/screenshot/lineChart.png

    Python Example::

        from nvd3 import lineChart
        chart = lineChart(name='lineChart', height=400, width=400, date=True)
        xdata = [1365026400000000, 1365026500000000, 1365026600000000]
        ydata = [-6, 5, -1]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    Javascript example::

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
