from setuptools import setup, find_packages

setup(
    name="nutri_score_calculator",
    version="0.2",
    packages=find_packages(),
    url="https://github.com/malteiwanicki/nutri_score_calculator",
    license="MIT",
    author="Malte Iwanicki",
    author_email="malteiwa@gmail.com",
    description="A Python package to calculate Nutri-Score based on the formula of 2024.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
