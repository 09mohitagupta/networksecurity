# setup.py: This script allows you to package your networksecurity folder. 
# It means you can install your own project as a library using pip install -e.
'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''
from setuptools import find_packages,setup
from typing import List

'''
find- packages : scans through all the folders and where ever it finds init.py file,
 it will consider that  particular folder as a package. for ex : cloud has init.py..cloud will 
now considered as package

set-up : responsible for providing all the info about the project
'''
def get_requirements()->List[str]:
    '''
    This  function will return list of requirements
    '''
    requirement_1st:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
        # Read lines from file
            lines = file.readlines()
        for line in lines:
            requirement = line.strip()
            # Ignore empty lines amd -e .
            if requirement and requirement != '-e .':
                requirement_1st.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_1st

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Mohita Gupta",
    author_email = "09mohitagupta@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)