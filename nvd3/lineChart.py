#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart, TemplateMixin


class lineChart(TemplateMixin, NVD3Chart):

    """
    A line chart or line graph is a type of chart which displays information
    as a series of data points connected by straight line segments.

    Python example::

        from nvd3 import lineChart
        chart = lineChart(name="lineChart", x_is_date=False, x_axis_format="AM_PM")

        xdata = range(24)
        ydata = [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 4, 3, 3, 5, 7, 5, 3, 16, 6, 9, 15, 4, 12]
        ydata2 = [9, 8, 11, 8, 3, 7, 10, 8, 6, 6, 9, 6, 5, 4, 3, 10, 0, 6, 3, 1, 0, 0, 0, 1]

        extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
        chart.add_serie(y=ydata, x=xdata, name='sine', extra=extra_serie)
        extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
        chart.add_serie(y=ydata2, x=xdata, name='cose', extra=extra_serie)
        chart.buildhtml()
        print(chart.content)

    Javascript generated:

    .. include:: ./examples/lineChart.html

    See the source code of this page, to see the underlying javascript.
    """
    CHART_FILENAME = "./linechart.html"
    template_chart_nvd3 = NVD3Chart.template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        super(lineChart, self).__init__(**kwargs)
        self.model = 'lineChart'

        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)

        if kwargs.get('x_is_date', False):
            self.set_date_flag(True)
            self.create_x_axis('xAxis',
                               format=kwargs.get('x_axis_format', '%d %b %Y'),
                               date=True)
            self.set_custom_tooltip_flag(True)
        else:
            if kwargs.get('x_axis_format') == 'AM_PM':
                self.x_axis_format = format = 'AM_PM'
            else:
                format = kwargs.get('x_axis_format', 'r')
            self.create_x_axis('xAxis', format=format,
                               custom_format=kwargs.get('x_custom_format',
                                                        False))
        self.create_y_axis(
            'yAxis',
            format=kwargs.get('y_axis_format', '.02f'),
            custom_format=kwargs.get('y_custom_format', False))

        # must have a specified height, otherwise it superimposes both chars
        self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
