.. labibi documentation master file, created by
   sphinx-quickstart on Sun Nov  4 10:10:29 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the labibi demo site!
================================

.. toctree::
   :maxdepth: 2

Labibi is a base package to use for documentation and Web sites for
other projects of mine.

For now, I've made it fairly easy to post sites to `ReadTheDocs
<http://readthedocs.org>`__ that enable Google Analytics, Disqus commenting,
and easy source file editing.  You can check it out at the `labibi demo
site <http://labibi.readthedocs.org/en/latest/>`__.

This is directly based off of Mikko Ohtamaa's excellent work on `the
Plone documentation
<http://opensourcehacker.com/2012/01/08/readthedocs-org-github-edit-backlink-and-short-history-of-plone-documentation/>`__.

A brief HOWTO do this for your own ReadTheDocs site:

  0. `Get started with ReadTheDocs <https://docs.readthedocs.org/en/latest/getting_started.html>`__.

  1. Create a _static/ directory and put `labibi.css <https://raw.github.com/ctb/labibi/master/_static/labibi.css>`__ and `labibi.js <https://raw.github.com/ctb/labibi/master/_static/labibi.js>`__ in it.

  2. Put "html_style = 'labibi.css'" in your conf.py

  3. Create a _templates/ directory and put `page.html <https://raw.github.com/ctb/labibi/master/_templates/page.html>`__ in there.

  4. Edit 'page.html' to set your google analytics, disqus, and github info.

For now, you can't disable the editing functionality, but if you
delete the google_analytics and disqus_shortname it should disable
that functionality on your site.

The labibi source code is `here <https://github.com/ctb/labibi>`__ for
your checking-out pleasure.

I've put up a short blog post `here <http://ivory.idyll.org/blog/rtd-comments-and-editing.html>`__.

--titus

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

    <link href="_static/nv.d3.css" rel="stylesheet" />
    <script src="_static/d3.min.js"></script>
    <script src="_static/nv.d3.min.js"></script>
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

