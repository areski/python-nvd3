#!/usr/bin/python
# -*- coding: utf-8 -*-
from NVD3Chart import NVD3Chart, stab


class lineChart(NVD3Chart):
    """
    A line chart or line graph is a type of chart which displays information
    as a series of data points connected by straight line segments.

    .. image:: ../_static/screenshot/lineChart.png

    Python example::

        from nvd3 import lineChart
        chart = lineChart(name='lineChart', height=400, width=400, date=True)
        xdata = [1365026400000000, 1365026500000000, 1365026600000000]
        ydata = [-6, 5, -1]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    Javascript generated::

        data_lineChart = [{
            "key" : "Serie 1",
            "values" : [
                { "x" : "1365026400000000",
                  "y" : -6
                },
                { "x" : "1365026500000000",
                  "y" : -5
                },
                { "x" : "1365026600000000",
                  "y" : -1
                },
              ],
            "yAxis" : "1"
        }]

        nv.addGraph(function() {
                var chart = nv.models.lineChart();
                chart.xAxis
                    .tickFormat(function(d) { return d3.time.format('%d %b %y')(new Date(d)) })
                chart.yAxis
                    .tickFormat(d3.format(',.2f'))
                d3.select('#lineChart svg')
                    .datum(data_lineChart)
                    .transition()
                    .duration(500)
                    .call(chart);
            return chart;
        });
    """
    def __init__(self, height=450, width=None, date=False, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        if date:
            self.set_date_flag(True)
            self.create_x_axis('xAxis', format='%d %b %Y', date=True)
            self.set_custom_tooltip_flag(True)
        else:
            self.create_x_axis('xAxis', format="r")
        self.create_y_axis('yAxis', format=".02f")

        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)

    def build_custom_tooltip(self, x_start='', x_end='', y_start='', y_end='', **axis_data):
        """generate custom tooltip for the chart"""

        axis_key_list = [d for d in axis_data.keys() if 'key' in d]
        tooltip_condition = ''
        for key in axis_key_list:
            axis_no = key.split('key')[1]
            series_name = axis_data['key' + axis_no]
            _start = axis_data['y' + axis_no + '_start']
            _end = axis_data['y' + axis_no + '_end']
            _start = ("'" + str(_start) + "' + ") if _start else ''
            _end = (" + '" + str(_end) + "'") if _end else ''
            tooltip_condition += stab(3) + "if(key == '" + series_name + "'){\n" +\
                stab(4) + "var y = " + _start + " String(graph.point.y) " + _end + ";\n" +\
                stab(3) + "}\n"


        if self.custom_tooltip_flag:
            x_start = ("'" + str(x_start) + "' + ") if x_start else ''
            x_end = (" + '" + str(x_end) + "'") if x_end else ''
            y_start = ("'" + str(y_start) + "' + ") if y_start else ''
            y_end = (" + '" + str(y_end) + "'") if y_end else ''

            if not self.date_flag:
                self.charttooltip = stab(2) + "chart.tooltipContent(function(key, y, e, graph) {\n" + \
                    stab(3) + "var y = " + y_start + " String(graph.point.y) " + y_end + ";\n" +\
                    stab(3) + "var x = " + x_start + " String(graph.point.x) " + x_end + ";\n" +\
                    stab(3) + "tooltip_str = '<center><b>'+key+'</b></center>' + x + ' <-> ' + y  ;\n" +\
                    stab(3) + "return tooltip_str;\n" + \
                    stab(2) + "});\n"
            else:

                self.charttooltip = stab(2) + "chart.tooltipContent(function(key, y, e, graph) {\n" + \
                    stab(3) + "var x = d3.time.format('%s')(new Date(parseInt(graph.point.x)));\n" % self.dateformat +\
                    stab(3) + "var y = " + y_start + " String(graph.point.y) " + y_end + ";\n" +\
                    tooltip_condition +\
                    stab(3) + "tooltip_str = '<center><b>'+key+'</b></center>' + y + ' on ' + x ; \n" +\
                    stab(3) + "return tooltip_str;\n" + \
                    stab(2) + "});\n"