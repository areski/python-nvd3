#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart, TemplateMixin


class candlestickBarChart(TemplateMixin, NVD3Chart):
    """
    A candlestick bar chart is a chart used in finance to demonstrate
    the movements of an asset or currency. It shows the opening,
    closing, high, and low values for each data point.

    Python example::


    values = [
        {"date": 15854, "open": 165.42, "high": 165.8, "low": 164.34, "close": 165.22, "volume": 160363400, "adjusted": 164.35},
        {"date": 15855, "open": 165.35, "high": 166.59, "low": 165.22, "close": 165.83, "volume": 107793800, "adjusted": 164.96},
        {"date": 15856, "open": 165.37, "high": 166.31, "low": 163.13, "close": 163.45, "volume": 176850100, "adjusted": 162.59},
        {"date": 15859, "open": 163.83, "high": 164.46, "low": 162.66, "close": 164.35, "volume": 168390700, "adjusted": 163.48},
        {"date": 15860, "open": 164.44, "high": 165.1, "low": 162.73, "close": 163.56, "volume": 157631500, "adjusted": 162.7},
        {"date": 15861, "open": 163.09, "high": 163.42, "low": 161.13, "close": 161.27, "volume": 211737800, "adjusted": 160.42},
        ]

        from nvd3 import candlestickBarChart
        type = 'candlestickBarChart'
        chart = candlestickBarChart(name=type, height=600, width=1400)
        chart.add_serie(values=values)
        chart.buildhtml()

    Javascript generated:

    .. raw:: html

    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <link href="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.2/nv.d3.min.css" rel="stylesheet" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.2/nv.d3.min.js"></script>
        </head>
        <body>

        <div id="candlestickbarchart"><svg style="width:1400px;height:600px;"></svg></div>


        <script>

            data_candlestickbarchart=[{"values": [{"adjusted": 164.35, "close": 165.22, "open": 165.42, "high": 165.8, "date": "2015-01-01", "low": 164.34, "volume": 160363400}, {"adjusted": 164.96, "close": 165.83, "open": 165.35, "high": 166.59, "date": "2015-01-02", "low": 165.22, "volume": 107793800}, {"adjusted": 162.59, "close": 163.45, "open": 165.37, "high": 166.31, "date": "2015-01-03", "low": 163.13, "volume": 176850100}, {"adjusted": 163.48, "close": 164.35, "open": 163.83, "high": 164.46, "date": "2015-01-04", "low": 162.66, "volume": 168390700}, {"adjusted": 162.7, "close": 163.56, "open": 164.44, "high": 165.1, "date": "2015-01-05", "low": 162.73, "volume": 157631500}, {"adjusted": 160.42, "close": 161.27, "open": 163.09, "high": 163.42, "date": "2015-01-06", "low": 161.13, "volume": 211737800}], "key": "Serie 1"}];

            nv.addGraph(function() {
            var chart = nv.models.candlestickBarChart()
                .x(function(d) { return d['date'] })
                .y(function(d) { return d['close'] })
                .duration(250)
                .margin({left: 75, bottom: 50});

            chart.xAxis
                    .axisLabel("Dates")
                    .tickFormat(function(d) {
                        return d3.time.format('%Y-%m-%d')(new Date(d));
                    });
            chart.yAxis
                    .axisLabel('Stock Price')
                    .tickFormat(function(d,i){ return '$' + d3.format(',.1f')(d); });
            d3.select("#candlestickbarchart svg")
                    .datum(data_candlestickbarchart)
                    .transition().duration(500)
                    .call(chart);
            nv.utils.windowResize(chart.update);
            return chart;
        });

        </script>

        </body>
    </html>

    """

    CHART_FILENAME = "./candlestickbar.html"
    template_chart_nvd3 = NVD3Chart.template_environment.get_template(
        CHART_FILENAME)

    def __init__(self, **kwargs):
        super(candlestickBarChart, self).__init__(**kwargs)
        self.model = 'candlestickBarChart'

        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)

        self.set_graph_height(height)
        if width:
            self.set_graph_width(width)

    def add_serie(self, values, name=None, **kwargs):
        if not name:
            name = "Serie %d" % (self.serie_no)
        data_keyvalue = {'values': values, 'key': name}

        self.serie_no += 1
        self.series.append(data_keyvalue)
