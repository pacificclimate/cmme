import os
from setuptools import setup, find_packages

__version__ = (0, 0, 1)

setup(
    name = "climdir",
    version ='.'.join(str(d) for d in __version__),
    author = "Basil Veerman",
    author_email = "bveerman@uvic.ca",
    description = ("Utility for generating and parsing CMIP5 file paths"),
    url = "http://www.pacificclimate.org/",
    packages = find_packages('.'),
    extras_require = {
        'netCDF': ['netCDF4'],
    },
    )
