.. _linePlusBarChart-model:

:class:`linePlusBarChart`
-------------------------



python-example ::

        from nvd3 import linePlusBarChart
        chart = linePlusBarChart(name='linePlusBarChart', date=True)
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
               "bar": "true",
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
            var chart = nv.models.linePlusBarChart();

            chart.xAxis
                .tickFormat(function(d) { return d3.time.format('%d %b %Y')(new Date(d)) });
            chart.y1Axis
                .tickFormat(d3.format(',f'));
            chart.y2Axis
                .tickFormat(function(d) { return '$' + d3.format(',f')(d) });

            d3.select('#linePlusBarChart svg')
                .datum(data_linePlusBarChart)
                .transition().duration(500)
                .attr('height', 350)
                .call(chart);
            return chart;
        });



.. image:: ../_static/screenshot/linePlusBarChart.png
