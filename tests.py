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
from nvd3 import multiChart
from nvd3 import bulletChart
from nvd3.NVD3Chart import stab
from nvd3.translator import Function, AnonymousFunction, Assignment
import random
import unittest
import datetime
import time


class ChartTest(unittest.TestCase):

    def test_chartWithBadName(self):
        name = "Chart with spaces"
        chart = lineChart(name=name, date=True, height=350)
        chart.buildhtml()
        assert(" " not in chart.name)
        assert("spaces" in chart.name)

    def test_lineWithFocusChart(self):
        """Test Line With Focus Chart"""
        chart_name = "lineWithFocusChart"
        chart = lineWithFocusChart(name=chart_name, date=True, height=350)
        nb_element = 100
        xdata = list(range(nb_element))
        xdata = [1365026400000 + x * 100000 for x in xdata]
        ydata = [i + random.randint(-10, 10) for i in range(nb_element)]
        ydata2 = [x * 2 for x in ydata]
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_lineChart(self):
        """Test Line Chart"""
        chart_name = "lineChart"
        chart = lineChart(name=chart_name, date=True, height=350)
        nb_element = 100
        xdata = list(range(nb_element))
        xdata = [1365026400000 + x * 100000 for x in xdata]
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = [x * 2 for x in ydata]
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()
        # extra tests
        chart.buildcontent()
        chart.buildhtmlheader()

    def test_lineChart_tooltip(self):
        """Test Line Chart"""
        chart_name = "lineChart"
        chart = lineChart(name=chart_name, date=True, height=350)
        nb_element = 100
        xdata = list(range(nb_element))
        xdata = [1365026400000 + x * 100000 for x in xdata]
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = [x * 2 for x in ydata]

        kwargs1 = {'color': 'green'}
        kwargs2 = {'color': 'red'}

        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " random values"}}
        chart.add_serie(name="Random X-Axis", y=ydata, x=xdata, extra=extra_serie, **kwargs1)
        extra_serie = {"tooltip": {"y_start": "", "y_end": " double values"}}
        chart.add_serie(name="Double X-Axis", y=ydata2, x=xdata, extra=extra_serie, **kwargs2)

        chart.buildhtml()

        assert(".tickFormat(d3.format(',.02f'));" in chart.htmlcontent)

    def test_linePlusBarChart(self):
        """Test line Plus Bar Chart"""
        chart_name = "linePlusBarChart"
        chart = linePlusBarChart(name=chart_name, date=True, height=350)
        start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
        nb_element = 100
        xdata = list(range(nb_element))
        xdata = [start_time + x * 1000000000 for x in xdata]
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = [i + random.randint(1, 10) for i in reversed(list(range(nb_element)))]
        kwargs = {}
        kwargs['bar'] = True
        chart.add_serie(y=ydata, x=xdata, **kwargs)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_stackedAreaChart(self):
        """Test Stacked Area Chart"""
        chart_name = "stackedAreaChart"
        chart = stackedAreaChart(name=chart_name, height=400)
        nb_element = 100
        xdata = list(range(nb_element))
        xdata = [100 + x for x in xdata]
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = [x * 2 for x in ydata]
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_MultiBarChart(self):
        """Test Multi Bar Chart"""
        chart_name = "MultiBarChart"
        chart = multiBarChart(name=chart_name, height=400)
        nb_element = 10
        xdata = list(range(nb_element))
        ydata = [random.randint(1, 10) for i in range(nb_element)]
        extra = {"type": "bar", "yaxis": 1}
        chart.add_serie(y=ydata, x=xdata, extra=extra)
        chart.buildhtml()

    def test_multiChart(self):
        """Test Multi (line plus bar) Chart"""
        chart_name = "multiChart"
        chart = multiChart(
            name=chart_name, x_is_date=False, x_axis_format="AM_PM",
            no_data_message='custom message shows when there is no data',
            xAxis_staggerLabel=True
        )

        xdata = [1,2,3,4,5,6]
        ydata = [115.5,160.5,108,145.5,84,70.5]
        ydata2 = [48624,42944,43439,24194,38440,31651]
        kwargs1 = {'color': 'brown'}
        kwargs2 = {'color': '#bada55'}
        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}
        chart.add_serie(y=ydata, x=xdata, type='line', yaxis=1, name='visits', extra=extra_serie, **kwargs1)
        extra_serie = {"tooltip": {"y_start": "", "y_end": " at this point"}}
        chart.add_serie(y=ydata2, x=xdata, type='bar', yaxis=2,name='spend', extra=extra_serie, **kwargs2)
        chart.buildhtml()

        assert("chart.noData('custom message shows when there is no data')" in chart.htmlcontent)
        assert("function get_am_pm" in chart.htmlcontent)


    def test_multiBarHorizontalChart(self):
        """Test multi Bar Horizontal Chart"""
        chart_name = "multiBarHorizontalChart"
        chart = multiBarHorizontalChart(name=chart_name, height=350)
        nb_element = 10
        xdata = list(range(nb_element))
        ydata = [random.randint(-10, 10) for i in range(nb_element)]
        ydata2 = [x * 2 for x in ydata]
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_cumulativeLineChart(self):
        """Test Cumulative Line Chart"""
        chart_name = "cumulativeLineChart"
        chart = cumulativeLineChart(name=chart_name, height=400)
        start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
        nb_element = 100
        xdata = list(range(nb_element))
        xdata = [start_time + x * 1000000000 for x in xdata]
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = [x * 2 for x in ydata]
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=ydata2, x=xdata)
        chart.buildhtml()

    def test_scatterChart(self):
        """Test Scatter Chart"""
        chart_name = "scatterChart"
        chart = scatterChart(name=chart_name, date=True, height=350)
        nb_element = 100
        xdata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata = [i * random.randint(1, 10) for i in range(nb_element)]
        ydata2 = [x * 2 for x in ydata]
        ydata3 = [x * 5 for x in ydata]

        kwargs1 = {'shape': 'circle', 'size': '1'}
        kwargs2 = {'shape': 'cross', 'size': '10'}
        kwargs3 = {'shape': 'triangle-up', 'size': '100'}
        chart.add_serie(y=ydata, x=xdata, **kwargs1)
        chart.add_serie(y=ydata2, x=xdata, **kwargs2)
        chart.add_serie(y=ydata3, x=xdata, **kwargs3)
        chart.buildhtml()

    def test_discreteBarChart(self):
        """Test discrete Bar Chart"""
        chart_name = "discreteBarChart"
        chart = discreteBarChart(name=chart_name, height=350)
        xdata = ["A", "B", "C", "D", "E", "F", "G"]
        ydata = [3, 12, -10, 5, 35, -7, 2]

        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

        # We don't modify the xAxis, so make sure that it's not invoked.
        assert("chart.xAxis" in chart.htmlcontent)
        assert("var chart = nv.models.discreteBarChart();" in chart.htmlcontent)

    def test_pieChart(self):
        """Test Pie Chart"""
        chart_name = "pieChart"
        chart = pieChart(name=chart_name, color_category='category20c', height=400, width=400)
        xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
        color_list = ['orange', 'yellow', '#C5E946', '#95b43f', 'red', '#FF2259', '#F6A641']
        extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}, "color_list": color_list}
        ydata = [3, 4, 0, 1, 5, 7, 3]
        chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
        chart.buildhtml()

        assert("tooltip_str =" in chart.htmlcontent)

    def test_donutPieChart(self):
        """Test Donut Pie Chart"""
        chart_name = "pieChart"
        chart = pieChart(name=chart_name, height=400, width=400, donut=True, donutRatio=0.2)
        xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
        ydata = [3, 4, 0, 1, 5, 7, 3]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    def test_can_create_bulletChart(self):
        chart_name = 'bulletChart'
        chart = bulletChart(name=chart_name, height=100, width=500)
        title = 'Revenue',
        subtitle = 'US$, in thousands'
        ranges = [150, 225, 300]
        measures = [220, 270]
        markers = [250]
        chart.add_serie(
            title=title,
            subtitle=subtitle,
            ranges=ranges,
            measures=measures,
            markers=markers)
        chart.buildhtml()

    def test_bulletChart_htmlcontent_correct(self):
        chart_name = 'bulletChart'
        chart = bulletChart(name=chart_name, height=100, width=500)
        title = 'Revenue',
        subtitle = 'USD, in mill'
        ranges = [100, 250, 300]
        measures = [220, 280]
        markers = [260]
        chart.add_serie(
            title=title,
            subtitle=subtitle,
            ranges=ranges,
            measures=measures,
            markers=markers)
        chart.buildhtml()
        assert 'data_bulletchart' in chart.htmlcontent
        assert '"title": ["Revenue"]'  in chart.htmlcontent
        assert '"ranges": [100, 250, 300]' in chart.htmlcontent
        assert 'nv.models.bulletChart();' in chart.htmlcontent

    def test_bulletChart_marker_optional(self):
        chart_name = 'bulletChart'
        chart = bulletChart(name=chart_name, height=100, width=500)
        title = 'Revenue',
        subtitle = 'USD, in mill'
        ranges = [100, 250, 300]
        measures = [220, 280]
        chart.add_serie(
            title=title,
            subtitle=subtitle,
            ranges=ranges,
            measures=measures
            )
        chart.buildhtml()
        assert 'data_bulletchart' in chart.htmlcontent
        assert 'marker' not in chart.htmlcontent


    def test_charts_with_extras(self):
        #  extras="d3.selectAll('#mygraphname text').style('opacity', 0.5)"
        chart_name = 'bulletChart'
        bullet_chart = bulletChart(name=chart_name, height=100, width=500, extras="d3.selectAll('#mygraphname text').style('opacity', 0.5)")
        bullet_chart.buildhtml()
        assert 'data_bulletchart' in bullet_chart.htmlcontent
        assert "d3.selectAll('#mygraphname text').style('opacity', 0.5)" in bullet_chart.htmlcontent

        chart_name = "pieChart"
        pie_chart = pieChart(name=chart_name, height=400, width=400, donut=True, donutRatio=0.2, extras="alert('Example of extra not even related to d3!')")
        pie_chart.buildhtml()
        assert "alert('Example of extra not even related to d3!')" in pie_chart.htmlcontent

        chart_name = "linePlusBarChart"
        line_plus_bar_chart = linePlusBarChart(name=chart_name, date=True, height=350, extras="d3.selectAll('#mygraphname text').style('fill', 'red')")
        line_plus_bar_chart.buildhtml()
        assert "d3.selectAll('#mygraphname text').style('fill', 'red')" in line_plus_bar_chart.htmlcontent

class FuncTest(unittest.TestCase):

    def test_stab(self):
        self.assertEqual("    ", stab(1))


class TranslatorTest(unittest.TestCase):

    def test_pieChart(self):
        func = Function('nv').addGraph(
            AnonymousFunction('', Assignment(
                'chart',
                Function('nv').models.pieChart().x(
                    AnonymousFunction('d', 'return d.label;')
                ).y(AnonymousFunction('d', 'return d.value;')
                    ).showLabels('true')
                )
            )
        )
        self.assertEqual(str(func),
                         'nv.addGraph(function() { var chart = '
                         'nv.models.pieChart().x(function(d) { return d.label; '
                         '}).y(function(d) { return d.value; }).showLabels(true); })')


if __name__ == '__main__':
    unittest.main()

# Usage
# python tests.py -v
