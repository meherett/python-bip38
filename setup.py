#!/usr/bin/env python3

from setuptools import (
    setup, find_packages
)

# Project URL's
project_urls: dict = {
    "Tracker": "https://github.com/meherett/python-bip38/issues",
    "Documentation": "https://bip38.readthedocs.io"
}

# README.md
with open("README.md", "r", encoding="utf-8") as readme:
    long_description: str = readme.read()

# requirements.txt
with open("requirements.txt", "r") as _requirements:
    requirements: list = list(map(str.strip, _requirements.read().split("\n")))

setup(
    name="bip38",
    version="v0.2.1",
    description="Python library for implementation of Bitcoin Improvement Proposal - 0038 / BIP38 protocol.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Meheret Tesfaye Batu",
    author_email="meherett.batu@gmail.com",
    url="https://github.com/meherett/python-bip38",
    project_urls=project_urls,
    keywords=[
        "bip38", "bitcoin", "private-key", "pure-python", "encrypt", "decrypt", "passphrase", "wif", "bip-0038"
    ],
    python_requires=">=3.9,<4",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        "tests": [
            "pytest>=7.4.0,<8",
            "pytest-cov>=4.1.0,<5",
            "pyyaml>=6.0.1,<7"
        ],
        "docs": [
            "sphinx>=7.2.5,<8",
            "sphinx-rtd-theme==1.3.0"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
