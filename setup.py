from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    Return list of requirements
    '''
    requirement_list:List[str] = []
    try:
        with open('requirement.txt', 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                requirement = line.strip()
                
                #Ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("File not found!!")
    
    return requirement_list

setup(
    name = 'Network_Security',
    version = '0.0.1',
    author = "Pham Duy Anh",
    author_email='phamduyanh0816@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)