# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
import os

version = open('version.txt').read().strip()

setup(name='archive.theme',
      version=version,
      description="Archive - theme for plone",
      long_description=open("README.txt").read() + "\n" +
      open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='archive plone theme',
      author='Ghiță Bizău',
      author_email="ghita_bizau@yahoo.com",
      url='https://github.com/GhitaB/archive.theme.git',
      license='The Unlicense',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['archive', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
