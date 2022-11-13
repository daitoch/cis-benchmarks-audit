#!/usr/bin/env python3

import setuptools

from cis_audit import __version__

setuptools.setup(
    name="cis-benchmarks-audit",
    version=__version__,
    author="Farhan Rauf",
    author_email="farhanch101@gmail.com",
    description="Check systems conformance to CIS Hardening benchmarks",
    packages=setuptools.find_packages(),
    py_modules=['cis_audit'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires='==3.6.*',
)
