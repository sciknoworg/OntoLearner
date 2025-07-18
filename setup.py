from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="OntoLearner",
    version="1.3.0",
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
        "pandas",
        "matplotlib",
        "tqdm",
        "python-dotenv",
        "rdflib==7.1.1",
        "networkx==3.2.1",
        "pydantic==2.11.3",
        "pathlib==1.0.1",
        "dspy==2.6.14",
        "huggingface-hub==0.31.1",
        "transformers==4.51.3",
        "torch==2.6.0",
        "sentence-transformers==4.1.0",
        "scikit-learn==1.6.1",
        "bitsandbytes==0.45.1",
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
