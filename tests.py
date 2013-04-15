#!/usr/bin/python
# -*- coding: utf-8 -*-
from nvd3 import lineChart
from nvd3 import lineWithFocusChart
from nvd3 import stackedAreaChart
from nvd3 import multiBarHorizontalChart
from nvd3 import linePlusBarChart
from nvd3 import cumulativeLineChart
from nvd3 import scatterChart
from nvd3 import discreteBarChart
from nvd3 import pieChart
from nvd3 import multiBarChart

import random
import unittest
import datetime
import time


class ChartTest(unittest.TestCase):

    def test_lineWithFocusChart(self):
        """Test Line With Focus Chart"""
        type = "lineWithFocusChart"
        chart = lineWithFocusChart(name=type, date=True, height=350)
        nb_element = 100
        xdata = range(nb_element)
        xdata = map(lambda x: 1365026400000 + x * 100000, xdata)
        ydata = [i + random.randint(-10, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_lineChart(self):
        """Test Line Chart"""
        type = "lineChart"
        chart = lineChart(name=type, date=True, height=350)
        nb_element = 100
        xdata = range(nb_element)
        xdata = map(lambda x: 1365026400000 + x * 100000, xdata)
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)

        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_linePlusBarChart(self):
        """Test line Plus Bar Chart"""
        type = "linePlusBarChart"
        chart = linePlusBarChart(name=type, date=True, height=350)
        start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
        nb_element = 100
        xdata = range(nb_element)
        xdata = map(lambda x: start_time + x * 1000000000, xdata)
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = [i + random.randint(1, 10) for i in reversed(range(nb_element))]
        kwargs = {}
        kwargs['bar'] = True
        chart.add_serie(y=ydata, x=xdata, **kwargs)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_stackedAreaChart(self):
        """Test Stacked Area Chart"""
        type = "stackedAreaChart"
        chart = stackedAreaChart(name=type, height=400)
        nb_element = 100
        xdata = range(nb_element)
        xdata = map(lambda x: 100 + x, xdata)
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_MultiBarChart(self):
        """Test Multi Bar Chart"""
        type = "MultiBarChart"
        chart = multiBarChart(name=type, height=400)
        nb_element = 10
        xdata = range(nb_element)
        ydata = [random.randint(1, 10) for i in range(nb_element)]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    def test_multiBarHorizontalChart(self):
        """Test multi Bar Horizontal Chart"""
        type = "multiBarHorizontalChart"
        chart = multiBarHorizontalChart(name=type, height=350)
        nb_element = 10
        xdata = range(nb_element)
        ydata = [random.randint(-10, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_cumulativeLineChart(self):
        """Test Cumulative Line Chart"""
        type = "cumulativeLineChart"
        chart = cumulativeLineChart(name=type, height=400)
        start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
        nb_element = 100
        xdata = range(nb_element)
        xdata = map(lambda x: start_time + x * 1000000000, xdata)
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_scatterChart(self):
        """Test Scatter Chart"""
        type = "scatterChart"
        chart = scatterChart(name=type, date=True, height=350)
        nb_element = 100
        xdata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata = [i * random.randint(1, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)
        ydata3 = map(lambda x: x * 5, ydata)

        kwargs1 = {'shape': 'circle'}
        kwargs2 = {'shape': 'cross'}
        kwargs3 = {'shape': 'triangle-up'}
        chart.add_serie(y=ydata, x=xdata, **kwargs1)
        chart.add_serie(y=ydata2, x=xdata, **kwargs2)
        chart.add_serie(y=ydata3, x=xdata, **kwargs3)
        chart.buildhtml()

    def test_discreteBarChart(self):
        """Test discrete Bar Chart"""
        type = "discreteBarChart"
        chart = discreteBarChart(name=type, date=True, height=350)
        xdata = ["A", "B", "C", "D", "E", "F", "G"]
        ydata = [3, 12, -10, 5, 35, -7, 2]

        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    def test_pieChart(self):
        """Test Pie Chart"""
        type = "pieChart"
        chart = pieChart(name=type, height=400, width=400)
        xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
        ydata = [3, 4, 0, 1, 5, 7, 3]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()


if __name__ == '__main__':
    unittest.main()

# > python tests.py -v