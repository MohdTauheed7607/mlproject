from setuptools import setup, find_packages

HYPHEN_E_DOT="-e ."

def get_requirements(file_path):
    with open(file_path,"r") as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
name="mlproject",
version="0.0.1",
author="Tauheed",
author_email="motauheed9452@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)