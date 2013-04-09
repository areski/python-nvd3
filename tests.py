#!/usr/bin/python
# -*- coding: utf-8 -*-
import nvd3
import unittest


class ChartTest(unittest.TestCase):

    def test_pieChart(self):
        """Test pie chart"""

        type = "pieChart"
        chart = nvd3.pieChart(name=type, height=400, width=400)
        xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
        ydata = [3, 4, 0, 1, 5, 7, 3]

        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()


if __name__ == '__main__':
    unittest.main()

# > python tests.py -v