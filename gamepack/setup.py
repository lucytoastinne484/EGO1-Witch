import setuptools 
import os


path = r"C:\Users\Computador\EGO1Project\tutorialandobjs\README.md"
os.chdir(path)
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="ego1witch",
 
    #version of the module
    version="2024.1.0" ,
 
    #Name of Author
    author="lucytoastinne484",
 
    #your Email address
    author_email="https://lucytoastinne.carrd.co",
 
    #Small Description about module
    description="a package for help in my game developing",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/lucytoastinne484/EGO1-Witch",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)