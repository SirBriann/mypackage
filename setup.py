from setuptools import setup, find_packages
setup(
    name='myPackage',
    version= 0.1,
    packages=find_packages(exclude=['test*']),
    license = 'MIT',
    description = 'EDSA example package in Python',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/SirBriann/myPackage',
    Author = 'Brian Maina',
    AuthorEmail = 'bmaina049@yahoo.com'
)