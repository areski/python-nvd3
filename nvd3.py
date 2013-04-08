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

__version__ = '0.1.0'

import json


#for template we might want to use something like Jinja2
#http://docs.python.org/2/library/string.html#template-strings
template_header_nvd3 = """
<!DOCTYPE html>
<html lang="en">
<head>
<link media="all" href="http://nvd3.org/src/nv.d3.css" type="text/css" rel="stylesheet" />
<script src="http://nvd3.org/lib/d3.v2.js" type="text/javascript"></script>
<script src="http://nvd3.org/nv.d3.js" type="text/javascript"></script>
</head>
<body>
"""

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
      .transition().duration(500).call(chart);

    nv.utils.windowResize(chart.update);

    return chart;
});

</script>
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
    data = []
    axislist = {}
    style = ''  # Special style
    html = ''  # This will contain the htmloutput
    height = None
    width = None
    model = ''  # LineWithFocusChart, MultiBarChart
    d3_select_extra = ''
    x_axis_date = False
    resize = False
    stacked = False

    def __init__(self, name=None, **kwargs):
        """
        Constructor
        """
        #set the model
        self.model = self.__class__.__name__

        #Init Data
        self.data = []
        self.axislist = {}

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
            name = "Serie %d" % (len(self.data) + 1)

        if self.x_axis_date:
            #x = [d.isoformat() for d in x]
            x = [str(d) + '000' for d in x]

        serie = [{"x":x[i], "y":y} for i, y in enumerate(y)]
        data = {"values": serie, "key": name}

        #multiChart
        try:
            data["type"] = kwargs["type"]
        except:
            pass

        try:
            data["yAxis"] = kwargs["axis"]
        except:
            data["yAxis"] = "1"

        try:
            if kwargs["bar"]:
                data["bar"] = 'true'
        except:
            pass

        try:
            data["disabled"] = kwargs["disabled"]
        except:
            pass

        self.data.append(data)

    def set_graph_height(self, height):
        """Set Graph height"""
        self.height = height

    def set_graph_width(self, width):
        """Set Graph width"""
        self.width = width

    def __str__(self):
        self.buildhtml()
        return self.html

    def buildhtml(self):
        """generate HTML div"""

        #Create SVG div with style
        if self.width:
            self.style += 'width:%spx;' % self.width
        if self.height:
            self.style += 'height:%spx;' % self.height

        if self.style:
            self.style = ' style="%s"' % self.style
        nvhtml = '<div id="%s"><svg%s></svg></div>\n' % (self.name, self.style)

        #Generate Javascript
        nvhtml += '\n<script type="text/javascript">\n' + \
            stab() + 'nv.addGraph(function() {\n'

        nvhtml += stab(2) + 'var chart = nv.models.%s();\n' % self.model

        #TODO: Move to pieChart
        if self.model == 'pieChart':
            nvhtml += stab(2) + 'chart.x(function(d) { return d.x })\n' + \
                stab(3) + '.y(function(d) { return d.y })\n' + \
                stab(3) + '.values(function(d) { return d })\n' + \
                stab(3) + '.color(d3.scale.category10().range());\n'

            if self.width:
                nvhtml += stab(2) + 'chart.width(%s);\n' % self.width
            if self.height:
                nvhtml += stab(2) + 'chart.height(%s);\n' % self.height

        if self.stacked:
            nvhtml += stab(2) + "chart.stacked(true);"

        """
        We want now to loop through all the defined Axis and add:
            chart.y2Axis
                .tickFormat(function(d) { return '$' + d3.format(',.2f')(d) });
        """
        if self.model != 'pieChart':
            for axis_name, a in self.axislist.iteritems():
                nvhtml += stab(2) + "chart.%s\n" % axis_name
                for attr, value in a.iteritems():
                    nvhtml += stab(3) + ".%s(%s)\n" % (attr, value)

        if self.model == 'pieChart':
            if self.width:
                self.d3_select_extra += ".attr('width', %s)\n" % self.width
            if self.height:
                self.d3_select_extra += ".attr('height', %s)\n" % self.height

        datum = "data_%s" % self.name
        if self.model == 'pieChart':
            datum = "[data_%s[0].values]" % self.name

        #Inject data to D3
        nvhtml += stab(2) + "d3.select('#%s svg')\n" % self.name + \
            stab(3) + ".datum(%s)\n" % datum + \
            stab(3) + ".transition().duration(500)\n" + \
            stab(3) + self.d3_select_extra + \
            stab(3) + ".call(chart);\n\n"

        if self.resize:
            nvhtml += "    nv.utils.windowResize(chart.update);\n"
        nvhtml += "    return chart;\n});\n"
        nvhtml += """data_%s=%s;\n</script>""" % (
            self.name, json.dumps(self.data))
        self.html = nvhtml

    #TODO : Check if it might not make sense to have create_x_axis, create_y_axis
    def create_axis(self, name, label=None, format=".2f", date=False):
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

Currently implemented:
    lineWithFocusChart
    lineChart
    multiBarChart
    pieChart

"""


class lineWithFocusChart(NVD3Chart):
    def __init__(self, height=450, width=None, date=False, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        if date:
            self.create_axis('xAxis', format='%d %b %y', date=True)
            self.create_axis('x2Axis', format='%d %b %y', date=True)
        else:
            self.create_axis('xAxis', format=".2f")
            self.create_axis('x2Axis', format=".2f")
        self.create_axis('yAxis', format=".2f")
        self.create_axis('y2Axis', format=".2f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(450)
        if width:
            self.set_graph_width(450)


class lineChart(NVD3Chart):
    def __init__(self, height=450, width=None, date=False, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        if date:
            self.create_axis('xAxis', format='%d %b %y', date=True)
        else:
            self.create_axis('xAxis', format=".2f")
        self.create_axis('yAxis', format=".2f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(450)
        if width:
            self.set_graph_width(450)


class multiBarChart(NVD3Chart):
    def __init__(self, height=450, width=None, date=False, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        if date:
            self.create_axis('xAxis', format='%d %b %y', date=True)
        else:
            self.create_axis('xAxis', format=".2f")
        self.create_axis('yAxis', format=".2f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(450)
        if width:
            self.set_graph_width(450)


class pieChart(NVD3Chart):
    def __init__(self, height=450, width=None, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        self.create_axis('xAxis')
        self.create_axis('yAxis')
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(450)
        if width:
            self.set_graph_width(450)
