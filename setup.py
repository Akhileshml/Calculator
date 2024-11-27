from setuptools import setup, find_packages

setup(
    name="Calculator",  # Replace with your package name
    version="0.1.0",  # Replace with your package version
    description="A simple calculator package",
    author="Your Name",
    author_email="your.email@example.com",
    py_modules=["cal"],  # List your Python modules here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
