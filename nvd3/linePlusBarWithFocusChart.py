#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart, TemplateMixin


class linePlusBarWithFocusChart(TemplateMixin, NVD3Chart):
    """
    A linePlusBarWithFocusChart Chart is a type of chart which displays information
    as a series of data points connected by straight line segments
    and with some series with rectangular bars with lengths proportional
    to the values that they represent

    Python example::

        from nvd3 import linePlusBarWithFocusChart
        chart = linePlusBarWithFocusChart(name='linePlusBarChart', x_is_date=True, x_axis_format="%d %b %Y")

        xdata = [1338501600000, 1345501600000, 1353501600000]
        ydata = [6, 5, 1]
        y2data = [36, 55, 11]
        kwargs = {}
        kwargs['bar'] = True
        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}
        chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie, **kwargs)

        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " min"}}
        chart.add_serie(name="Serie 2", y=y2data, x=xdata, extra=extra_serie)
        chart.buildhtml()

    Javascript generated:

    .. raw:: html

            <div id="linePlusBarChart"><svg style="height:450px;"></svg></div>
            <script>
                data_linePlusBarChart=[{"bar": "true", "values": [{"y": 6, "x": 1338501600000}, {"y": 5, "x": 1345501600000}, {"y": 1, "x": 1353501600000}], "key": "Serie 1"}, {"values": [{"y": 36, "x": 1338501600000}, {"y": 55, "x": 1345501600000}, {"y": 11, "x": 1353501600000}], "key": "Serie 2"}];

                nv.addGraph(function() {
                    var chart = nv.models.linePlusBarWithFocusChart();
                    chart.margin({top: 30, right: 60, bottom: 20, left: 60});
                    var datum = data_linePlusBarChart;
                            chart.y2Axis
                                .tickFormat(function(d) { return d3.format(',.2f')(d) });
                            chart.x2Axis
                                .tickFormat(function(d) {
                            var dx = data_linePlusBarChart[0].values[d] && data_linePlusBarChart[0].values[d].x || 0;
                            return d3.time.format('%d %b %Y')(new Date(dx)); });
                            chart.y4Axis
                                .tickFormat(function(d) { return d3.format(',.2f')(d) });
                            chart.y3Axis
                                .tickFormat(d3.format(',f'));
                            chart.xAxis
                                .tickFormat(function(d) {
                            var dx = data_linePlusBarChart[0].values[d] && data_linePlusBarChart[0].values[d].x || 0;
                            if (dx > 0) { return d3.time.format('%d %b %Y')(new Date(dx)) }
                            return null; });
                            chart.y1Axis
                                .tickFormat(d3.format(',f'));

                        chart.tooltipContent(function(key, y, e, graph) {
                            var x = d3.time.format("%d %b %Y %H:%S")(new Date(parseInt(graph.point.x)));
                            var y = String(graph.point.y);
                            if(key.indexOf('Serie 1') > -1 ){
                                    var y = 'There is ' +  String(graph.point.y)  + ' calls';
                                }
                                if(key.indexOf('Serie 2') > -1 ){
                                    var y = 'There is ' +  String(graph.point.y)  + ' min';
                                }

                            tooltip_str = '<center><b>'+key+'</b></center>' + y + ' on ' + x;
                            return tooltip_str;
                        });


                        chart.showLegend(true);

                    chart.x(function(d,i) { return i });

                    d3.select('#linePlusBarChart svg')
                        .datum(datum)
                        .transition().duration(500)
                        .attr('height', 450)
                        .call(chart);    });
            </script>

    """

    CHART_FILENAME = "./linebarwfocuschart.html"
    template_chart_nvd3 = NVD3Chart.template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        super(linePlusBarWithFocusChart, self).__init__(**kwargs)
        self.model = 'linePlusBarWithFocusChart'

        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)

        if kwargs.get('x_is_date', False):
            self.set_date_flag(True)

            with_focus_chart_1 = """function(d) {
                var dx = data_%s[0].values[d] && data_%s[0].values[d].x || 0;
                if (dx > 0) { return d3.time.format('%s')(new Date(dx)) }
                return null;
            }""" % (self.name, self.name, kwargs.get('x_axis_format',
                                                     '%d %b %Y %H %S'))
            self.create_x_axis('xAxis', format=with_focus_chart_1, date=False,
                               custom_format=True)

            with_focus_chart_2 = """function(d) {
                var dx = data_%s[0].values[d] && data_%s[0].values[d].x || 0;
                return d3.time.format('%s')(new Date(dx));
            }""" % (self.name, self.name, kwargs.get('x_axis_format',
                                                     '%d %b %Y %H %S'))

            self.create_x_axis('x2Axis', format=with_focus_chart_2,
                               date=False, custom_format=True)

            self.set_custom_tooltip_flag(True)
        else:
            if kwargs.get('x_axis_format') == 'AM_PM':
                # why overwrite format here?
                self.x_axis_format = format = 'AM_PM'
            else:
                format = kwargs.get('x_axis_format', '.2f')
            self.create_x_axis('xAxis', format=format)
            # self.create_x_axis('xAxis', format=".2f")

        self.create_y_axis('y1Axis', format="f")
        self.create_y_axis('y3Axis', format="f")

        self.create_y_axis('y2Axis',
                           format="function(d) { return d3.format(',.2f')(d) }",
                           custom_format=True)

        self.create_y_axis('y4Axis',
                           format="function(d) { return d3.format(',.2f')(d) }",
                           custom_format=True)

        self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
