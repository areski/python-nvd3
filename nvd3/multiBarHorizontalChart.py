#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart, TemplateMixin


class multiBarHorizontalChart(TemplateMixin, NVD3Chart):
    """
    A multiple horizontal bar graph contains comparisons of two or more categories or bars.

    Python example::

        from nvd3 import multiBarHorizontalChart
        chart = multiBarHorizontalChart(name='multiBarHorizontalChart', height=400, width=400)
        xdata = [-14, -7, 7, 14]
        ydata = [-6, 5, -1, 9]
        y2data = [-23, -6, -32, 9]

        extra_serie = {"tooltip": {"y_start": "", "y_end": " balls"}}
        chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie)

        extra_serie = {"tooltip": {"y_start": "", "y_end": " calls"}}
        chart.add_serie(name="Serie 2", y=y2data, x=xdata, extra=extra_serie)
        chart.buildhtml()
        print(chart.content)

    Javascript generated:

    .. include:: ./examples/multiBarHorizontalChart.html

    """

    CHART_FILENAME = "./multibarcharthorizontal.html"
    template_chart_nvd3 = NVD3Chart.template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        super(multiBarHorizontalChart, self).__init__(**kwargs)
        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)

        self.create_x_axis('xAxis', format=kwargs.get('x_axis_format', '.2f'))
        self.create_y_axis('yAxis', format=kwargs.get('y_axis_format', '.2f'))

        self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
