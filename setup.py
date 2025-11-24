from setuptools import setup, find_packages
import os

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="OntoLearner",
    version=open(os.path.join(os.path.dirname(__file__), 'ontolearner/VERSION')).read().strip(),
    author="Hamed Babaei Giglou, Andrei C. Aioanei",
    author_email="hamedbabaeigiglou@gmail.com, andrei.c.aioanei@gmail.com",
    description="OntoLearner: A Modular Python Library for Ontology Learning with LLMs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sciknoworg/OntoLearner",
    packages=find_packages(),
    install_requires=[
        "seaborn",
        "numpy",
        "openpyxl",
        "pandas",
        "matplotlib",
        "tqdm",
        "g4f",
        "python-dotenv",
        "rdflib==7.1.1",
        "networkx==3.2.1",
        "pydantic==2.11.3",
        "pathlib==1.0.1",
        "dspy>=2.6.14,<3.0.0",
        "torch>=2.8.0,<3.0.0",
        "huggingface-hub>=0.34.4,<1.0.0",
        "transformers>=4.56.0,<5.0.0",
        "sentence-transformers>=5.1.0,<6.0.0",
        "scikit-learn>=1.6.1,<2.0.0",
        "bitsandbytes>=0.45.1,<1.0.0",
        "protobuf<5",
        "Levenshtein"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10,<3.14.0",
    project_urls={
        "Documentation": "https://ontolearner.readthedocs.io/",
        "Source": "https://github.com/sciknoworg/OntoLearner",
        "Tracker": "https://github.com/sciknoworg/OntoLearner/issues",
    },
)
