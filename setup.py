
from setuptools import setup,find_packages
from typing import List

REQQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description : This function is going to return list of requiremenet mention
    in the requirements.txt file

    return: This function is going to return a list which contain name of
    libraries mentioned in the requirements.txt file
    """
    with open ( REQQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines().remove("-e .")

# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.3"
AUTHOR = "Shashank Kandpal"
DESCRIPTION = "This is a first FSDS NOV batch MAchine Learning Project"
#PACKAGES = ["housing"]

setup(
    name  = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())