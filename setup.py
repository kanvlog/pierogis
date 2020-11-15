from setuptools import setup
from setuptools import find_packages

setup(
    name='pierogis',
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=[
        'Pillow',
        'numpy'
    ],
)