"""The python wrapper for IQ Option API package setup."""

from setuptools import setup, find_packages
from iqbroker.version_control import api_version

setup(
    name="iqbroker",
    version=api_version,
    packages=find_packages(),
    install_requires=["requests", "websocket-client"],
    include_package_data=True,
    description="Best IQ Option API for python",
    long_description="Best IQ Option API for python",
    url="https://github.com/zagmi/iqbroker",
    author="Santiago Ramirez",
    zip_safe=False,
)
