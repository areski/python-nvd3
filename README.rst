Python Wrapper for NVD3 - Create beautiful charts effortlessly
==============================================================

:Description: Python-nvd3 is a wrapper for NVD3 graph library
:nvd3: NVD3 http://nvd3.org/
:d3: Data-Driven Documents http://d3js.org/


NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.


.. image:: https://www.travis-ci.org/areski/python-nvd3.png?branch=master


Installation
------------

Install, upgrade and uninstall python-nvd3.py with these commands::

  #Install
  $ sudo pip install python-nvd3

  #Upgrade
  $ sudo pip install --upgrade python-nvd3

  #Uninstall
  $ sudo pip uninstall python-nvd3


Or if you don't have `pip`, use easy_install to install python-nvd3::

  $ sudo easy_install python-nvd3


Usage
-----

After installation use python-nvd3 as follows ::

    from nvd3 import pieChart

    #Open File to write the D3 Graph
    output_file = open('test-nvd3.html', 'w')

    type = 'pieChart'
    chart = pieChart(name=type, height=450, width=450)
    chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

    #Create the keys
    xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    ydata = [3, 4, 0, 1, 5, 7, 3]

    #Add the serie
    chart.add_serie(y=ydata, x=xdata)
    chart.buildhtml()
    output_file.write(chart.htmlcontent)

    #close Html file
    output_file.close()


See the file examples.py for more samples.


Demo
----

See a live demo on jsfiddle : http://jsfiddle.net/4KuSx/


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


License
-------

Python-nvd3 is licensed under MIT, see `MIT-LICENSE.txt`.
