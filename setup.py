import os

from setuptools import setup

version = os.getenv(
    "VERSION", "0.0.0"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'



setup(
    name="Attendance_list",
    version=version,
    author="Kamil Biłous",
    author_email="bruhleq@gmail.com",
    description="Attendance list managment";
    url="https://github.com/fburczyk/Attendance-List/tree/kamil_testing",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
