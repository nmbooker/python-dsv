#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "dsv",
    version = "0.1.0",
    scripts = ['dsv2csv', 'dsvjoinline'],
    packages = find_packages(),
    author = "Nick Booker",
    description = "Delimiter separated values dialect for csv, and utilities",
    license = "GPLv2",
    url = "https://github.com/nmbooker/python-dsv",
)
