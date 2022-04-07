"""Fornax setup file."""

from pathlib import Path
from typing import List

from setuptools import find_packages, setup

from inventory.version import version

BASE_PROJECT_DIR = Path(__file__).absolute().parent


def get_requirements() -> List[str]:
    """Load requirements.

    :return: list of requirements
    :rtype: List[str]
    """
    requirements_path = BASE_PROJECT_DIR.joinpath("requirements.txt")
    with open(requirements_path, "r") as stream:
        return [pkg.strip("\n") for pkg in stream if pkg != ""]


setup(
    name="inventory",
    version=version,
    description="",
    author="lwencel-priv",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=get_requirements(),
    url="https://github.com/lwencel-priv/inventory",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha" "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "console_scripts": [
            "inventory=inventory.main:main",
        ]
    },
)
