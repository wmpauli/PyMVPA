# emacs: -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
#
# PyMVPA documentation build configuration file, created by
# sphinx-quickstart on Tue Dec 29 10:32:00 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, re
import numpy as np
import mvpa2

# We need to know sphinx version for decisions below
import sphinx
from distutils.version import LooseVersion
sphinx_version = LooseVersion(sphinx.__version__)

try:
    import matplotlib
    # Disable warning from matplotlib
    import warnings
    warnings.filterwarnings(
        'ignore', 'This call to matplotlib.use() has no effect.*',
        UserWarning)
    matplotlib.use('svg')
except:
    pass

##################################################
# Config settings are at the bottom of the file! #
##################################################

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('../sphinxext'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.ifconfig',
              'sphinx.ext.inheritance_diagram',
              'sphinx.ext.pngmath',
              # we have a local copy of the extension, imported from NumPy 1.3
              # this also includes the docscrape* extensions
              'numpydoc',
              # finally our own little thingie to display tasks
              'exercise_directive']

# we have a local copy of autosummary from the unreleased sphinx
# 1.0 -- reason: the 0.6 extension creates half-empty summaries
extensions += [sphinx_version < '1.1.2'
               and 'autosummary'
               or 'sphinx.ext.autosummary']

# the following doesn't work with sphinx < 1.0, but will make a separate
# sphinx-autogen run obsolete in the future
#autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General substitutions.
project = 'PyMVPA'
copyright = '2006-2010, PyMVPA Authors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = mvpa2.__version__
# The full version, including alpha/beta/rc tags.
release = mvpa2.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# what to put into API doc (just class doc, just init, or both
autoclass_content = 'both'

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None
#default_role = "autolink" # causes actual running of code and crashes
# the problem with this setting is that is also confused things
# `Dataset` might lead to a link to the h5py.Dataset` docs
default_role = "obj"	   # seems to be sufficient to provide basic hyperlinking


# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'pymvpa_offline'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = 'pics/pymvpa_logo.jpg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'index': 'indexsidebar.html'}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {'index': 'index.html'}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'PyMVPAdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('pdfmanual', 'PyMVPA-Manual.tex', 'PyMVPA Manual',
   'PyMVPA Authors',
   'manual'),
  ('devguide', 'PyMVPA-DevGuide.tex', 'PyMVPA Developer Guidelines',
   'PyMVPA Authors',
   'manual'),
#  ('modref', 'PyMVPA-Reference.tex', 'PyMVPA Reference',
#   'PyMVPA Authors',
#   'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'pics/pymvpa_logo.pdf'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
latex_preamble = r"""
\usepackage{enumitem}
\setdescription{style=nextline,font=\normalfont}

% more table of contents
\setcounter{tocdepth}{3}

% Have gray background for notes and exercises
\definecolor{MyBluishGray}{rgb}{0.90,0.90,1.00}

\makeatletter\newenvironment{graybox}{%
   \begin{lrbox}{\@tempboxa}\begin{minipage}{\columnwidth}}{\end{minipage}\end{lrbox}%
   \colorbox{MyBluishGray}{\usebox{\@tempboxa}}
}\makeatother

\makeatletter
\renewenvironment{notice}[2]{
  \begin{graybox}
  \bf\it
  \def\py@noticetype{#1}
  \par\strong{#2}
  \csname py@noticestart@#1\endcsname
}
{
  \csname py@noticeend@\py@noticetype\endcsname
  \end{graybox}
}
\makeatother

"""

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# -----------------------------------------------------------------------------
# Intersphinx configuration
# -----------------------------------------------------------------------------
# to link to related projects
intersphinx_mapping = {'http://docs.python.org/': None,
                       'http://nipy.sourceforge.net/nipype': None,
                       'http://nipy.sourceforge.net/nipy/stable': None,
                       'http://h5py.alfven.org/docs': None,
                       'http://docs.scipy.org/doc/scipy/reference': None,
                       'http://docs.scipy.org/doc/numpy/': None,
                       'http://matplotlib.sourceforge.net/': None,
                       }
