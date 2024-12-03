from setuptools import setup, find_packages

setup(
    name='pattern_formation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'dask',
        'click',  # Add 'click' for the CLI tool
    ],
    entry_points={
        'console_scripts': [
            'run-simulation=src.pattern_simulation:main',
        ],
    },
)
