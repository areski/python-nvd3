.. _lineWithFocusChart-model:

:class:`lineWithFocusChart`
---------------------------



python-example ::

        from nvd3 import lineWithFocusChart
        chart = lineWithFocusChart(name='lineWithFocusChart', date=True)
        xdata = [1365026400000000, 1365026500000000, 1365026600000000]
        ydata = [-6, 5, -1]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

js example::

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



.. image:: https://raw.github.com/areski/python-nvd3/master/screenshot/lineWithFocusChart.png
