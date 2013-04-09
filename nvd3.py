#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3

Part of this code is inspired from goulib
https://github.com/goulu/Goulib/blob/master/Goulib/nvd3.py

This project aims to be reusuable with less dependencies and with the aim
to power more library using it. For instance Django-Nvd3.

General aims :
- keep a separation between the templating and the output generation
- don't tie with too many dependencies
- easy to use
- clean APIs
- Documented
- Clean code / PEP8
"""

__version__ = '0.1.1'

import json
from optparse import OptionParser
from string import Template


template_page_nvd3 = """
<!DOCTYPE html>
<html lang="en">
<head>
$header
</head>
<body>
$container
$jschart
</body>
"""

#TODO: Maybe using a similar skel will improve a lot buildjschart
template_graph_nvd3 = """
nv.addGraph(function() {
    var chart = nv.models.linePlusBarChart()
        .x(function(d,i) { return i });

    chart.xAxis.tickFormat(function(d) {
      var dx = testdata[0].values[d] && testdata[0].values[d].x || 0;
      return dx ? d3.time.format('%x')(new Date(dx)) : '';
    });

    chart.y1Axis
        .tickFormat(d3.format(',f'));

    chart.y2Axis
        .tickFormat(function(d) { return '$' + d3.format(',.2f')(d) });

    chart.bars.forceY([0]);

    d3.select('#chart1 svg')
        .datum(testdata)
        .transition()
        .duration(500)
        .call(chart);

    nv.utils.windowResize(chart.update);

    return chart;
});
"""


def stab(tab=1):
    """
    create space tabulation
    """
    return ' ' * 4 * tab


class NVD3Chart:
    """
    Chart Base class
    """
    count = 0
    dateformat = '%x'
    series = []
    axislist = {}
    style = ''  # Special style
    htmlcontent = ''  # This will contain the htmloutput
    htmlheader = ''  # This will contain the html header
    height = None
    width = None
    model = ''  # LineWithFocusChart, MultiBarChart
    d3_select_extra = ''
    x_axis_date = False
    resize = False
    stacked = False
    template_page_nvd3 = None
    container = None
    containerheader = ''
    jschart = None

    header_css = ['http://nvd3.org/src/nv.d3.css']
    header_js = ['http://nvd3.org/lib/d3.v2.js', 'http://nvd3.org/nv.d3.js']

    def __init__(self, name=None, **kwargs):
        """
        Constructor
        """
        #set the model
        self.model = self.__class__.__name__

        #Init Data
        self.series = []
        self.axislist = {}
        self.template_page_nvd3 = Template(template_page_nvd3)

        if not name:
            self.count += 1
            name = "chart%d" % (self.count)
        self.name = name

        if 'stacked' in kwargs and kwargs["stacked"]:
            self.stacked = True

        if 'resize' in kwargs and kwargs["resize"]:
            self.resize = True

    def add_serie(self, y, x, name=None, **kwargs):
        """
        add serie - Series are list of data that will be plotted
        y {1, 2, 3, 4, 5} / x {1, 2, 3, 4, 5}
        """
        if not name:
            name = "Serie %d" % (len(self.series) + 1)

        if self.x_axis_date:
            #x = [d.isoformat() for d in x]
            x = [str(d) + '000' for d in x]

        serie = [{"x":x[i], "y":y} for i, y in enumerate(y)]
        data_keyvalue = {"values": serie, "key": name}

        #multiChart
        #Histogram type="bar" for the series
        if 'type' in kwargs and kwargs["type"]:
            data_keyvalue["type"] = kwargs["type"]

        #Define on which Y axis the serie is related
        #a chart can have 2 Y axis, left and right, by default only one Y Axis is used
        if 'yaxis' in kwargs and kwargs["yaxis"]:
            data_keyvalue["yAxis"] = kwargs["yaxis"]
        else:
            data_keyvalue["yAxis"] = "1"

        if 'bar' in kwargs and kwargs["bar"]:
            data_keyvalue["bar"] = 'true'

        if 'disabled' in kwargs and kwargs["disabled"]:
            data_keyvalue["disabled"] = 'true'

        self.series.append(data_keyvalue)

    def set_graph_height(self, height):
        """Set Graph height"""
        self.height = height

    def set_graph_width(self, width):
        """Set Graph width"""
        self.width = width

    def set_containerheader(self, containerheader):
        """Set containerheader"""
        self.containerheader = containerheader

    def __str__(self):
        """return htmlcontent"""
        self.buildhtml()
        return self.htmlcontent

    def buildhtml(self):
        """Build the HTML page
        Create the htmlheader with css / js
        Create html page
        Add Js code for nvd3
        """

        self.buildhtmlheader()
        self.buildcontainer()
        self.buildjschart()

        self.htmlcontent = self.template_page_nvd3.substitute(header=self.htmlheader, container=self.container, jschart=self.jschart)

    def buildhtmlheader(self):
        """generate HTML header"""

        self.htmlheader = ''
        for css in self.header_css:
            self.htmlheader += '<link media="all" href="%s" type="text/css" rel="stylesheet" />\n' % css
        for js in self.header_js:
            self.htmlheader += '<script src="%s" type="text/javascript"></script>\n' % js

    def buildcontainer(self):
        """generate HTML div"""
        self.container = self.containerheader
        #Create SVG div with style
        if self.width:
            self.style += 'width:%spx;' % self.width
        if self.height:
            self.style += 'height:%spx;' % self.height

        if self.style:
            self.style = 'style="%s"' % self.style

        self.container += '<div id="%s"><svg %s></svg></div>\n' % (self.name, self.style)

    def buildjschart(self):
        """generate javascript code for the chart"""

        self.jschart = ''
        self.jschart += '\n<script type="text/javascript">\n' + \
            stab() + 'nv.addGraph(function() {\n'

        self.jschart += stab(2) + 'var chart = nv.models.%s();\n' % self.model

        #TODO: Move this code to pieChart
        if self.model == 'pieChart':
            self.jschart += stab(2) + 'chart.x(function(d) { return d.x })\n' + \
                stab(3) + '.y(function(d) { return d.y })\n' + \
                stab(3) + '.values(function(d) { return d })\n' + \
                stab(3) + '.color(d3.scale.category10().range());\n'
            if self.width:
                self.jschart += stab(2) + 'chart.width(%s);\n' % self.width
            if self.height:
                self.jschart += stab(2) + 'chart.height(%s);\n' % self.height

        if self.stacked:
            self.jschart += stab(2) + "chart.stacked(true);"

        # custom tooltip can goes here
        #chart.tooltipContent(function(key, y, e, graph) { return 'Some String' });

        """
        We want now to loop through all the defined Axis and add:
            chart.y2Axis
                .tickFormat(function(d) { return '$' + d3.format(',.2f')(d) });
        """
        if self.model != 'pieChart':
            for axis_name, a in self.axislist.iteritems():
                self.jschart += stab(2) + "chart.%s\n" % axis_name
                for attr, value in a.iteritems():
                    self.jschart += stab(3) + ".%s(%s)\n" % (attr, value)

        #if self.model == 'pieChart':
        if self.width:
            self.d3_select_extra += ".attr('width', %s)\n" % self.width
        if self.height:
            self.d3_select_extra += ".attr('height', %s)\n" % self.height

        datum = "data_%s" % self.name
        if self.model == 'pieChart':
            datum = "[data_%s[0].values]" % self.name

        #Inject data to D3
        self.jschart += stab(2) + "d3.select('#%s svg')\n" % self.name + \
            stab(3) + ".datum(%s)\n" % datum + \
            stab(3) + ".transition().duration(500)\n" + \
            stab(3) + self.d3_select_extra + \
            stab(3) + ".call(chart);\n\n"

        if self.resize:
            self.jschart += stab(1) + "nv.utils.windowResize(chart.update);\n"
        self.jschart += stab(1) + "return chart;\n});\n"

        #Include data
        self.jschart += """data_%s=%s;\n</script>""" % (self.name, json.dumps(self.series))

    #TODO : Check if it might not make sense to have create_x_axis, create_y_axis
    def set_axis(self, name, label=None, format=".2f", date=False):
        """
        Create axis
        """
        axis = {}
        axis["tickFormat"] = "d3.format(',%s')" % format
        if label:
            axis["axisLabel"] = label

        #date format : see https://github.com/mbostock/d3/wiki/Time-Formatting
        if date:
            self.dateformat = format
            axis["tickFormat"] = "function(d) { return d3.time.format('%s')(new Date(d)) }\n" % self.dateformat
            #flag is the x Axis is a date
            if name[0] == 'x':
                self.x_axis_date = True

        #Add new axis to list of axis
        self.axislist[name] = axis


"""
The following classes correspond to those defined in nv.d3.js
Examples : http://nvd3.org/ghpages/examples.html

