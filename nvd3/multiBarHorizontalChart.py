#!/usr/bin/python
# -*- coding: utf-8 -*-
from NVD3Chart import NVD3Chart


class multiBarHorizontalChart(NVD3Chart):
    """
    A multiple horizontal bar graph contains comparisons of two or more categories or bars.

    .. image:: ../_static/screenshot/multiBarHorizontalChart.png

    Python Example::

        from nvd3 import multiBarHorizontalChart
        chart = multiBarHorizontalChart(name='multiBarHorizontalChart', height=400, width=400)
        xdata = [-14, -7, 7, 14]
        ydata = [-6, 5, -1, 9]
        y2data = [-23, -6, -32, 9]
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=y2data, x=xdata)
        chart.buildhtml()

    Javascript example::

        data_lineChart = [ { "key" : "Serie 1",
            "values" : [ { "x" : 0,
                  "y" : -2
                },
                { "x" : 1,
                  "y" : 4
                },
                { "x" : 2,
                  "y" : -7
                },
              ],
            "yAxis" : "1"
          },
          { "key" : "Serie 2",
            "values" : [ { "x" : 0,
                  "y" : -4
                },
                { "x" : 1,
                  "y" : 8
                },
                { "x" : 2,
                  "y" : -14
                },
              ],
            "yAxis" : "1"
          }
        ]

        nv.addGraph(function() {
                var chart = nv.models.multiBarHorizontalChart();
                chart.xAxis
                    .tickFormat(d3.format(',.2f'))
                chart.yAxis
                    .tickFormat(d3.format(',.2f'))
                d3.select('#multiBarHorizontalChart svg')
                    .datum(data_multiBarHorizontalChart)
                    .transition().duration(500)
                    .attr('height', 350)
                    .call(chart);

            return chart;
        });
    """
    def __init__(self, height=450, width=None, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        self.create_x_axis('xAxis', format=".2f")
        self.create_y_axis('yAxis', format=".2f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
