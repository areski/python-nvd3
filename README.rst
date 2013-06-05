Python Wrapper for NVD3 - It's time for beautiful charts
========================================================

:Description: Python-nvd3 is a wrapper for NVD3 graph library
:nvd3: NVD3 http://nvd3.org/
:d3: Data-Driven Documents http://d3js.org/


NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.


.. image:: https://www.travis-ci.org/areski/python-nvd3.png?branch=master

|endorse|

.. |endorse| image:: https://api.coderwall.com/areski/endorsecount.png
    :target: https://coderwall.com/areski


Installation
------------

Install, upgrade and uninstall python-nvd3 with these commands::

    $ pip install python-nvd3
    $ pip install --upgrade python-nvd3
    $ pip uninstall python-nvd3


Usage
-----

After installation use python-nvd3 as follows ::

    from nvd3 import pieChart

    #Open File to write the D3 Graph
    output_file = open('test-nvd3.html', 'w')

    type = 'pieChart'
    chart = pieChart(name=type, color_category='category20c', height=450, width=450)
    chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

    #Create the keys
    xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    ydata = [3, 4, 0, 1, 5, 7, 3]

    #Add the serie
    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
    chart.buildhtml()
    output_file.write(chart.htmlcontent)

    #close Html file
    output_file.close()


See the file examples.py for more samples.


Live demo of NVD3
-----------------

See a live demo on jsfiddle : http://jsfiddle.net/areski/z4zuH/3/


Supported nvd3 charts
---------------------

Charts list:

.. image:: https://raw.github.com/areski/python-nvd3/master/docs/source/_static/screenshot/lineWithFocusChart.png

.. image:: https://raw.github.com/areski/python-nvd3/master/docs/source/_static/screenshot/lineChart.png

.. image:: https://raw.github.com/areski/python-nvd3/master/docs/source/_static/screenshot/multiBarChart.png

.. image:: https://raw.github.com/areski/python-nvd3/master/docs/source/_static/screenshot/pieChart.png

.. image:: https://raw.github.com/areski/python-nvd3/master/docs/source/_static/screenshot/stackedAreaChart.png

.. image:: https://raw.github.com/areski/python-nvd3/master/docs/source/_static/screenshot/multiBarHorizontalChart.png

.. image:: https://raw.github.com/areski/python-nvd3/master/docs/source/_static/screenshot/linePlusBarChart.png

.. image:: https://raw.github.com/areski/python-nvd3/master/docs/source/_static/screenshot/cumulativeLineChart.png

.. image:: https://raw.github.com/areski/python-nvd3/master/docs/source/_static/screenshot/discreteBarChart.png

.. image:: https://raw.github.com/areski/python-nvd3/master/docs/source/_static/screenshot/scatterChart.png


Documentation
-------------

Documentation is available on 'Read the Docs':
http://python-nvd3.readthedocs.org


Changelog
---------

Changelog summary : https://github.com/areski/python-nvd3/blob/master/CHANGELOG.rst


Like Django ?
-------------

We love Django too and we made available a django wrapper for nvd3:
https://github.com/areski/django-nvd3


License
-------

Python-nvd3 is licensed under MIT, see `MIT-LICENSE.txt`.
