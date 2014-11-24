#!/usr/bin/env python

from setuptools import setup

setup(name='python_hadoop',
      version='0.1.7',
      description='Python Hadoop I/O Utilities',
      license="Apache Software License 2.0 (ASF)",
      author='Matteo Bertozzi',
      author_email='theo.bertozzi@gmail.com',
      url='http://hadoop.apache.org',
      packages=[
        "python_hadoop",
        "python_hadoop.hadoop",
        'python_hadoop.hadoop.util',
        'python_hadoop.hadoop.io',
        'python_hadoop.hadoop.io.compress',
        "python_hadoop.hadoop.pydoop"
      ],
      extras_require = {
        'pydoop': ['pydoop>=0.9.1']
        }
     )

