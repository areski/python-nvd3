#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

__version__ = '0.11.0'  # edit also docs/source/conf.py
__all__ = ['lineChart', 'pieChart', 'lineWithFocusChart',
           'stackedAreaChart', 'multiBarHorizontalChart',
           'linePlusBarChart', 'cumulativeLineChart',
           'scatterChart', 'discreteBarChart', 'multiBarChart',
           'linePlusBarWithFocusChart']


from .lineChart import lineChart
from .pieChart import pieChart
from .lineWithFocusChart import lineWithFocusChart
from .stackedAreaChart import stackedAreaChart
from .multiBarHorizontalChart import multiBarHorizontalChart
from .linePlusBarChart import linePlusBarChart
from .cumulativeLineChart import cumulativeLineChart
from .scatterChart import scatterChart
from .discreteBarChart import discreteBarChart
from .multiBarChart import multiBarChart
from .linePlusBarWithFocusChart import linePlusBarWithFocusChart


def initialize_notebook(local=False):
    """Initialize the IPython notebook display elements"""
    try:
        from IPython.core.display import display, Javascript, HTML
    except ImportError:
        print('IPython Notebook could not be loaded.')
    
    #TODO: Keep local?
    d3_js_url = 'http://d3js.org/d3.v3.min.js'
    nvd3_js_url = 'http://nvd3.org/nv.d3.js'
    nvd3_css_url = 'http://nvd3.org/src/nv.d3.css'
    # in IPython master a nbextensions folder exists in 
    # the IPython profile path. So js can be load from there
    if local:
        d3_js_url = './nbextensions/d3/d3.v3.min.js'
        nvd3_js_url = './nbextensions/nvd3/nv.d3.min.js'
        nvd3_css_url = './nbextensions/nvd3/src/nv.d3.css'


    display(Javascript('''$.getScript("%s", function() {
        $.getScript("%s", function() {
            $([IPython.events]).trigger("vega_loaded.vincent");
        })
    });''' % (d3_js_url, nvd3_js_url)))

    display(HTML('''<link media="all" href="%s" type="text/css" 
                rel="stylesheet"/>''' %(nvd3_css_url)))





