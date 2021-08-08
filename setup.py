from setuptools import setup, find_packages
import sys, os

version = '0.2.1'

setup(name='robust_request',
      version=version,
      description="A more reliable http request.",
      long_description="""""",
      classifiers=[],
      keywords='http requests',
      author='Jesse Aldridge',
      author_email='JesseAldridge@gmail.com',
      url='https://github.com/JesseAldridge/robust_request',
      license='MIT',
      packages=['robust_request'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        "requests"
      ]
      )
