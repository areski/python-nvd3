#!/usr/bin/python
# -*- coding: utf-8 -*-
from optparse import OptionParser
from string import Template
import random

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
    NVD3Chart Base class

    **Attributes**:

        * ``count`` - chart count
        * ``dateformat`` - see https://github.com/mbostock/d3/wiki/Time-Formatting
        * ``series`` - Series are list of data that will be plotted
        * ``axislist`` - All X, Y axis list
        * ``style`` - Special style
        * ``htmlcontent`` - Contain the htmloutput
        * ``htmlheader`` - Contain the html header
        * ``height`` - Set graph height
        * ``width`` - Set graph width
        * ``model`` - set the model (ex. pieChart, LineWithFocusChart, MultiBarChart)
        * ``d3_select_extra`` -
        * ``x_axis_date`` - False / True
        * ``resize`` - False / True
        * ``stacked`` - False / True
        * ``template_page_nvd3`` - template variable
        * ``container`` - Place for graph
        * ``containerheader`` - Header for javascript code
        * ``jschart`` - Javascript code as string
        * ``custom_tooltip_flag`` - False / True
        * ``charttooltip`` - Custom tooltip string
        * ``header_css`` - False / True
        * ``header_js`` - Custom tooltip string
    """
    count = 0
    dateformat = '%x'
    series = []
    axislist = {}
    style = ''
    htmlcontent = ''
    htmlheader = ''
    height = None
    width = None
    model = ''
    d3_select_extra = ''
    x_axis_date = False
    resize = False
    stacked = False
    template_page_nvd3 = None
    container = None
    containerheader = ''
    jschart = None
    custom_tooltip_flag = False
    charttooltip = None

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
            x = [str(d) for d in x]

        x = sorted(x)
        if 'shape' in kwargs:
            serie = [{"x": x[i], "y": y, "shape": kwargs["shape"], "size": random.randint(1, 3)} for i, y in enumerate(y)]
        else:
            serie = [{"x": x[i], "y": y} for i, y in enumerate(y)]

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

    def set_custom_tooltip_flag(self, custom_tooltip_flag):
        """Set custom_tooltip_flag"""
        self.custom_tooltip_flag = custom_tooltip_flag

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

    def buildtooltip(self):
        """generate custom tooltip for the chart"""
        if self.custom_tooltip_flag:
            self.charttooltip = stab(2) + "chart.tooltipContent(function(key, y, e, graph) {\n" + \
                stab(3) + "var x = d3.time.format('%s')(new Date(parseInt(graph.point.x)));\n" % self.dateformat +\
                stab(3) + "tooltip_str = '<center><b>'+key+'</b></center>' + graph.point.y +' on ' + x ;" +\
                stab(3) + "return tooltip_str;\n" + \
                stab(2) + "});\n"

    def buildjschart(self):
        """generate javascript code for the chart"""

        self.jschart = ''
        self.jschart += '\n<script type="text/javascript">\n' + \
            stab() + 'nv.addGraph(function() {\n'

        self.jschart += stab(2) + 'var chart = nv.models.%s();\n' % self.model
        if self.stacked:
            self.jschart += stab(2) + "chart.stacked(true);"

        """
        We want now to loop through all the defined Axis and add:
            chart.y2Axis
                .tickFormat(function(d) { return '$' + d3.format(',.2f')(d) });
        """
        if self.model != 'pieChart':
            for axis_name, a in self.axislist.iteritems():
                self.jschart += stab(2) + "chart.%s\n" % axis_name
                for attr, value in a.iteritems():
                    self.jschart += stab(3) + ".%s(%s);\n" % (attr, value)

        if self.width:
            self.d3_select_extra += ".attr('width', %s)\n" % self.width
        if self.height:
            self.d3_select_extra += ".attr('height', %s)\n" % self.height

        datum = "data_%s" % self.name
        if self.model == 'pieChart':
            datum = "[data_%s[0].values]" % self.name

        # add custom tooltip string in jschart
        if self.custom_tooltip_flag:
            self.buildtooltip()
            self.jschart += self.charttooltip

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
        self.jschart += """data_%s=%s;\n</script>""" % (self.name, self.series)

    def create_x_axis(self, name, label=None, format=None, date=False):
        """
        Create X-axis
        """
        axis = {}
        if format:
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

    def create_y_axis(self, name, label=None, format=None, custom_format=False):
        """
        Create Y-axis
        """
        axis = {}

        if custom_format and format:
            axis["tickFormat"] = format
        else:
            if format:
                axis["tickFormat"] = "d3.format(',%s')" % format

        if label:
            axis["axisLabel"] = label

        #Add new axis to list of axis
        self.axislist[name] = axis


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
