# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "skeins"
author = "Akshay Balsubramani"
copyright = "2023, Akshay Balsubramani"
# release = "0.1.2"
# extensions = [
#     "sphinx.ext.autodoc",
#     "sphinx.ext.napoleon",
#     "sphinx_click",
#     "myst_parser",
# ]


extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'nbsphinx']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

root_doc = 'index'
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
# autodoc_typehints = "description"
# html_theme = "furo"
# napoleon_numpy_docstring = True



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
