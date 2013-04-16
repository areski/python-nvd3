.. _pieChart-model:

:class:`pieChart`
-----------------

A pie chart (or a circle graph) is a circular chart divided into sectors, illustrating numerical proportion. In chart, the arc length of each sector is proportional to the quantity it represents.

python-example ::

        from nvd3 import pieChart
        chart = pieChart(name='pieChart', height=400, width=400)
        xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
        ydata = [3, 4, 0, 1, 5, 7, 3]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

js example::

        data = [{ key: "Cumulative Return",
                  values: [
                    {
                      "label": "One",
                      "value" : 29.765957771107
                    },
                    {
                      "label": "Two",
                      "value" : 0
                    },
                    {
                      "label": "Three",
                      "value" : 32.807804682612
                    },
                  ]
                }]

        nv.addGraph(function() {
          var chart = nv.models.pieChart()
              .x(function(d) { return d.label })
              .y(function(d) { return d.value })
              .showLabels(true);

            d3.select("#div_id")
                .datum(data)
                .transition()
                .duration(1200)
                .call(chart);

          return chart;
        });



.. image:: https://raw.github.com/areski/python-nvd3/master/screenshot/pieChart.png
