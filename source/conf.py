# -*- coding: utf-8 -*-
#
# DiracDocs documentation build configuration file, created by
# sphinx-quickstart on Sun Apr 25 17:34:37 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

sys.path.append(os.getcwd())

import fakeEnv

sys.modules["DIRAC.Core.Base"] = fakeEnv
sys.modules["DIRAC.Core.Base.Script"] = fakeEnv
sys.modules["DIRAC.Core.Base.DB"] = fakeEnv
sys.modules["DIRAC.Core.Base.AgentModule"] = fakeEnv
sys.modules["DIRAC.Core.Base.API"] = fakeEnv
sys.modules["DIRAC.Core.Base.Client"] = fakeEnv
sys.modules["DIRAC.Core.Base.AgentReactor"] = fakeEnv

sys.modules["DIRAC.DataManagementSystem.DB.RequestDB"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.Graphs"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.Graphs.BarGraph"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.Graphs.Graph"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.Graphs.GraphData"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.Graphs.GraphUtilities"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.Graphs.Legend"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.Graphs.LineGraph"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.Graphs.Palette"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.Graphs.PieGraph"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.Graphs.PlotBase"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.Graphs.QualityMapGraph"] = fakeEnv
sys.modules["DIRAC.Core.Utilities.OracleDB"] = fakeEnv
sys.modules["RequestDB"] = fakeEnv
sys.modules["pytz"] = fakeEnv
sys.modules["numpy"] = fakeEnv
sys.modules["numpy.random"] = fakeEnv
sys.modules["matplotlib"] = fakeEnv
sys.modules["matplotlib.ticker"] = fakeEnv
sys.modules["matplotlib.figure"] = fakeEnv
sys.modules["matplotlib.dates"] = fakeEnv
sys.modules["dateutil"] = fakeEnv
sys.modules["dateutil.relativedelta"] = fakeEnv
sys.modules["matplotlib.backends"] = fakeEnv
sys.modules["matplotlib.backends.backend_agg"] = fakeEnv
sys.modules["MySQLdb"] = fakeEnv
sys.modules["DIRAC.FrameworkSystem.Service.PlotCache"] = fakeEnv
sys.modules["DIRAC.FrameworkSystem.Service.PlottingHandler"] = fakeEnv



# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'DIRAC'
copyright = u'2011, DIRAC Project'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%H:%M %d/%m/%Y %Z'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

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
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {
#  'sidebarbgcolor':'#D5E2F2'                      
#}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "DIRAC Documentation"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = '_static/DIRAC-logo-transp.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d/%m/%Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'DiracDocsdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'DiracDocs.tex', u'DIRAC Documentation',
   u'DIRAC Project.', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
