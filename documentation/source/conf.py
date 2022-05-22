# -*- coding: utf-8 -*-
#
# Testworks documentation build configuration file, created by
# sphinx-quickstart on Fri Oct 26 11:31:31 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
sys.path.insert(0, os.path.abspath('../../ext/sphinx-extensions/sphinxcontrib'))
import dylan.themes as dylan_themes

# -- Project information -----------------------------------------------------

project = 'dylan-libraries'
copyright = '2022, Dylan Hackers'
author = 'Dylan Hackers'


# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'dylan.domain',
    'sphinx.ext.intersphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The primary domain.
primary_domain = 'dylan'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = dylan_themes.get_html_theme_default()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = dylan_themes.get_html_theme_options_default()

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [dylan_themes.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Testworks"

# Output file base name for HTML help builder.
htmlhelp_basename = 'Testworks'


# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Testworks.tex', u'Testworks', u'Dylan Hackers', 'manual'),
]


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'testworks', u'Testworks', [u'Dylan Hackers'], 1)
]


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Testworks', u'Testworks',
   u'Dylan Hackers', 'Testworks', 'One line description of project.',
   'Miscellaneous'),
]


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Testworks'
epub_author = u'Dylan Hackers'
epub_publisher = u'Dylan Hackers'
epub_copyright = u'2022, Dylan Hackers'
