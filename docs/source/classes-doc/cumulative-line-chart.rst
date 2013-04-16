.. _cumulativeLineChart-model:

:class:`cumulativeLineChart`
----------------------------

A cumulative line chart is used when you have one important grouping representing an ordered set of data and one value to show, summed over time.

python-example ::

        from nvd3 import cumulativeLineChart
        chart = cumulativeLineChart(name='cumulativeLineChart', date=True)
        xdata = [1365026400000000, 1365026500000000, 1365026600000000]
        ydata = [-6, 5, -1]
        y2data = [36, 55, 11]
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=y2data, x=xdata)
        chart.buildhtml()

js example::

        data_lineWithFocusChart = [
            {
               "key" : "Serie 1",
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
            },
            {
               "key" : "Serie 2",
               "values" : [
                    { "x" : "1365026400000000",
                      "y" : 34
                    },
                    { "x" : "1365026500000000",
                      "y" : 56
                    },
                    { "x" : "1365026600000000",
                      "y" : 32
                    },
                  ],
            }
        ]

        nv.addGraph(function() {
            var chart = nv.models.cumulativeLineChart();

            chart.xAxis
                .tickFormat(function(d) { return d3.time.format('%d %b %Y')(new Date(d)) });
            chart.y1Axis
                .tickFormat(d3.format('.1%'));

            d3.select('#cumulativeLineChart svg')
                .datum(data_linePlusBarChart)
                .transition().duration(500)
                .attr('height', 350)
                .call(chart);
            return chart;
        });



.. image:: ../_static/screenshot/cumulativeLineChart.png
