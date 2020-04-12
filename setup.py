#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name ='oscar-stripe',
    version = '0.0.1',
    description=(
        " Stripe Card Payment and Adaptive"
        "Payments for django-oscar"),
    long_description=open('README.rst').read(),
    keywords="Payment, Stripe, Oscar",
    license=open('LICENSE').read(),
    platforms=['linux'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=1.8',
        'stripe>=1.49.0',
        'django-oscar>=1.4'
        ],
)
