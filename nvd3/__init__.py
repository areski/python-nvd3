#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3

Part of this code is inspired from goulib
https://github.com/goulu/Goulib/blob/master/Goulib/nvd3.py

This project aims to be reusuable with less dependencies and with the aim
to power more library using it. For instance Django-Nvd3.

General aims :
- keep a separation between the templating and the output generation
- don't tie with too many dependencies
- easy to use
- clean APIs
- Documented
- Clean code / PEP8
"""

__version__ = '0.2.1'


from lineChart import lineChart
from pieChart import pieChart
from lineWithFocusChart import lineWithFocusChart
from stackedAreaChart import stackedAreaChart
from multiBarHorizontalChart import multiBarHorizontalChart
from linePlusBarChart import linePlusBarChart
from cumulativeLineChart import cumulativeLineChart
from scatterChart import scatterChart
from discreteBarChart import discreteBarChart
from multiBarChart import multiBarChart


class lineChart(lineChart):
    pass


class pieChart(pieChart):
    pass


class lineWithFocusChart(lineWithFocusChart):
    pass


class stackedAreaChart(stackedAreaChart):
    pass


class multiBarHorizontalChart(multiBarHorizontalChart):
    pass


class linePlusBarChart(linePlusBarChart):
    pass


class cumulativeLineChart(cumulativeLineChart):
    pass


class scatterChart(scatterChart):
    pass


class discreteBarChart(discreteBarChart):
    pass


class multiBarChart(multiBarChart):
    pass
