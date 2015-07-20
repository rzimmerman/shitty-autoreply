# -*- coding: utf-8 -*-
from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

version = '1.0'


setup(name='shitty-autoreply',
      version=version,
      description="Irritate people by getting their names wrong",
      long_description=README,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: Plugins',
          'Framework :: Paste',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
      ],
      keywords='',
      author='Rob Zimmerman',
      author_email='rmzimmerman@gmail.com',
      url='https://github.com/rzimmerman/shitty-autoreply',
      license='MIT License',
      packages=['shitty_autoreply'],
      include_package_data=True,
      )
