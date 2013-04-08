Python Wrapper for NVD3 - Create beautiful charts effortlessly
==============================================================

Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.


Installation
------------

Install, upgrade and uninstall python-nvd3.py with these commands::

  $ sudo pip install python-nvd3
  $ sudo pip install --upgrade python-nvd3
  $ sudo pip uninstall python-nvd3

Or if you don't have `pip`::

  $ sudo easy_install python-nvd3


Usage
-----

After installation use python-nvd3 as follow ::

    import nvd3

    #Open File to write the D3 Graph
    output_file = open('testnvd3.html', 'w')
    output_file.write(nvd3.template_header_nvd3)

    chart = nvd3.pieChart(name="pieChart", height=450, width=450)
    xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    ydata = [1, 2, 3, 4, 5, 3, 4]

    chart.add_serie(y=ydata, x=xdata)
    chart.buildhtml()

    output_file.write("\n\n<h2> pieChart Graph </h2>\n\n")
    output_file.write(chart.html)

    #close Html file
    output_file.close()



See our examples directory for more usage.


Documentation
-------------

Documentation is available on 'Read the Docs':
http://python-nvd3.readthedocs.org


License
-------

Python-nvd3 is licensed under MIT, see `MIT-LICENSE.txt`.
