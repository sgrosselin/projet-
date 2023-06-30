# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath("../ConstructionPlanVol"))
sys.path.insert(0, os.path.abspath("../ConstructionPlanVol/Modules"))
sys.path.insert(0, os.path.abspath("../ConstructionPlanVol/Modules"))

project = 'Projet_Final'
copyright = '2023, Emilien Morlet / Salomé Grosselin / Slimane Iskounene / Cassiopée Dujardin'
author = 'Emilien Morlet / Salomé Grosselin / Slimane Iskounene / Cassiopée Dujardin'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc','sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static', 'data']
