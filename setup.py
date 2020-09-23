
from setuptools import setup, find_packages

NAME = "gcandle-client"
DESCRIPTION = "gcandle-client: all about my strategies"
KEYWORDS = ["gcandle-client", "quant", "finance", "Backtest", 'trade']
VERSION='1.0'
LICENSE = "MIT"
required = ['gcandle>=0.0.1']

setup(
    name=NAME,
    description=DESCRIPTION,
    version=VERSION,
    install_requires=required,
    license=LICENSE,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
)
