#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart, TemplateMixin


class bulletChart(TemplateMixin, NVD3Chart):
    '''
    A bullet chart is a variation of a bar graph
    used to indicate the value of a single variable
    in relation to a set of qualitative ranges. It is
    inspired by a dashboard gauge or thermometer chart.

    Python example:

        from nvd3.bulletChart import bulletChart
        chart = bulletChart.bulletChart(name=type, height=100, width=500)
        title = 'Revenue',
        subtitle = 'US$, in thousands'
        ranges = [150, 225, 300]
        measures = [220, 270]
        markers = [250]
        chart.add_serie(
            title=title,
            subtitle=subtitle,
            ranges=ranges,
            measures=measures,
            markers=markers)
        chart.buildhtml()
        print(chart.content)

    JavaScript generated:

    .. include:: ./examples/bulletChart.html

    '''
    CHART_FILENAME = './bulletchart.html'
    template_chart_nvd3 = NVD3Chart.template_environment.get_template(
        CHART_FILENAME)

    def __init__(self, **kwargs):
        super(bulletChart, self).__init__(**kwargs)
        self.model = 'bulletChart'

        height = kwargs.get('height', None)
        width = kwargs.get('width', 200)

        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)

    def add_serie(self, ranges, measures, title, subtitle, markers=None,
            name=None, **kwargs):
        if not name:
            name = "Serie %d" % (self.serie_no)
        if markers:
            serie = [{
                'title': title,
                'subtitle': subtitle,
                'ranges': ranges,
                'measures': measures,
                'markers': markers
                }]
        else:
            serie = [{
                'title': title,
                'subtitle': subtitle,
                'ranges': ranges,
                'measures': measures,
                }]
        data_keyvalue = {'values': serie, 'key': name}

        self.serie_no += 1
        self.series.append(data_keyvalue)
