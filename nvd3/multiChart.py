#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart, TemplateMixin


class multiChart(TemplateMixin, NVD3Chart):

    """
    A multiChart is a type of chart which combines several plots of the same or different types.

    Python example::

        from nvd3 import multiChart
        type = "multiChart"
        chart = multiChart(name=type, x_is_date=False, x_axis_format="AM_PM")

        xdata = [1,2,3,4,5,6]
        ydata = [115.5,160.5,108,145.5,84,70.5]
        ydata2 = [48624,42944,43439,24194,38440,31651]

        kwargs1 = {'color': 'black'}
        kwargs2 = {'color': 'red'}
        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}
        chart.add_serie(y=ydata, x=xdata, type='line', yaxis=1, name='visits', extra=extra_serie, **kwargs1)
        extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
        chart.add_serie(y=ydata2, x=xdata, type='bar', yaxis=2,name='spend', extra=extra_serie, **kwargs2)
        chart.buildhtml()
        print(chart.content)


    Javascript rendered to:

    .. include:: ./examples/multiChart.html

    See the source code of this page, to see the underlying javascript.
    """
    CHART_FILENAME = "./multichart.html"
    template_chart_nvd3 = NVD3Chart.template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        super(multiChart, self).__init__(**kwargs)
        self.model = 'multiChart'

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
            'yAxis1',
            format=kwargs.get('y1_axis_format', '.02f'),
            custom_format=kwargs.get('y1_custom_format', False))

        self.create_y_axis(
            'yAxis2',
            format=kwargs.get('y2_axis_format', '.02f'),
            custom_format=kwargs.get('y2_custom_format', False))

        # must have a specified height, otherwise it superimposes both chars
        self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
