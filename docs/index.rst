.. labibi documentation master file, created by
   sphinx-quickstart on Sun Nov  4 10:10:29 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python-nvd3 Documentation!
==========================

:Release: |version|
:Date: |today|
:Keywords: python, plot, graph, nvd3, d3
:Author: Arezqui Belaid
:Description: Python wrapper for nvd3, build re-usable charts and chart components for d3.js

Contents:

.. toctree::
    :maxdepth: 2

    introduction
    chart-classes
    resources
    modules

The following python code will create the graph bellow::

    from nvd3 import pieChart

    #Open File for test
    output_file = open('test_pieChart.html', 'w')

    type = "pieChart"
    chart = pieChart(name=type, color_category='category20c', height=400, width=400)
    chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    ydata = [3, 4, 0, 1, 5, 7, 3]

    chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
    chart.buildhtml()

.. raw:: html

    <div id="pieChart"><svg style="width:400px;height:400px;"></svg></div>
    <script>

        data_pieChart=[{"values": [{"value": 3, "label": "Orange"}, {"value": 4, "label": "Banana"}, {"value": 0, "label": "Pear"}, {"value": 1, "label": "Kiwi"}, {"value": 5, "label": "Apple"}, {"value": 7, "label": "Strawberry"}, {"value": 3, "label": "Pineapple"}], "key": "Serie 1"}];
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
                .call(chart);
        });
    </script>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

