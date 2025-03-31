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
import versioneer

requirements = [
    "pandas",
    "matplotlib",
    "seaborn",
    "transformers",
    "huggingface_hub",
    "python-dotenv",
    "autopep8",
    "pylint",
    "timm",
    "torch",
    "torchvision",
    "torchaudio"
]

setup(
    name="pic-2-table",
    version=versioneer.get_version(),
    packages=find_packages(where=".", exclude=["tests", "tests.*"]),
    install_requires=requirements,
    python_requires=">=3.10.6",
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
