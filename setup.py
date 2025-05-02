from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="OntoLearner",
    version="0.4.0",
    author="Hamed Babaei Giglou, Andrei C. Aioanei",
    author_email="hamedbabaeigiglou@gmail.com, andrei.c.aioanei@gmail.com",
    description="OntoLearner: Ontology Learning Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sciknoworg/OntoLearner",
    packages=find_packages(),
    install_requires=[
        "rdflib==7.1.1",
        "networkx==3.2.1",
        "seaborn==0.13.2",
        "numpy==1.26.4",
        "pandas==2.1.1",
        "matplotlib==3.9.4",
        "tqdm==4.67.1",
        "pydantic==2.10.5",
        "pathlib==1.0.1",
        "dspy==2.6.22"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10,<4.0.0",
    project_urls={
        "Documentation": "https://ontolearner.readthedocs.io/",
        "Source": "https://github.com/sciknoworg/OntoLearner",
        "Tracker": "https://github.com/sciknoworg/OntoLearner/issues",
    },
)
