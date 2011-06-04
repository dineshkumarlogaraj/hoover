try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='Hoover',
      version='0.3',
      description="Library for logging to Loggly from within Python webapps",
      author="Mike Blume",
      author_email="mike@loggly.com",
      # fix this
      url="http://www.loggly.com",
      packages=['hoover'],
      install_requires=['httplib2'],
)
