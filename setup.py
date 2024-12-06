from setuptools import setup, find_packages

setup(
    name='calculator',
    use_scm_version=True,  # Automatically manage version via Git tags
    setup_requires=['setuptools_scm'],  # Dependency for versioning
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
