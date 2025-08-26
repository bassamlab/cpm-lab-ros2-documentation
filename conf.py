# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CPM Lab'
copyright = '2025 Professorship for Adaptive Behavior of Autonomous Vehicles at University of the Bundeswehr Munich'
author = 'Simon Schäfer'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = ['sphinx_rtd_theme', 'sphinx_copybutton', 'sphinx.ext.autosummary']
extensions = ['sphinxawesome_theme', 'sphinx.ext.autosummary']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv', 'public']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'CPM Lab'

# html_theme = 'sphinx_rtd_theme' 
html_theme = 'sphinxawesome_theme'

html_permalinks = False

html_theme_options = {
    "logo_light": "images/logo.svg",
    "logo_dark": "images/logo-dark.svg",
    "show_breadcrumbs": True,
    "awesome_external_links": True,       
}