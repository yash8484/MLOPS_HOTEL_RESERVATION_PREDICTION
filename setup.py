from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-PROJECT",
    version="0.1",
    author="Yash_Sontakke",
    packages=find_packages(),
    install_requires = requirements,

)
