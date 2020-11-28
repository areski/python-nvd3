#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart, TemplateMixin


class cumulativeLineChart(TemplateMixin, NVD3Chart):
    """
    A cumulative line chart is used when you have one important grouping representing
    an ordered set of data and one value to show, summed over time.

    Python example::

        from nvd3 import cumulativeLineChart
        chart = cumulativeLineChart(name='cumulativeLineChart', x_is_date=True)
        xdata = [1365026400000, 1365026500000, 1365026600000]
        ydata = [6, 5, 1]
        y2data = [36, 55, 11]

        extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
        chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie)

        extra_serie = {"tooltip": {"y_start": "", "y_end": " mins"}}
        chart.add_serie(name="Serie 2", y=y2data, x=xdata, extra=extra_serie)
        chart.buildhtml()
        print(chart.content)


    Javascript generated:


    .. include:: ./examples/cumulativeLineChart.html


    """

    CHART_FILENAME = "./cumulativelinechart.html"
    template_chart_nvd3 = NVD3Chart.template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        super(cumulativeLineChart, self).__init__(**kwargs)
        self.model = 'cumulativeLineChart'

        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)

        if kwargs.get('x_is_date', False):
            self.set_date_flag(True)
            self.create_x_axis('xAxis',
                               format=kwargs.get('x_axis_format', '%d %b %Y'),
                               date=True)
            self.set_custom_tooltip_flag(True)
        else:
            self.create_x_axis('xAxis', format=kwargs.get(
                'x_axis_format', '.2f'))

        self.create_y_axis('yAxis', format=kwargs.get('y_axis_format', '.1%'))

        self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
