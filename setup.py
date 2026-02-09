from setuptools import setup, find_packages

import src

setup(
    name="dab_project",
    version="0.0.1",
    description="",
    author="",
    packages=find_packages(where="./src"),
    package_dir={"":"./src"},
    install_requires=["setuptools"]
)
