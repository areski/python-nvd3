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
# from jinja2 import DebugUndefined, Template
import os


class pieChart(NVD3Chart):
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

    Javascript generated:

    .. raw:: html

        <div id="pieChart"><svg style="height:450px;"></svg></div>
        <script>


            data_pieChart=[{"values": [{"value": 3, "label": "Orange"},
                           {"value": 4, "label": "Banana"},
                           {"value": 0, "label": "Pear"},
                           {"value": 1, "label": "Kiwi"},
                           {"value": 5, "label": "Apple"},
                           {"value": 7, "label": "Strawberry"},
                           {"value": 3, "label": "Pineapple"}],
                           "key": "Serie 1"}];

            nv.addGraph(function() {
                var chart = nv.models.pieChart();
                chart.margin({top: 30, right: 60, bottom: 20, left: 60});
                var datum = data_pieChart[0].values;
                        chart.tooltipContent(function(key, y, e, graph) {
                            var x = String(key);
                            var y =  String(y)  + ' cal';

                            tooltip_str = '<center><b>'+x+'</b></center>' + y;
                            return tooltip_str;
                        });
                    chart.showLegend(true);
                    chart.showLabels(true);
                    chart.donut(false);
                chart
                    .x(function(d) { return d.label })
                    .y(function(d) { return d.value });
                chart.width(400);
                chart.height(400);

                d3.select('#pieChart svg')
                    .datum(datum)
                    .transition().duration(500)
                    .attr('width', 400)
                    .attr('height', 400)
                    .call(chart);  });
        </script>

    """

    CHART_FILENAME = "./pie.html"

    template_environment = Environment(lstrip_blocks=True, trim_blocks=True)
    template_environment.loader = FileSystemLoader(os.path.join(
        os.path.dirname(__file__), 'templates'))
    template_chart_nvd3 = template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
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

    def buildjschart(self):
        NVD3Chart.buildjschart(self)
        self.jschart = self.template_chart_nvd3.render(chart=self)


class PieChart(NVD3Chart):

    CHART_FILENAME = "./piechart.html"

    template_environment = Environment(lstrip_blocks=True, trim_blocks=True)
    template_environment.loader = FileSystemLoader(os.path.join(
        os.path.dirname(__file__), 'templates'))
    template_chart_nvd3 = template_environment.get_template(CHART_FILENAME)

    def __init__(self, **kwargs):
        super(PieChart, self).__init__(**kwargs)

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

    def buildjschart(self):
        """
        This only renders the template discretebarchart.html,
        the rest of the body is renderd by calling NVD3Chart.buildhtml
        """
        super(PieChart, self).buildjschart()

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
