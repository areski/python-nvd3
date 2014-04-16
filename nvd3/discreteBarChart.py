#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart


class discreteBarChart(NVD3Chart):
    """
    A discrete bar chart or bar graph is a chart with rectangular bars with
    lengths proportional to the values that they represent.

    .. image:: ../_static/doc_images/discreteBarChart.png

    Python example::

        from nvd3 import discreteBarChart
        chart = discreteBarChart(name='discreteBarChart', height=400, width=400)

        xdata = ["A", "B", "C", "D", "E", "F"]
        ydata = [3, 4, 0, -3, 5, 7]

        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    Javascript generated::

        nv.addGraph(function() {
            var chart = nv.models.discreteBarChart();
            chart.tooltipContent(function(key, y, e, graph) {
                var x = String(graph.point.x);
                var y = String(graph.point.y);
                var y = String(graph.point.y);
                tooltip_str = '<center><b>'+key+'</b></center>' + y + ' at ' + x;
                return tooltip_str;
            });
            d3.select('#discreteBarChart svg')
                .datum(data_discreteBarChart)
                .transition().duration(500)
                .attr('width', 400)
                .attr('height', 400)
                .call(chart);

        return chart;
        });data_discreteBarChart=[
            {"key": "Serie 1",
            "yAxis": "1",
            "values": [{"x": "A", "y": 3},
                       {"x": "B", "y": 4},
                       {"x": "C", "y": 0},
                       {"x": "D", "y": 3},
                       {"x": "E", "y": 5},
                       {"x": "F", "y": 7}
        ]}];
    """
    def __init__(self, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        # self.slugify_name(kwargs.get('name', 'discreteBarChart'))
        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)

        if kwargs.get('x_is_date', False):
            self.set_date_flag(True)
            self.create_x_axis('xAxis',
                               format=kwargs.get('x_axis_format', "%d %b %Y %H %S"),
                               date=True)
        else:
            self.create_x_axis('xAxis', format=None)

        self.set_custom_tooltip_flag(True)

        # must have a specified height, otherwise it superimposes both charts
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
