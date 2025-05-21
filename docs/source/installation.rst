Installation
=============

We recommend **Python 3.10+**,`PyTorch 1.4.0+ <https://pytorch.org/get-started/locally/>`_, and `transformers v4.41.0+ <https://github.com/huggingface/transformers>`_.


Install with pip
-----------------------

.. sidebar:: Verify the installation

    Once the isntallation is done, verify the installation by:

    .. code-block:: python

        import ontolearner

        print(ontolearner.__version__)


.. tab:: From PyPI

    OntoLearner is available on the Python Package Index at `pypi.org <https://pypi.org/project/OntoLearner/>`_ for installation.
    ::

        pip install -U ontolearner

.. tab:: From GitHub

    The following pip install will installs the latest version of OntoLearner from the `main` branch of the OntoLearner at GitHub using `pip`.

    ::

        pip install git+https://github.com/sciknoworg/OntoLearner.git


Install from Source
----------------------
You can install OntoLearner directly from source to take advantage of the bleeding edge main branch for development.


1. Clone the repository:

.. code-block:: bash

    git clone https://github.com/sciknoworg/OntoLearner.git
    cd OntoLearner

2. (Optional but recommended) Create and activate a virtual environment:

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies and the library

.. code-block:: bash

    pip install -e .

.. hint:: The -e flag installs the package in editable mode, which is ideal for development—changes in the code reflect immediately.

Install PyTorch with CUDA support
--------------------------------------------
To use a GPU/CUDA for learners, you must install PyTorch with CUDA support. Follow `PyTorch - Get Started<https://pytorch.org/get-started/locally/>`_ for installation steps.
