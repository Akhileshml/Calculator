from setuptools import setup, find_packages

setup(
    name='calculator',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    description='A calculator package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
