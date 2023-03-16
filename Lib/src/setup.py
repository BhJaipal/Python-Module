import setuptools
def readme():
    with open("README.md","r") as read:
        print(read.read())

setuptools.setup(
name= "Lib",
version="0.4.4",
author="Jaipal Bhanwariya",
author_email="jaipalbhanwariya001@gmail.com",
description="This is a Personal Python Module created by Jaipal. It is only accessible to Jaipal. Download this zip file and extract where your python libraries are present and you can access it too by using 'import Lib'",
long_description=readme(),
url="http://github.com/BhJaipal/Personal-Python-Module",
packages= setuptools.find_packages(),
classifiers= ("Programming Language :: Python  :: 3",
"Programming Language :: Python :: 3.4","Programming Language :: Python ::3.6",
"Programming Language :: Python :: 3.8","Programming Language :: Python :: 3.9",
"Programming Language :: Python :: 3.10","Programming Language :: Python ::3.11",
"Operating System :: OS Independent"))
