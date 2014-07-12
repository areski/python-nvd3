.. automodule:: nvd3.pieChart

.. _pieChart-model:

:class:`pieChart`
-----------------

.. autoclass:: pieChart

The following python code will produce the graph::

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

    <div id="multiBarChart"><svg style="height:350px;"></svg></div>
    <script>

        data_multiBarChart=[{"values": [{"y": 3, "x": 0}, {"y": 5, "x": 1}, {"y": 5, "x": 2}, {"y": 7, "x": 3}, {"y": 6, "x": 4}, {"y": 9, "x": 5}, {"y": 7, "x": 6}, {"y": 2, "x": 7}, {"y": 2, "x": 8}, {"y": 8, "x": 9}], "key": "Count", "yAxis": "1"}, {"values": [{"y": 6, "x": 0}, {"y": 10, "x": 1}, {"y": 10, "x": 2}, {"y": 14, "x": 3}, {"y": 12, "x": 4}, {"y": 18, "x": 5}, {"y": 14, "x": 6}, {"y": 4, "x": 7}, {"y": 4, "x": 8}, {"y": 16, "x": 9}], "key": "Duration", "yAxis": "1"}];
        nv.addGraph(function() {
            var chart = nv.models.multiBarChart();
            chart.margin({top: 30, right: 60, bottom: 20, left: 60});
            var datum = data_multiBarChart;

                    chart.xAxis
                        .tickFormat(d3.format(',.2f'));
                    chart.yAxis
                        .tickFormat(d3.format(',.2f'));
                    chart.tooltipContent(function(key, y, e, graph) {
                        var x = String(graph.point.x);
                        var y = String(graph.point.y);
                                            if(key == 'Count'){
                            var y =  String(graph.point.y)  + ' call';
                        }
                        if(key == 'Duration'){
                            var y =  String(graph.point.y)  + ' min';
                        }

                        tooltip_str = '<center><b>'+key+'</b></center>' + y + ' at ' + x;
                        return tooltip_str;
                    });

                chart.showLegend(true);

            d3.select('#multiBarChart svg')
                .datum(datum)
                .transition().duration(500)
                .attr('height', 350)
                .call(chart);
        });

    </script>

