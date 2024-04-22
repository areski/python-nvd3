#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart, TemplateMixin


class stackedAreaChart(TemplateMixin, NVD3Chart):
    """
    The stacked area chart is identical to the area chart, except the areas are stacked
    on top of each other, rather than overlapping. This can make the chart much easier to read.

    Python example::

        from nvd3 import stackedAreaChart
        chart = stackedAreaChart(name='stackedAreaChart', height=400, width=400)

        xdata = [100, 101, 102, 103, 104, 105, 106,]
        ydata = [6, 11, 12, 7, 11, 10, 11]
        ydata2 = [8, 20, 16, 12, 20, 28, 28]

        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " min"}}
        chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie)
        chart.add_serie(name="Serie 2", y=ydata2, x=xdata, extra=extra_serie)
        chart.buildhtml()
        print(chart.content)

    Javascript generated:

    .. include:: ./examples/stackedAreaChart.html

    """

    CHART_FILENAME = "./stackedareachart.html"
    template_chart_nvd3 = NVD3Chart.template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        super(stackedAreaChart, self).__init__(**kwargs)
        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)
        self.model = 'stackedAreaChart'

        if kwargs.get('x_is_date', False):
            self.set_date_flag(True)
            self.create_x_axis('xAxis',
                               format=kwargs.get('x_axis_format', '%d %b %Y'),
                               date=True)
            self.set_custom_tooltip_flag(True)
        else:
            self.create_x_axis('xAxis', format=kwargs.get('x_axis_format',
                                                          '.2f'))
        self.create_y_axis('yAxis', format=kwargs.get('y_axis_format', '.2f'))

        self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
