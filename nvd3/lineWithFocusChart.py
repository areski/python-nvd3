#!/usr/bin/python
# -*- coding: utf-8 -*-
from NVD3Chart import NVD3Chart


class lineWithFocusChart(NVD3Chart):
    """
    .. image:: ../_static/screenshot/lineWithFocusChart.png

    Python Example::

        from nvd3 import lineWithFocusChart
        chart = lineWithFocusChart(name='lineWithFocusChart', date=True)
        xdata = [1365026400000000, 1365026500000000, 1365026600000000]
        ydata = [-6, 5, -1]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    Javascript example::

        data_lineWithFocusChart = [{ "key" : "Serie 1",
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
                var chart = nv.models.lineWithFocusChart();
                chart.yAxis
                    .tickFormat(d3.format(',.2f'))
                chart.y2Axis
                    .tickFormat(d3.format(',.2f'))
                chart.xAxis
                    .tickFormat(function(d) { return d3.time.format('%d %b %y')(new Date(d)) })
                chart.x2Axis
                    .tickFormat(function(d) { return d3.time.format('%d %b %y')(new Date(d)) })
                d3.select('#lineWithFocusChart svg')
                    .datum(data_lineWithFocusChart)
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
            self.create_x_axis('x2Axis', format='%d %b %Y', date=True)
            self.set_custom_tooltip_flag(True)
        else:
            self.create_x_axis('xAxis', format=".2f")
            self.create_x_axis('x2Axis', format=".2f")

        self.create_y_axis('yAxis', format=".2f")
        self.create_y_axis('y2Axis', format=".2f")

        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
