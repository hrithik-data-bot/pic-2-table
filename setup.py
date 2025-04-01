"""
Once the project is set up, run the following command on the console
to make use of the entry-points:
>>> pip install -e .

This will enable the user to run the module from the command line
as follows:
>>> xyz
"""

# type: ignore
# pylint: skip-file

from setuptools import find_packages, setup

# Define the package version manually
PACKAGE_VERSION = "0.1.0"

requirements = [
    "pandas==1.3.3",
    "matplotlib==3.4.3",
    "seaborn==0.11.2",
    "transformers==4.30.2",
    "huggingface_hub==0.14.1",
    "python-dotenv==1.0.0",
    "autopep8==1.6.0",
    "pylint==2.14.5",
    "timm==0.6.12",
    "torch==2.0.1",
    "torchvision==0.15.2",
    "torchaudio==2.0.2"
]

setup(
    name="pic-2-table",   # Package name
    version=PACKAGE_VERSION,  # Set package version manually
    packages=find_packages(where=".", exclude=["tests", "tests.*"]),
    install_requires=requirements,
    python_requires="==3.10.6",  # Ensuring only Python 3.10.6 is used
    keywords="table-extraction",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "xyz = pic_to_table.cli:main"
        ]
    }
)
