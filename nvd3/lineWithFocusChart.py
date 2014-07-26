#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from .NVD3Chart import NVD3Chart
from jinja2 import Environment, FileSystemLoader
import os


class lineWithFocusChart(NVD3Chart):
    """
    A lineWithFocusChart or line graph is a type of chart which displays information
    as a series of data points connected by straight line segments.
    The lineWithFocusChart provide a smaller chart that act as a selector,
    this is very useful if you want to zoom on a specific time period.

    Python example::

        from nvd3 import lineWithFocusChart
        chart = lineWithFocusChart(name='lineWithFocusChart', x_is_date=True, x_axis_format="%d %b %Y")
        xdata = [1365026400000000, 1365026500000000, 1365026600000000]
        ydata = [-6, 5, -1]

        extra_serie = {"tooltip": {"y_start": "", "y_end": " ext"},
                       "date_format": "%d %b %Y"}
        chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie)
        chart.buildhtml()

    Javascript generated:

    .. raw:: html

        <div id="lineWithFocusChart"><svg style="height:450px;"></svg></div>
        <script>
            data_lineWithFocusChart=[{"values": [{"y": -6, "x": 1365026400000000}, {"y": 5, "x": 1365026500000000}, {"y": -1, "x": 1365026600000000}], "key": "Serie 1", "yAxis": "1"}];
            nv.addGraph(function() {
                var chart = nv.models.lineWithFocusChart();
                chart.margin({top: 30, right: 60, bottom: 20, left: 60});
                var datum = data_lineWithFocusChart;
                        chart.yAxis
                            .tickFormat(d3.format(',.2f'));
                        chart.y2Axis
                            .tickFormat(d3.format(',.2f'));
                        chart.xAxis
                            .tickFormat(function(d) { return d3.time.format('%d %b %Y')(new Date(parseInt(d))) });
                        chart.x2Axis
                            .tickFormat(function(d) { return d3.time.format('%d %b %Y')(new Date(parseInt(d))) });

                    chart.tooltipContent(function(key, y, e, graph) {
                        var x = d3.time.format("%d %b %Y")(new Date(parseInt(graph.point.x)));
                        var y = String(graph.point.y);
                                            if(key == 'Serie 1'){
                                var y =  String(graph.point.y)  + ' ext';
                            }

                        tooltip_str = '<center><b>'+key+'</b></center>' + y + ' on ' + x;
                        return tooltip_str; });

                    chart.showLegend(true);

                d3.select('#lineWithFocusChart svg')
                    .datum(datum)
                    .transition().duration(500)
                    .attr('height', 450)
                    .call(chart); });
        </script>

    """
    def __init__(self, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)

        if kwargs.get('x_is_date', False):
            self.set_date_flag(True)
            self.create_x_axis('xAxis', format=kwargs.get('x_axis_format', '%d %b %Y %H %S'), date=True)
            self.create_x_axis('x2Axis', format=kwargs.get('x_axis_format', '%d %b %Y %H %S'), date=True)
            self.set_custom_tooltip_flag(True)
        else:
            self.create_x_axis('xAxis', format=kwargs.get('x_axis_format', '.2f'))
            self.create_x_axis('x2Axis', format=kwargs.get('x_axis_format', '.2f'))

        self.create_y_axis('yAxis', format=kwargs.get('y_axis_format', '.2f'))
        self.create_y_axis('y2Axis', format=kwargs.get('y_axis_format', '.2f'))

        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)

class LineWithFocusChart(NVD3Chart):

    CHART_FILENAME = "./linewfocuschart.html"

    template_environment = Environment(lstrip_blocks=True, trim_blocks=True)
    template_environment.loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
    template_chart_nvd3 = template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        super(LineWithFocusChart, self).__init__(**kwargs)
        self.model = 'lineWithFocusChart'

        height = kwargs.get('height', 450)
        width = kwargs.get('width', None)

        if kwargs.get('x_is_date', False):
            self.set_date_flag(True)
            self.create_x_axis('xAxis', format=kwargs.get('x_axis_format', '%d %b %Y %H %S'), date=True)
            self.create_x_axis('x2Axis', format=kwargs.get('x_axis_format', '%d %b %Y %H %S'), date=True)
            self.set_custom_tooltip_flag(True)
        else:
            self.create_x_axis('xAxis', format=kwargs.get('x_axis_format', '.2f'))
            self.create_x_axis('x2Axis', format=kwargs.get('x_axis_format', '.2f'))

        self.create_y_axis('yAxis', format=kwargs.get('y_axis_format', '.2f'))
        self.create_y_axis('y2Axis', format=kwargs.get('y_axis_format', '.2f'))

        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)

    def buildjschart(self):
        """
        This only renders the template discretebarchart.html,
        the rest of the body is renderd by calling NVD3Chart.buildhtml
        """
        NVD3Chart.buildjschart(self)

    def buildcontent(self):
        """Build HTML content only, no header or body tags. To be useful this
        will usually require the attribute `juqery_on_ready` to be set which
        will wrap the js in $(function(){<regular_js>};)
        """
        self.buildcontainer()
        # if the subclass has a method buildjs this method will be
        # called instead of the method defined here
        # when this subclass method is entered it does call
        # the method buildjschart defined here
        self.buildjschart()
        self.htmlcontent = self.template_chart_nvd3.render(chart=self)

    def buildhtml(self):
        """Build the HTML page
        Create the htmlheader with css / js
        Create html page
        Add Js code for nvd3
        """
        self.buildcontent()
        self.content = self.htmlcontent
        self.htmlcontent = self.template_page_nvd3.render(chart=self)
