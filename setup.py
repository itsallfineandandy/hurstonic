from setuptools import setup, find_packages

setup(
    name = 'hurstonic',
    version = '0.1.0',
    description = 'A package to calculate the Hurst exponent',
    author = 'Andrew Haley',
    packages = find_packages(),
    install_requires = ['numpy',
                        'numba'
                        ],
    )