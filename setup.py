#! /usr/bin/env python
# coding=utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='python-nvd3',
    version='0.14.2',
    description="Python NVD3 - Chart Library for d3.js",
    long_description=readme + '\n\n' + history,
    keywords='plot, graph, nvd3, d3',
    author='Belaid Arezqui',
    author_email='areski@gmail.com',
    url='http://github.com/areski/python-nvd3',
    license="MIT",
    py_modules=['nvd3'],
    namespace_packages=[],
    test_suite='tests',
    packages=[
        'nvd3',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python-slugify>=1.2.5',
        'Jinja2>=2.8'
        # -*- Extra requirements: -*-
    ],
    entry_points={
        'console_scripts': [
            'nvd3 = nvd3.NVD3Chart:_main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
