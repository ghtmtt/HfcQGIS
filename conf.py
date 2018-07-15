# -*- coding: utf-8 -*-
#
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

import sys, os
import recommonmark
from recommonmark.transform import AutoStructify

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_static_path = ['static']

def setup(app):
    # overrides for wide tables in RTD theme
    app.add_stylesheet('theme_overrides.css') # path relative to static

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

source_suffix = ['.rst', '.md']

extensions = ['sphinx.ext.ifconfig','sphinx_markdown_tables']

# The master toctree document.
master_doc = 'index'

# General information about the project.


# project = u'HfcQGIS'
project = u''
copyright = u'2018, Salvatore Fiandaca'
author = u'Salvatore Fiandaca'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'HfcQGIS - 1.0'
# The full version, including alpha/beta/rc tags.
release = u'HfcQGIS - 1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "img/favicon_h.ico"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "img/logo_hfc_00.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'description': 'HfcQGIS - Help funzioni calcolatore di campi di QGIS',
    'sticky_navigation': True,
    'style_external_links': True
}


# Output file base name for HTML help builder.
htmlhelp_basename = 'HfcQGIS'

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'HfcQGIS', u'HfcQGIS Documentation',
     [u'Salvatore Fiandaca'], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'HfcQGIS', u'HfcQGIS Documentation',
   u'Salvatore Fiandaca', 'HfcQGIS', 'Help funzioni calcolatore di campi di QGIS'
   ),
]

github_doc_root = 'https://github.com/gbvitrano/HfcQGIS/tree/master/'

# app setup hook
def setup(app):
    app.add_config_value('recommonmark_config', {
        'url_resolver': lambda url: github_doc_root + url,
        'enable_eval_rst': True,
        'enable_auto_doc_ref': True
    }, True)
    app.add_transform(AutoStructify)
