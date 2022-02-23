# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

autoclass_content = "both"

# -- Project information -----------------------------------------------------

project = "Piccolo API"
year = datetime.datetime.now().strftime("%Y")
author = "Daniel Townsend"
copyright = f"{year}, {author}"


import piccolo_api  # noqa

version = ".".join(piccolo_api.__VERSION__.split(".")[:2])
release = piccolo_api.__VERSION__

# -- General configuration ---------------------------------------------------

master_doc = "index"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "piccolo_theme"
