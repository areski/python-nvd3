#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

"""

var testdata = [
  {
    "key" : "Quantity" ,
    "bar": true,
    "values" : [ [ 1136005200000 , 1271000.0] , [ 1138683600000 , 1271000.0] , [ 1141102800000 , 1271000.0] , [ 1143781200000 , 0] , [ 1146369600000 , 0] , [ 1149048000000 , 0] , [ 1151640000000 , 0] , [ 1154318400000 , 0] , [ 1156996800000 , 0] , [ 1159588800000 , 3899486.0] , [ 1162270800000 , 3899486.0] , [ 1164862800000 , 3899486.0] , [ 1167541200000 , 3564700.0] , [ 1170219600000 , 3564700.0] , [ 1172638800000 , 3564700.0] , [ 1175313600000 , 2648493.0] , [ 1177905600000 , 2648493.0] , [ 1180584000000 , 2648493.0] , [ 1183176000000 , 2522993.0] , [ 1185854400000 , 2522993.0] , [ 1188532800000 , 2522993.0] , [ 1191124800000 , 2906501.0] , [ 1193803200000 , 2906501.0] , [ 1196398800000 , 2906501.0] , [ 1199077200000 , 2206761.0] , [ 1201755600000 , 2206761.0] , [ 1204261200000 , 2206761.0] , [ 1206936000000 , 2287726.0] , [ 1209528000000 , 2287726.0] , [ 1212206400000 , 2287726.0] , [ 1214798400000 , 2732646.0] , [ 1217476800000 , 2732646.0] , [ 1220155200000 , 2732646.0] , [ 1222747200000 , 2599196.0] , [ 1225425600000 , 2599196.0] , [ 1228021200000 , 2599196.0] , [ 1230699600000 , 1924387.0] , [ 1233378000000 , 1924387.0] , [ 1235797200000 , 1924387.0] , [ 1238472000000 , 1756311.0] , [ 1241064000000 , 1756311.0] , [ 1243742400000 , 1756311.0] , [ 1246334400000 , 1743470.0] , [ 1249012800000 , 1743470.0] , [ 1251691200000 , 1743470.0] , [ 1254283200000 , 1519010.0] , [ 1256961600000 , 1519010.0] , [ 1259557200000 , 1519010.0] , [ 1262235600000 , 1591444.0] , [ 1264914000000 , 1591444.0] , [ 1267333200000 , 1591444.0] , [ 1270008000000 , 1543784.0] , [ 1272600000000 , 1543784.0] , [ 1275278400000 , 1543784.0] , [ 1277870400000 , 1309915.0] , [ 1280548800000 , 1309915.0] , [ 1283227200000 , 1309915.0] , [ 1285819200000 , 1331875.0] , [ 1288497600000 , 1331875.0] , [ 1291093200000 , 1331875.0] , [ 1293771600000 , 1331875.0] , [ 1296450000000 , 1154695.0] , [ 1298869200000 , 1154695.0] , [ 1301544000000 , 1194025.0] , [ 1304136000000 , 1194025.0] , [ 1306814400000 , 1194025.0] , [ 1309406400000 , 1194025.0] , [ 1312084800000 , 1194025.0] , [ 1314763200000 , 1244525.0] , [ 1317355200000 , 475000.0] , [ 1320033600000 , 475000.0] , [ 1322629200000 , 475000.0] , [ 1325307600000 , 690033.0] , [ 1327986000000 , 690033.0] , [ 1330491600000 , 690033.0] , [ 1333166400000 , 514733.0] , [ 1335758400000 , 514733.0]]
  },
  {
    "key" : "Price" ,
    "values" : [ [ 1136005200000 , 71.89] , [ 1138683600000 , 75.51] , [ 1141102800000 , 68.49] , [ 1143781200000 , 62.72] , [ 1146369600000 , 70.39] , [ 1149048000000 , 59.77] , [ 1151640000000 , 57.27] , [ 1154318400000 , 67.96] , [ 1156996800000 , 67.85] , [ 1159588800000 , 76.98] , [ 1162270800000 , 81.08] , [ 1164862800000 , 91.66] , [ 1167541200000 , 84.84] , [ 1170219600000 , 85.73] , [ 1172638800000 , 84.61] , [ 1175313600000 , 92.91] , [ 1177905600000 , 99.8] , [ 1180584000000 , 121.191] , [ 1183176000000 , 122.04] , [ 1185854400000 , 131.76] , [ 1188532800000 , 138.48] , [ 1191124800000 , 153.47] , [ 1193803200000 , 189.95] , [ 1196398800000 , 182.22] , [ 1199077200000 , 198.08] , [ 1201755600000 , 135.36] , [ 1204261200000 , 125.02] , [ 1206936000000 , 143.5] , [ 1209528000000 , 173.95] , [ 1212206400000 , 188.75] , [ 1214798400000 , 167.44] , [ 1217476800000 , 158.95] , [ 1220155200000 , 169.53] , [ 1222747200000 , 113.66] , [ 1225425600000 , 107.59] , [ 1228021200000 , 92.67] , [ 1230699600000 , 85.35] , [ 1233378000000 , 90.13] , [ 1235797200000 , 89.31] , [ 1238472000000 , 105.12] , [ 1241064000000 , 125.83] , [ 1243742400000 , 135.81] , [ 1246334400000 , 142.43] , [ 1249012800000 , 163.39] , [ 1251691200000 , 168.21] , [ 1254283200000 , 185.35] , [ 1256961600000 , 188.5] , [ 1259557200000 , 199.91] , [ 1262235600000 , 210.732] , [ 1264914000000 , 192.063] , [ 1267333200000 , 204.62] , [ 1270008000000 , 235.0] , [ 1272600000000 , 261.09] , [ 1275278400000 , 256.88] , [ 1277870400000 , 251.53] , [ 1280548800000 , 257.25] , [ 1283227200000 , 243.1] , [ 1285819200000 , 283.75] , [ 1288497600000 , 300.98] , [ 1291093200000 , 311.15] , [ 1293771600000 , 322.56] , [ 1296450000000 , 339.32] , [ 1298869200000 , 353.21] , [ 1301544000000 , 348.5075] , [ 1304136000000 , 350.13] , [ 1306814400000 , 347.83] , [ 1309406400000 , 335.67] , [ 1312084800000 , 390.48] , [ 1314763200000 , 384.83] , [ 1317355200000 , 381.32] , [ 1320033600000 , 404.78] , [ 1322629200000 , 382.2] , [ 1325307600000 , 405.0] , [ 1327986000000 , 456.48] , [ 1330491600000 , 542.44] , [ 1333166400000 , 599.55] , [ 1335758400000 , 583.98] ]
  }
].map(function(series) {
  series.values = series.values.map(function(d) { return {x: d[0], y: d[1] } });
  return series;
});

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
    args = None
    data = []
    axislist = {}
    style = ''  # Special style
    html = ''  # This will contain the htmloutput
    height = None
    width = None
    model = ''  # LineWithFocusChart, MultiBarChart
    d3_select_extra = ''
    x_axis_date = False

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

        self.args = kwargs

    def add_serie(self, y, x=None, name=None, **kwargs):
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

        try:
            if self.args["stacked"]:
                nvhtml += stab(2) + "chart.stacked(true);"
        except:
            pass

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

        try:
            resize = self.args["resize"]
        except:
            resize = True
        if resize:
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


if __name__ == '__main__':  # tests

    #Open File for test
    output_file = open('test.html', 'w')
    output_file.write(template_header_nvd3)

    type = "lineWithFocusChart"
    #chart = LineWithFocusChart(name=type, x=X, y=Waves)
    chart = lineWithFocusChart(name=type, date=True)
    xdata = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    xdata = map(lambda x: 1365026400000 + x * 100000, xdata)
    ydata = [1, 2, 3, 4, 5, 3, 4, 5, 5, 3, 4, 5, 5, 3, 4, 5]
    ydata2 = map(lambda x: x * 2, ydata)
    ydata3 = map(lambda x: x * 3, ydata)
    ydata4 = map(lambda x: x * 4, ydata)

    # for w in Waves:
    #     chart.add(w, x=Date)
    chart.add_serie(ydata, x=xdata)
    chart.add_serie(ydata2, x=xdata)
    chart.add_serie(ydata3, x=xdata)
    chart.add_serie(ydata4, x=xdata)
    chart.buildhtml()

    output_file.write("\n\n<h2>" + type + "</h2>\n\n")
    output_file.write(chart.html)

    #---------------------------------------
    type = "lineChart"
    #chart = LineWithFocusChart(name=type, x=X, y=Waves)
    chart = lineChart(name="lineChart", date=True)
    xdata = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    xdata = map(lambda x: 1365026400000 + x * 100000, xdata)
    ydata = [1, 2, 3, 4, 5, 3, 4, 5, 5, 3, 4, 5, 5, 3, 4, 5]
    ydata2 = map(lambda x: x * 2, ydata)

    # for w in Waves:
    #     chart.add(w, x=Date)
    chart.add_serie(ydata, x=xdata)
    chart.add_serie(ydata2, x=xdata)
    chart.buildhtml()

    output_file.write("\n\n<h2>" + type + "</h2>\n\n")
    output_file.write(chart.html)

    #---------------------------------------
    type = "MultiBarChart"
    #chart = LineWithFocusChart(name=type, x=X, y=Waves)
    chart = multiBarChart(name=type)
    xdata = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    ydata = [1, 2, 3, 4, 5, 3, 4, 5, 5, 3, 4, 5, 5, 3, 4, 5]
    ydata2 = map(lambda x: x * 2, ydata)
    ydata3 = map(lambda x: x * 3, ydata)
    ydata4 = map(lambda x: x * 4, ydata)

    # for w in Waves:
    #     chart.add(w, x=Date)
    chart.add_serie(ydata, x=xdata)
    chart.add_serie(ydata2, x=xdata)
    chart.add_serie(ydata3, x=xdata)
    chart.add_serie(ydata4, x=xdata)
    chart.buildhtml()

    output_file.write("\n\n<h2>" + type + "</h2>\n\n")
    output_file.write(chart.html)
    #---------------------------------------

    type = "pieChart"
    chart = pieChart(name=type, height=450, width=450)
    xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    ydata = [1, 2, 3, 4, 5, 3, 4]

    # for w in Waves:
    #     chart.add(w, x=Date)
    chart.add_serie(ydata, x=xdata)
    chart.buildhtml()

    output_file.write("\n\n<h2>" + type + "</h2>\n\n")
    output_file.write(chart.html)

    #---------------------------------------
    #close Html file
    output_file.close()
