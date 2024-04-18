.. python-nvd3 documentation master file, created by
   sphinx-quickstart on Thu Dec  8 12:55:34 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python-nvd3 Documentation!
==========================

:Release: |version|
:Date: |today|
:Keywords: python, plot, graph, nvd3, d3
:Author: Arezqui Belaid
:Description: Python wrapper for nvd3, build re-usable charts and chart components for d3.js

NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js offers you.

Python-NVD3 makes your life easy! You write Python and the library
renders JavaScript for you!
These graphs can be part of your web application:

 .. image:: https://raw.githubusercontent.com/areski/python-nvd3/develop/docs/showcase/multiple-charts.png


Want to try it yourself? Install python-nvd3, enter your python shell and try this quick demo::

    >>> from nvd3 import pieChart
    >>> chart_name = 'pieChart'
    >>> chart = pieChart(name=chart_name, color_category='category20c', height=450, width=450)
    >>> xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    >>> ydata = [3, 4, 0, 1, 5, 7, 3]
    >>> extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    >>> chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
    >>> chart.buildcontent()
    >>> print chart.htmlcontent


This will output the following HTML to render a live chart. The HTML could be stored into a HTML file, used in a Web application, or even used via Ipython Notebook::

    <div id="pieChart"><svg style="width:450px;height:450px;"></svg></div>
    <script>
    data_pieChart=[{"values": [{"value": 3, "label": "Orange"},
                   {"value": 4, "label": "Banana"},
                   {"value": 0, "label": "Pear"},
                   {"value": 1, "label": "Kiwi"},
                   {"value": 5, "label": "Apple"},
                   {"value": 7, "label": "Strawberry"},
                   {"value": 3, "label": "Pineapple"}], "key": "Serie 1"}];

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
        chart.width(450);
        chart.height(450);
        d3.select('#pieChart svg')
            .datum(datum)
            .transition().duration(500)
            .attr('width', 450)
            .attr('height', 450)
            .call(chart);
    });
    </script>


Check out the class references for dynamic examples and a full list of supported charts!

Excited !? Learn more here:


.. toctree::
    :maxdepth: 2

    introduction
    resources
    chart-classes
    examples-of-chart-types

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

