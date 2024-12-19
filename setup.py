import os

from setuptools import setup


version = os.getenv(
    "VERSION", "0.0.0"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'



setup(
    name="fburczyk",
    version=version,
    author="Filip Burczyk",
    author_email="filip.b0311@gmail.com",
    description="Attendance list",
    url="https://github.com/fburczyk/Attendance-List/tree/filip_testing",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.8",
)
