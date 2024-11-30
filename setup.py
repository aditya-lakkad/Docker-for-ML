import io
import os
from pathlib import Path

from setuptools import setup, find_packages

# metadata

NAME = 'CaloriesBurned_Prediction_Model'
DESCRIPTION = 'Predicts the calories burned during the workout based on several fatures'
EMAIL = 'lakkadaditya@gmail.com'
AUTHOR = 'Aditya Lakkad'
LICENSE = 'MIT'

path = os.path.abspath((os.path.dirname(__file__)))

# get the list of packages tobe installed
def list_of_requirements(fname='requirement.txt'):
    with open(os.path.join(path, fname), 'r', encoding='utf-16') as f:
        return f.read().splitlines()


setup(
    name=NAME,
    version='1.0.0',
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(),
    install_requires=list_of_requirements('requirement.txt'),
    license=LICENSE
)
