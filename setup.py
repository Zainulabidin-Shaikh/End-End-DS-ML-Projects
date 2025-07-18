from setuptools import find_packages,setup
from typing import List

req_extras = '-e . # this will automatically trigger setup.py file, and this line comes in extras because its not a package so we have to eliminate it from reading in our function (get_requirements)'

def get_requirements(file_path:str)->List[str]:

    '''
    file_path: str = The argument file_path should be a string
    -> List[str] = The function will return a list of strings
    This is called a type hint or type annotation.
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # from the above code the '\n' will also get read as we have written evey package in a newline
        # in our req..txt file
        # so simply we replace the \n with the empty:
        requirements=[req.replace("\n","") for req in requirements]

        if req_extras in requirements:
            requirements.remove(req_extras)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Zain',
author_email='zainulabidinshaikh12@gmail.com',
packages=find_packages(),
# install_requires=['pandas','numpy','seaborn'] this method is not efficient as we have to manually type so many packages 
# so we do instead : 
install_requires=get_requirements('requirements.txt') # so we make a get_requirements function that takes requirements file as a parameter
# and install all the requirements packages
)


