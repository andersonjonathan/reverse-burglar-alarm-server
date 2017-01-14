#!/usr/bin/env python

from setuptools import setup

setup(
    name='Larm',
    version='0.1',
    description='Larm server',
    author='Jonathan Anderson',
    author_email='jonathan@jonathananderson.se',
    url='https://github.com/andersonjonathan',
    install_requires=[
        'Django==1.8.4'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
