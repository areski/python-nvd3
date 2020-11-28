#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart, TemplateMixin


class pieChart(TemplateMixin, NVD3Chart):

    """
    A pie chart (or a circle graph) is a circular chart divided into sectors,
    illustrating numerical proportion. In chart, the arc length of each sector
    is proportional to the quantity it represents.

    Python example::

        from nvd3 import pieChart
        chart = pieChart(name='pieChart', color_category='category20c',
                         height=400, width=400)

        xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawbery",
                 "Pineapple"]
        ydata = [3, 4, 0, 1, 5, 7, 3]

        extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
        chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
        chart.buildhtml()
        print(chart.content)

    Javascript generated:

    .. include:: ./examples/pieChart.html

    """
    CHART_FILENAME = "./piechart.html"
    template_chart_nvd3 = NVD3Chart.template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        super(pieChart, self).__init__(**kwargs)

        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)
        self.donut = kwargs.get('donut', False)
        self.donutRatio = kwargs.get('donutRatio', 0.35)
        self.color_list = []
        self.create_x_axis('xAxis', format=None)
        self.create_y_axis('yAxis', format=None)
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
        self.donut = kwargs.get('donut', False)
        self.donutRatio = kwargs.get('donutRatio', 0.35)
        self.callback = kwargs.get('callback', None)
