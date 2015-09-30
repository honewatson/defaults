#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'toolz>=0.7.4'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='defaults',
    version='0.1.0',
    description="A simple package to create data structures with defaults",
    long_description=readme + '\n\n' + history,
    author="Hone Watson",
    author_email='comments@hone.be',
    url='https://github.com/honewatson/defaults',
    packages=[
        'defaults',
    ],
    package_dir={'defaults':
                 'defaults'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='defaults,data structures,objects',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
