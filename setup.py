from setuptools import find_packages , setup
from typing import List
# function to create requirements.txt into array 
def getRequirements() -> list[str]:
    with open("requirements.txt" , "r") as file : 
        requirements = file.readlines()
    requirements = [requirements.strip() for req in requirements]
    if "-e ." in requirements:
        requirements.remove("-e .")
    return requirements

setup(
    name = "ToxicCommentClassifier",
    version = "0.0.1",
    author="Shivam Bhardwaj",
    author_email= "shivam63982023@gmail.com",
    packages= find_packages()
)
