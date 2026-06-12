from setuptools import find_packages, setup

def getRequirements() -> list[str]:
    with open("requirements.txt", "r") as file:
        requirements = file.readlines()

    requirements = [req.strip() for req in requirements]

    if "-e ." in requirements:
        requirements.remove("-e .")

    return requirements

setup(
    name="ToxicCommentClassifier",
    version="0.0.1",
    author="Shivam Bhardwaj",
    author_email="shivam63982023@gmail.com",
    packages=find_packages(),
    install_requires=getRequirements(),
)