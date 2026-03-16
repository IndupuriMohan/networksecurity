'''
<<<<<<< HEAD
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
=======
The setup.py file is an essential part of packing and distributing python projects it used by setuptools
distributing python projects it used by setuptoolss
(or distutils in older python versions) to define the configuration
of your project suchas it metadata dependencies and more
>>>>>>> 10064a7e02c6a3da0d08880cffa0b92588a4e450
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
<<<<<<< HEAD
    """
    Thiss function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Krish Naik",
    author_email="krishnaik06@gmail.com",
=======
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
>>>>>>> 10064a7e02c6a3da0d08880cffa0b92588a4e450
    packages=find_packages(),
    install_requires=get_requirements()
)