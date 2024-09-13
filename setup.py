# by building this we can treat and distribute this project as packages.
# 'setup' is a function containing basic info of project .
# 'find_packages' is function which automatically finds all the pacakes defined in the project.

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'

#setting the requirements.txt file path and reading every  line and install all packages like numpy, pandas etc 
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements: #ignoreing the -e. in requiremnts because its a package 
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='Fault detection',
    version='0.0.1',
    author='Suhas',
    author_mail='suhasrao1218@gmail.com',
    install_requirements=get_requirements('requirements.txt'), # dependency 
    packages=find_packages()
)