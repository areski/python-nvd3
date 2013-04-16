.. _scatterChart-model:

:class:`scatterChart`
---------------------

A pie chart (or a circle graph) is a circular chart divided into sectors, illustrating numerical proportion. In chart, the arc length of each sector is proportional to the quantity it represents.

python-example ::

        from nvd3 import scatterChart
        chart = scatterChart(name='scatterChart', height=400, width=400)
        xdata = [3, 4, 0, -3, 5, 7]
        ydata = [-1, 2, 3, 3, 15, 2]
        ydata = [1, -2, 4, 7, -5, 3]

        kwargs1 = {'shape': 'circle'}
        kwargs2 = {'shape': 'cross'}
        chart.add_serie(y=ydata, x=xdata, **kwargs1)
        chart.add_serie(y=ydata, x=xdata, **kwargs2)
        chart.buildhtml()

js example::

        data = [{ key: "series 1",
                  values: [
                    {
                      "x": 2,
                      "y": 10,
                      "shape": "circle"
                    },
                    {
                      "x": -2,
                      "y" : 0,
                      "shape": "circle"
                    },
                    {
                      "x": 5,
                      "y" : -3,
                      "shape": "circle"
                    },
                  ]
                },
                { key: "series 2",
                  values: [
                    {
                      "x": 4,
                      "y": 10,
                      "shape": "cross"
                    },
                    {
                      "x": 4,
                      "y" : 0,
                      "shape": "cross"
                    },
                    {
                      "x": 3,
                      "y" : -3,
                      "shape": "cross"
                    },
                  ]
                }]

        nv.addGraph(function() {
            var chart = nv.models.scatterChart()
                .showLabels(true);

            chart.showDistX(true);
            chart.showDistY(true);

            d3.select("#div_id")
                .datum(data)
                .transition()
                .duration(1200)
                .call(chart);

            return chart;
        });



.. image:: https://raw.github.com/areski/python-nvd3/master/screenshot/scatterChart.png
