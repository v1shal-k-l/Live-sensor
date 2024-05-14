## to get info about packages 
from setuptools import find_packages ,setup
from typing import list


def get_requirements()->list[str]:

    requirements_list:list[str]=[]

    return requirements_list
setup(
    name="Sensor",
    version="0.0.1",
    author="Vishal",
    author_email="vishalkumarlal44@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)