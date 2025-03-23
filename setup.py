"""
Once the project is set-up, run the following command on the console
to make use of the entry-points:
>>> pip install -e .

This will enable user to run the module from the command line
following way:
>>> xyz
"""

# type: ignore
# pylint: skip-file

from setuptools import find_packages, setup
import versioneer


requirements = [
    # package requirements (other than Python) go here
    # add required dependencies that are also specified in conda.yaml

]

setup(
    name='xyz',
    version=versioneer.get_version(),
    packages=find_packages(where='.', exclude=['tests', 'tests.*']),
    install_requires=requirements,
    keywords='xyz',
    classifiers=[
        'Programming Language :: Python :: 3.10.6',
    ],
    entry_points={
        'console_scripts': [
            'xyz = pic_to_table.cli:main'
        ]
    }
)
