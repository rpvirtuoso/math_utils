from setuptools import setup, find_packages

setup(
    name="calc-utils",
    version="0.1.0",
    author="Rahul P",
    author_email="rpvirtuoso@gmail.com",
    description="A package for basic math utilities",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rpvirtuoso/math_utils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
