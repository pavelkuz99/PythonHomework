from setuptools import setup, find_packages

setup(
    name='pycalc',
    version='1.0.1',
    author='Pavel Kuzmich',
    author_email='pavelkuz99@outlook.com',
    description='Pure Python command-line calculator',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pycalc=calculator.pycalc:main',
        ]
    }
)
