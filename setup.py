#!/usr/bin/env python3
from setuptools import setup, find_packages
setup(
    name="SCPSycer",
    version="0.1",
    packages=find_packages(),
    install_requires=['paramiko', 'scp', 'PyYAML', 'colorama'],

    # metadata to display on PyPI
    author="Frederic98",
    description="SCP syncer",
    keywords="scp sync syncer",
    url="https://github.com/Frederic98/SCP-Syncer"
)
