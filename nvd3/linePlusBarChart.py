#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart, TemplateMixin


class linePlusBarChart(TemplateMixin, NVD3Chart):

    """
    A linePlusBarChart Chart is a type of chart which displays information
    as a series of data points connected by straight line segments
    and with some series with rectangular bars with lengths proportional
    to the values that they represent.

    Python example::

        from nvd3 import linePlusBarChart
        chart = linePlusBarChart(name="linePlusBarChart",
                             width=500, height=400, x_axis_format="%d %b %Y",
                             x_is_date=True, focus_enable=True,
                             yaxis2_format="function(d) { return d3.format(',0.3f')(d) }")

        xdata = [1338501600000, 1345501600000, 1353501600000]
        ydata = [6, 5, 1]
        y2data = [0.002, 0.003, 0.004]

        extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"},
                       "date_format": "%d %b %Y %H:%S" }
        chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie,
                        bar=True)

        extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " min"}}
        chart.add_serie(name="Serie 2", y=y2data, x=xdata, extra=extra_serie)
        chart.buildhtml()
        print(chart.content)

    Note that in case you have two data serie with extreme different numbers,
    that you would like to format in different ways,
    you can pass a keyword *yaxis1_format* or *yaxis2_format* when
    creating the graph.

    In the example above the graph created presents the values of the second
    data series with three digits right  of the decimal point.

    Javascript generated:

    .. include:: ./examples/linePlusBarChart.html

    """
    CHART_FILENAME = "./lineplusbarchart.html"
    template_chart_nvd3 = NVD3Chart.template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        super(linePlusBarChart, self).__init__(**kwargs)
        self.model = 'linePlusBarChart'

        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)
        self.yaxis1_format = kwargs.get('yaxis1_format',
                                        "function(d) { return d3.format(',f')(d) }")
        self.yaxis2_format = kwargs.get('yaxis2_format',
                                        "function(d) { return d3.format(',f')(d) }")

        if kwargs.get('x_is_date', False):
            self.set_date_flag(True)
            self.create_x_axis('xAxis',
                               format=kwargs.get('x_axis_format',
                                                 '%d %b %Y %H %S'),
                               date=True)
            self.create_x_axis('x2Axis', format=kwargs.get('x_axis_format',
                                                           '%d %b %Y %H %S'),
                               date=True)
            self.set_custom_tooltip_flag(True)
        else:
            self.create_x_axis('xAxis', format=kwargs.get('x_axis_format',
                                                          '.2f'))
            self.create_x_axis('x2Axis', format=kwargs.get('x_axis_format',
                                                           '.2f'))

        self.create_y_axis('y1Axis', format=self.yaxis1_format,
                           custom_format=True)
        self.create_y_axis('y2Axis', format=self.yaxis2_format,
                           custom_format=True)

        self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
