#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart, TemplateMixin


class scatterChart(TemplateMixin, NVD3Chart):

    """
    A scatter plot or scattergraph is a type of mathematical diagram using Cartesian
    coordinates to display values for two variables for a set of data.
    The data is displayed as a collection of points, each having the value of one variable
    determining the position on the horizontal axis and the value of the other variable
    determining the position on the vertical axis.

    Python example::

        from nvd3 import scatterChart
        chart = scatterChart(name='scatterChart', height=400, width=400)
        xdata = [3, 4, 0, -3, 5, 7]
        ydata = [-1, 2, 3, 3, 15, 2]
        ydata2 = [1, -2, 4, 7, -5, 3]

        kwargs1 = {'shape': 'circle', 'size': '1'}
        kwargs2 = {'shape': 'cross', 'size': '10'}

        extra_serie = {"tooltip": {"y_start": "", "y_end": " call"}}
        chart.add_serie(name="series 1", y=ydata, x=xdata, extra=extra_serie, **kwargs1)

        extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
        chart.add_serie(name="series 2", y=ydata2, x=xdata, extra=extra_serie, **kwargs2)
        chart.buildhtml()
        print(chart.content)

    Javascript generated:

    .. include:: ./examples/scatterChart.html

    """

    CHART_FILENAME = "./scatterchart.html"
    template_chart_nvd3 = NVD3Chart.template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        super(scatterChart, self).__init__(**kwargs)
        self.model = 'scatterChart'
        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)
        self.create_x_axis('xAxis', format=kwargs.get('x_axis_format', '.02f'),
                           label=kwargs.get('x_axis_label', None))
        self.create_y_axis('yAxis', format=kwargs.get('y_axis_format', '.02f'),
                           label=kwargs.get('y_axis_label', None))
        self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
