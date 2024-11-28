from setuptools import setup, find_packages

setup(
    name="code_complexity_pro",
    version="1.1.2",
    author="Madhur Saluja",
    author_email="msaluja1@myseneca.ca",
    description="A Python tool for analyzing code complexity",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/code-complexity-pro",  
    packages=find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "python-dotenv",
        "toml",
    ],
    entry_points={
        "console_scripts": [
            "code_complexity_pro=code_complexity_pro.main:main", 
        ],
    },
)
