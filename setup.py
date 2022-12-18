import setuptools
def readme():
    with open("Lib/README.md","r") as read:
        print(read.read())

setuptools.setup(
name= "lib",
version="0.3.4",
author="Jaipal Bhanwariya",
author_email="jaipalbhanwariya001@gmail.com",
description="This is a Personal Python Module created by Jaipal. It is only accessible to Jaipal.",
long_description=readme(),
url="storage/emulated/0/qpython/lib/python3.6/site-packages",
packages= setuptools.find_packages(),
classifiers= ("Programming Language :: Python  :: 3",
"Programming Language :: Python :: 3.4","Programming Language :: Python ::3.6",
"Programming Language :: Python :: 3.8","Programming Language :: Python :: 3.9",
"Programming Language :: Python :: 3.10","Programming Language :: Python ::3.11",
"Operating System :: OS Independent"))