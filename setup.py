#! /usr/bin/env python

from setuptools import setup


def get_version(filename="nvd3/__init__.py", varname="__version__"):
    glb = {}
    with open(filename) as fp:
        for line in fp:
            if varname in line:
                exec(line, glb)
                break
    return glb[varname]


def readfile(filename):
    with open(filename) as fp:
        return fp.read()


readme = readfile('README.rst')
history = readfile('CHANGELOG.rst').replace('.. :changelog:', '')

setup(
    name='python-nvd3',
    version=get_version(),
    description="Python NVD3 - Chart Library for d3.js",
    long_description=readme + '\n\n' + history,
    keywords='plot, graph, nvd3, d3',
    author='Belaid Arezqui',
    author_email='areski@gmail.com',
    url='http://github.com/areski/python-nvd3',
    license="MIT",
    test_suite='tests',
    packages=['nvd3'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python-slugify==1.1.4',
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
