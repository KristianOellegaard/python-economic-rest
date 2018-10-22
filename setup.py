import os
from setuptools import setup
from economic import version

setup(
    name = "python-economic-rest",
    version = version,
    author = "Kristian Oellegaard",
    author_email = "kristian@kristian.io",
    description = "Easy to use and dynamic python interface to the experimental e-conomic REST api",
    license = "BSD",
    keywords = "economic e-conomic accounting bookkeeping",
    url = "https://github.com/KristianOellegaard/python-economic-rest",
    packages=['economic'],
    classifiers=[
    ],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe = False,
)
