from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT =  '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]  # next line mai jane par \n remove karna hai, that's why we've used list comprehension

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOTs)

        return requirements


setup(
    name = 'DiamondPricePrediction',
    version = '0.0.1',
    author = 'Amit',
    author_email = 'amitgour1390@gmail.com',
    # install_requires = ['pandas', 'numpy'],    # for installing basic libs. I can also give it to requirements.txt file (where all libs are there)
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()      # for indentifying sub-modules
)