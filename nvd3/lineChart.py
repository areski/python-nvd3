#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart


class lineChart(NVD3Chart):
    """
    A line chart or line graph is a type of chart which displays information
    as a series of data points connected by straight line segments.

    .. image:: ../_static/screenshot/lineChart.png

    Python example::

        from nvd3 import lineChart
        chart = lineChart(name='lineChart', height=400, width=400, date=True, x_axis_date_format="%d %b %Y %H")
        xdata = [1365026400000000, 1365026500000000, 1365026600000000]
        ydata = [-6, 5, -1]

        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"},
                       "date_format": "%d %b %Y %H:%S"}
        chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie)
        chart.buildhtml()

    Javascript generated::

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
                    .tickFormat(function(d) { return d3.time.format('%d %b %y %H')(new Date(d)) });
                chart.yAxis
                    .tickFormat(d3.format(',.2f'));
                chart.tooltipContent(function(key, y, e, graph) {
                    var x = d3.time.format('%d %b %Y %H:%S')(new Date(parseInt(graph.point.x)));
                    var y = String(graph.point.y);
                    if(key == 'Serie 1'){
                        var y = 'There is ' +  String(graph.point.y)  + ' calls';
                    }
                    tooltip_str = '<center><b>'+key+'</b></center>' + y + ' on ' + x;
                    return tooltip_str;
                });
                d3.select('#lineChart svg')
                    .datum(data_lineChart)
                    .transition()
                    .duration(500)
                    .call(chart);
            return chart;
        });
    """
    def __init__(self, height=450, width=None, date=False, x_axis_date_format="%d %b %Y", **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        if date:
            self.set_date_flag(True)
            self.create_x_axis('xAxis', format=x_axis_date_format, date=True)
            self.set_custom_tooltip_flag(True)
        else:
            self.create_x_axis('xAxis', format="r")
        self.create_y_axis('yAxis', format=".02f")

        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
