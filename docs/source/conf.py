# Configuration file for the Sphinx documentation builder.
# import pathlib
# import sys
import datetime
import importlib
import inspect
import os
# -- Project information -----------------------------------------------------
#
# from sphinx.search import IndexBuilder
# import snowballstemmer
#
# # Override the stemmer with 'english' instead of 'porter'
# IndexBuilder.lang = 'en'
# IndexBuilder.stemmer = snowballstemmer.stemmer('english')

year = str(datetime.datetime.now().year)
project = 'OntoLearner'
copyright = year + ' SciKnowOrg'
release = '0.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "myst_parser",
    "sphinx_markdown_tables",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.linkcode",
    "sphinx_inline_tabs",
    "sphinxcontrib.mermaid",
    'sphinx_tabs.tabs',
]

# autosummary_generate = True  # Turn on sphinx.ext.autosummary

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to include when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
include_patterns = [
    "**",
    "index.rst",
]
# Ensure exclude_patterns doesn't exclude your master document accidentally
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

source_suffix = '.rst'

# specify the master doc, otherwise the build at read the docs fails
master_doc = "index"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "external_links": [
          ("Github", "https://github.com/sciknoworg/OntoLearner"),
    ],
    "navigation_depth": 4,
    "collapse_navigation": True
}

html_static_path = ["_static"]

html_js_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js',
    'custom.js'
]

html_css_files = [
    # 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css',
    'custom.css',
]

html_show_sourcelink = True
html_context = {
    "display_github": True,
    "github_user": "sciknoworg",
    "github_repo": "OntoLearner",
    "github_version": "main/",
}

html_logo = 'images/logo.png'
html_favicon = "images/icon.ico"
autoclass_content = "both"

# Required to get rid of some myst.xref_missing warnings
myst_heading_anchors = 3

html_copy_source = True
def linkcode_resolve(domain, info):
    """
    Resolve a GitHub link for the given domain and info dictionary.
    """
    if domain != "py" or not info["module"]:
        return None

    # Define the GitHub repository URL
    repo_url = "https://github.com/sciknoworg/OntoLearner/blob/main"
    branch = "main"  # Update if using a different branch

    # Retrieve the module and object
    try:
        module = importlib.import_module(info["module"])
    except ImportError:
        return None

    # Try to get the source file and line numbers
    try:
        file_path = inspect.getsourcefile(module)
        source_lines, start_line = inspect.getsourcelines(getattr(module, info["fullname"]))
    except (TypeError, AttributeError, OSError):
        return None

    # Generate the relative file path and GitHub link
    relative_path = os.path.relpath(file_path, start=os.path.dirname(__file__))
    end_line = start_line + len(source_lines) - 1
    return f"{repo_url}/blob/{branch}/{relative_path}#L{start_line}-L{end_line}"
