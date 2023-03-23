# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import datetime


# -- Project information -----------------------------------------------------

project = 'Эффективная разработка'
copyright = '2023, Михаил Красильников'
author = 'Михаил Красильников'

# The short X.Y version
version = '0.2'
# The full version, including alpha/beta/rc tags
release = version + '.1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinxcontrib.plantuml',
]

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# A string of reStructuredText that will be included at the beginning of
# every source file that isread. This is a possible place to add
# substitutions that should be available in every file.
rst_prolog = ''

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ru'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
    '_include/*',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-today_fmt
today_fmt = '%d.%m.%Y'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinxdoc'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'style_external_links': True,
    'titles_only': True,
#    'github_url': 'https://github.com/mekras/hwd/'
}

# The "title" for HTML documentation generated with Sphinx’s own templates. This is appended to the
# <title> tag of individual pages, and used in the navigation bar as the "topmost" element. It
# defaults to '<project> v<revision> documentation'.
#
html_title = 'Эффективная разработка'

# A shorter "title" for the HTML docs. This is used in for links in the header and in the HTML Help
# docs. If not given, it defaults to the value of html_title.
#
html_short_title = 'Книга'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# If true (and html_copy_source is true as well), links to the reST sources will be added to the
# sidebar. The default is True.
# New in version 0.6.
#
html_show_sourcelink = False

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'effective-development'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'effective-development.tex', 'Эффективная разработка',
     'Михаил Красильников', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'effective-development', 'Эффективная разработка',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'effective-development', 'Эффективная разработка',
     author, 'effective-development', 'Эффективная разработка.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
