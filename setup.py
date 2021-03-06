#!/usr/bin/env python

from setuptools import setup

setup(name='python_hadoop',
      version='0.1.9',
      description='Python Hadoop I/O Utilities',
      license="Apache Software License 2.0 (ASF)",
      author='Matteo Bertozzi',
      author_email='theo.bertozzi@gmail.com',
      url='http://hadoop.apache.org',
      packages=[
        "hadoop",
        'hadoop.util',
        'hadoop.io',
        'hadoop.io.compress',
        "hadoop.pydoop"
      ],
      extras_require = {
        'pydoop': ['pydoop>=0.9.1']
        }
     )

