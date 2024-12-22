from setuptools import setup, find_packages

setup(
    name="py_matrix_operations",
    version="1.0.0",
    description="A Python module for matrix operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Fitahiana Christalin RATSIMBAZAFY",
    author_email="ratsimbazafyf.christalin@gmail.com",
    url="https://github.com/Rafita261/matrix-operations",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
