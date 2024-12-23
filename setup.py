import os

from setuptools import setup

version = os.getenv(
    "VERSION", "0.0.0"
) # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'

setup(
    name = "Mbinias",
    version = version,
    author = "Marcin Biniaś",
    author_email = "marcin.binias@edu.uekat.pl",
    description="Attendance list",
    url="https://github.com/fburczyk/Attendance-List/tree/marcin_testing",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)