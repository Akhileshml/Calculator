from setuptools import setup, find_packages

setup(
    name='calculator',
    version='1.0.3',  # Incremented version
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    description='Simple cal package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    options={
        'sdist': {'formats': ['zip']}
    },
)
