from setuptools import setup, find_packages

setup(
    name="wordfrequency",
    packages=find_packages(),
    install_requires=[
        "click",
        "requests",
    ],
    version="0.0.0",
    entry_points="""
    [console_scripts]
    wordfrequency=wordfrequency:wordfrequency
    """,
)
