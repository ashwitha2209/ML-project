from setuptools import setup,find_packages
with open("Requirements.txt") as f:
    Requirements=f.read().splitlines()

setup(
    name="MLOPS-PROJECT-1",
    version="0.1",
    author="Ashwitha",
    packages=find_packages(),
    install_requires=Requirements,
)
 