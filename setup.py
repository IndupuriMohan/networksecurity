'''
The setup.py file is an essential part of packing and distributing python projects it used by setuptools
distributing python projects it used by setuptoolss
(or distutils in older python versions) to define the configuration
of your project suchas it metadata dependencies and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements 
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r')  as file:
            #Read lines from the file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirments.txt file not found")
    return requirement_lst
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Mohan Vamsi",
    author_email="mohanindupuri2003@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)