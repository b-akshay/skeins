"""Sphinx configuration."""
project = "skeins"
author = "Akshay Balsubramani"
copyright = "2023, Akshay Balsubramani"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
napoleon_numpy_docstring = True