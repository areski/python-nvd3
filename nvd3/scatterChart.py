#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from NVD3Chart import NVD3Chart, stab


class scatterChart(NVD3Chart):
    """
    usage ::

        from nvd3 import scatterChart
        chart = scatterChart(name='scatterChart', height=400, width=400)
        xdata = [3, 4, 0, -3, 5, 7]
        ydata = [-1, 2, 3, 3, 15, 2]
        ydata = [1, -2, 4, 7, -5, 3]

        kwargs1 = {'shape': 'circle'}
        kwargs2 = {'shape': 'cross'}
        chart.add_serie(y=ydata, x=xdata, **kwargs1)
        chart.add_serie(y=ydata, x=xdata, **kwargs2)
        chart.buildhtml()

    js example::

        data = [{ key: "series 1",
                  values: [
                    {
                      "x": 2,
                      "y": 10,
                      "shape": "circle"
                    },
                    {
                      "x": -2,
                      "y" : 0,
                      "shape": "circle"
                    },
                    {
                      "x": 5,
                      "y" : -3,
                      "shape": "circle"
                    },
                  ]
                },
                { key: "series 2",
                  values: [
                    {
                      "x": 4,
                      "y": 10,
                      "shape": "cross"
                    },
                    {
                      "x": 4,
                      "y" : 0,
                      "shape": "cross"
                    },
                    {
                      "x": 3,
                      "y" : -3,
                      "shape": "cross"
                    },
                  ]
                }]

        nv.addGraph(function() {
            var chart = nv.models.scatterChart()
                .showLabels(true);

            chart.showDistX(true);
            chart.showDistY(true);

            d3.select("#div_id")
                .datum(data)
                .transition()
                .duration(1200)
                .call(chart);

            return chart;
        });
    """
    def __init__(self, height=450, width=None, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        self.create_x_axis('xAxis', format=".02f")
        self.create_y_axis('yAxis', format=".02f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)

    def buildjschart(self):
        NVD3Chart.buildjschart(self)

        scatter_jschart = '\n' + stab(3) + '.showDistX(true)\n' + \
            stab(3) + '.showDistY(true)\n' + \
            stab(3) + '.color(d3.scale.category10().range())'

        start_index = self.jschart.find('.scatterChart()')
        string_len = len('.scatterChart()')
        replace_index = start_index + string_len
        if start_index > 0:
            self.jschart = self.jschart[:replace_index] + scatter_jschart + self.jschart[replace_index:]