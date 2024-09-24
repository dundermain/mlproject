from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

'''
The -e . in a requirements.txt file is used to install a package in "editable" mode. 

Here's what it does:
1. -e stands for "editable." When you install a package in editable mode, any changes made to the source code of the package are immediately reflected without needing to reinstall the package.
2. . refers to the current directory. It assumes that the package is located in the current directory and contains a setup.py file that defines how to install the package.

'''

def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.1.0",
    author="Sachin",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)