from setuptools import setup, find_packages

setup(
    name="waduh",
    version="0.1.0",
    author="indra87g",
    author_email="noeldycreator@gmail.com",
    description="A multifunction library for python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/indra87g/waduh",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.11',
)