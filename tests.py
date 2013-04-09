#!/usr/bin/python
# -*- coding: utf-8 -*-
import nvd3
import random
import unittest


class ChartTest(unittest.TestCase):

    def test_lineWithFocusChart(self):
        """Test Line With Focus Chart"""
        type = "lineWithFocusChart"
        chart = nvd3.lineWithFocusChart(name=type, date=True, height=350)
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
        chart = nvd3.lineChart(name=type, date=True, height=350)
        nb_element = 100
        xdata = range(nb_element)
        xdata = map(lambda x: 1365026400000 + x * 100000, xdata)
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)

        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_stackedAreaChart(self):
        """Test Stacked Area Chart"""
        type = "stackedAreaChart"
        chart = nvd3.stackedAreaChart(name=type, height=400)
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
        chart = nvd3.multiBarChart(name=type, height=400)
        nb_element = 10
        xdata = range(nb_element)
        ydata = [random.randint(1, 10) for i in range(nb_element)]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    def test_pieChart(self):
        """Test Pie Chart"""
        type = "pieChart"
        chart = nvd3.pieChart(name=type, height=400, width=400)
        xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
        ydata = [3, 4, 0, 1, 5, 7, 3]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()


if __name__ == '__main__':
    unittest.main()

# > python tests.py -v