Currently implemented nvd3 chart:

* lineWithFocusChart
* lineChart
* multiBarChart
* pieChart
* stackedAreaChart
* stackedAreaChart

"""


#TODO: Add extensive documentation on lineWithFocusChart
#settings supported
#examples
class lineWithFocusChart(NVD3Chart):
    """
    usage ::

        chart = nvd3.lineWithFocusChart(name='lineWithFocusChart', date=True)
        xdata = [1365026400000000, 1365026500000000, 1365026600000000]
        ydata = [-6, 5, -1]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    js-code ::

        data_lineWithFocusChart = [{ "key" : "Serie 1",
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
                var chart = nv.models.lineWithFocusChart();
                chart.yAxis
                    .tickFormat(d3.format(',.2f'))
                chart.y2Axis
                    .tickFormat(d3.format(',.2f'))
                chart.xAxis
                    .tickFormat(function(d) { return d3.time.format('%d %b %y')(new Date(d)) })
                chart.x2Axis
                    .tickFormat(function(d) { return d3.time.format('%d %b %y')(new Date(d)) })
                d3.select('#lineWithFocusChart svg')
                    .datum(data_lineWithFocusChart)
                    .transition()
                    .duration(500)
                    .call(chart);
            return chart;
        });
    """
    def __init__(self, height=450, width=None, date=False, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        if date:
            self.set_axis('xAxis', format='%d %b %y', date=True)
            self.set_axis('x2Axis', format='%d %b %y', date=True)
        else:
            self.set_axis('xAxis', format=".2f")
            self.set_axis('x2Axis', format=".2f")
        self.set_axis('yAxis', format=".2f")
        self.set_axis('y2Axis', format=".2f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)


#TODO: Add extensive documentation on lineChart
#settings supported
#examples
class lineChart(NVD3Chart):
    """
    usage ::

        chart = nvd3.lineChart(name='lineChart', height=400, width=400, date=True)
        xdata = [1365026400000000, 1365026500000000, 1365026600000000]
        ydata = [-6, 5, -1]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    js-code ::

        data_lineChart = [{ "key" : "Serie 1",
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
            self.set_axis('xAxis', format='%d %b %y', date=True)
        else:
            self.set_axis('xAxis', format=".2f")
        self.set_axis('yAxis', format=".2f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)


#TODO: Add extensive documentation on multiBarChart
#settings supported
#examples
class multiBarChart(NVD3Chart):
    """
    usage ::

        chart = nvd3.multiBarChart(name='multiBarChart', height=400, width=400)
        xdata = [0, 1, 3, 4]
        ydata = [6, 12, 9, 16]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    js-code ::

        data_MultiBarChart = [{ "key" : "Serie 1",
           "values" : [
                { "x" : 0
                  "y" : 6
                },
                { "x" : 1,
                  "y" : 12
                },
                { "x" : 3,
                  "y" : 9
                },
              ],
            "yAxis" : "1"
        }]

        nv.addGraph(function() {
            var chart = nv.models.multiBarChart();
            chart.xAxis
                .tickFormat(d3.format(',.2f'))
            chart.yAxis
                .tickFormat(d3.format(',.2f'))
            d3.select('#MultiBarChart svg')
                .datum(data_MultiBarChart)
                .transition()
                .duration(500)
                .call(chart);
            return chart;
        });
    """
    def __init__(self, height=450, width=None, date=False, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        if date:
            self.set_axis('xAxis', format='%d %b %y', date=True)
        else:
            self.set_axis('xAxis', format=".2f")
        self.set_axis('yAxis', format=".2f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)


#TODO: Add extensive documentation on StackedAreaChart
#settings supported
#examples
class stackedAreaChart(NVD3Chart):
    """
    usage ::

        chart = nvd3.stackedAreaChart(name='stackedAreaChart', height=400, width=400)
        xdata = [100, 101, 102, 103, 104, 105, 106,]
        ydata = [6, 11, 12, 7, 11, 10, 11]
        ydata2 = [8, 20, 16, 12, 20, 28, 28]
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    js example::

        data_stackedAreaChart = [{
                  "values":[
                     {
                        "y":9,
                        "x":100
                     },
                     {
                        "y":5,
                        "x":101
                     },
                  ],
                  "key":"Serie 1",
                  "yAxis":"1"
               },
               {
                  "values":[
                     {
                        "y":18,
                        "x":100
                     },
                     {
                        "y":10,
                        "x":101
                     },
                  ],
                  "key":"Serie 2",
                  "yAxis":"1"
               }
            ]

        nv.addGraph(function() {
            var chart = nv.models.stackedAreaChart();
            chart.xAxis
                .tickFormat(d3.format(',.2f'))
            chart.yAxis
                .tickFormat(d3.format(',.2f'))
            d3.select('#stackedAreaChart svg')
                .datum(data_stackedAreaChart)
                .transition()
                .duration(500)
                .call(chart);
            return chart;
        });
    """
    def __init__(self, height=450, width=None, date=False, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        if date:
            self.set_axis('xAxis', format='%d %b %y', date=True)
        else:
            self.set_axis('xAxis', format=".2f")
        self.set_axis('yAxis', format=".2f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)


#TODO: Add extensive documentation on pieChart
#settings supported
#examples
class pieChart(NVD3Chart):
    """
    usage ::

        chart = nvd3.pieChart(name='pieChart', height=400, width=400)
        xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
        ydata = [3, 4, 0, 1, 5, 7, 3]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    js example::

        data = [{ key: "Cumulative Return",
                  values: [
                    {
                      "label": "One",
                      "value" : 29.765957771107
                    },
                    {
                      "label": "Two",
                      "value" : 0
                    },
                    {
                      "label": "Three",
                      "value" : 32.807804682612
                    },
                  ]
                }]

        nv.addGraph(function() {
          var chart = nv.models.pieChart()
              .x(function(d) { return d.label })
              .y(function(d) { return d.value })
              .showLabels(true);

            d3.select("#div_id")
                .datum(data)
                .transition()
                .duration(1200)
                .call(chart);

          return chart;
        });
    """
    def __init__(self, height=450, width=None, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        self.set_axis('xAxis')
        self.set_axis('yAxis')
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)

    # def buildjschart(self):
    #     """generate javascript code for the chart"""

    #     self.jschart = ''
    #     self.jschart += '\n<script type="text/javascript">\n' + \
    #         stab() + 'nv.addGraph(function() {\n'

    #     self.jschart += stab(2) + 'var chart = nv.models.%s();\n' % self.model

    #     self.jschart += stab(2) + 'chart.x(function(d) { return d.x })\n' + \
    #         stab(3) + '.y(function(d) { return d.y })\n' + \
    #         stab(3) + '.values(function(d) { return d })\n' + \
    #         stab(3) + '.color(d3.scale.category10().range());\n'

    #     if self.width:
    #         self.jschart += stab(2) + 'chart.width(%s);\n' % self.width
    #         self.d3_select_extra += ".attr('width', %s)\n" % self.width
    #     if self.height:
    #         self.jschart += stab(2) + 'chart.height(%s);\n' % self.height
    #         self.d3_select_extra += ".attr('height', %s)\n" % self.height

    #     datum = "data_%s" % self.name
    #     datum = "[data_%s[0].values]" % self.name

    #     #Inject data to D3
    #     self.jschart += stab(2) + "d3.select('#%s svg')\n" % self.name + \
    #         stab(3) + ".datum(%s)\n" % datum + \
    #         stab(3) + ".transition().duration(500)\n" + \
    #         stab(3) + self.d3_select_extra + \
    #         stab(3) + ".call(chart);\n\n"

    #     if self.resize:
    #         self.jschart += stab(1) + "nv.utils.windowResize(chart.update);\n"
    #     self.jschart += stab(1) + "return chart;\n});\n"

    #     #Include data
    #     self.jschart += """data_%s=%s;\n</script>""" % (self.name, json.dumps(self.series))


def _main():
    """
    Parse options and process commands
    """
    # Parse arguments
    usage = "usage: nvd3.py [options]"
    parser = OptionParser(usage=usage, version="python-nvd3 " + __version__ + " - Python wrapper for nvd3 ")
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print messages to stdout")

    (options, args) = parser.parse_args()


if __name__ == '__main__':
    _main()
