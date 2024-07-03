#
# LDMP documentation build configuration file, created by
# sphinx-quickstart on Sun Feb 12 17:11:03 2012.
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
from datetime import date

import sphinx_rtd_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
# extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'rinoh.frontend.sphinx']
# extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'rst2pdf.pdfbuilder']
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinxcontrib.spelling",
    "myst_parser",
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Spellcheck options
spelling_word_list_filename = ["known_good_spellings.txt"]
# Don't check the general/index.rst file due to all the names in the publications lists
# that show up as misspellings
spelling_exclude_patterns = ["general/index.rst"]
spelling_ignore_pypi_package_names = True


todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = [".rst", ".md"]

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Trends.Earth"
copyright = "2017-{}, Conservation International".format(date.today().year)

locale_dirs = ["../i18n/"]
gettext_compact = False

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "2.1.16"
# The full version, including alpha/beta/rc tags.
release = "2.1.16"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = os.environ.get("READTHEDOCS_LANGUAGE")
if not language:
    for t in tags:
        if t.startswith("language_"):
            language = t[9:]

READTHEDOCS_VERSION_STRING = os.environ.get("READTHEDOCS_VERSION", "")
relative_path = "../"
# On RTD there the root is two folders back - one for the language, and one for the
# version name, so need to add another "../"
if READTHEDOCS_VERSION_STRING != "":
    relative_path += "../"

pdf_url_base = "https://data.trends.earth/documentation/"


extlinks = {
    "index_path": (f"{relative_path}%s/{READTHEDOCS_VERSION_STRING}", "%s"),
    "docs_pdf": (f"{pdf_url_base}TrendsEarth_%s_{version}_{language}.pdf", "%s"),
}

rst_epilog = f"""
.. |iconCalculator| image:: /static/common/icon-calculator.png
   :width: 2em
.. |iconReports| image:: /static/common/reports_button.png
   :width: 82
.. |trends.earth| image:: /static/common/trends_earth_logo_bl_print.png
   :width: 7em
   :alt: Trends.Earth
.. |CURRENT| replace:: {version}
.. |qgisMinVersion| replace:: 3.22
"""

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["../resources"]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_TemplateModuleNames = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "trends_earth_logo_square_32x32.ico"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "trends_earth_logo_square_32x32.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["static"]

html_show_sourcelink = False

# Note the underscore SHOULD be used below as this is how the static folder is
# named by sphinx on generation.
html_css_files = ["custom.css"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
# htmlhelp_basename = "TemplateClassdoc"

# -- Options for LaTeX output --------------------------------------------------

user_guide_titles = {
    "en": "Trends.Earth - User Guide",
    "es": "Trends.Earth - Guía del usuario",
    "fa": "Trends.Earth - راهنمای کاربر",
    "fr": "Trends.Earth - Guide de l'utilisateur",
    "pt": "Trends.Earth - Guia do usuário",
    "ru": "Trends.Earth — Руководство пользователя",
    "sw": "Trends.Earth - Mwongozo wa Mtumiaji",
    "zh": "Trends.Earth - 用户指南",
}
developer_guide_titles = {
    "en": "Trends.Earth - Developer Guide",
    "es": "Trends.Earth - Guía para desarrolladores",
    "fa": "Trends.Earth - راهنمای برنامه نویس",
    "fr": "Trends.Earth - Guide du développeur",
    "pt": "Trends.Earth - Guia do desenvolvedor",
    "ru": "Trends.Earth — Руководство для разработчиков",
    "sw": "Trends.Earth - Mwongozo wa Wasanidi Programu",
    "zh": "Trends.Earth - 开发者指南",
}
general_information_titles = {
    "en": "Trends.Earth - General Information",
    "es": "Trends.Earth - Información general",
    "fa": "Trends.Earth - اطلاعات عمومی",
    "fr": "Trends.Earth - Informations générales",
    "pt": "Trends.Earth - Informações gerais",
    "ru": "Trends.Earth - Общая информация",
    "sw": "Trends.Earth - Taarifa za Jumla",
    "zh": "Trends.Earth - 一般信息",
}

latex_documents = [
    (
        "for_users/index",
        f"TrendsEarth_User_Guide_{version}_{language}.tex",
        user_guide_titles.get(language, user_guide_titles["en"]),
        "Conservation International",
        "manual",
    ),
    (
        "for_developers/index",
        f"TrendsEarth_Developer_Guide_{version}_{language}.tex",
        developer_guide_titles.get(language, developer_guide_titles["en"]),
        "Conservation International",
        "manual",
    ),
    (
        "general/index",
        f"TrendsEarth_General_Information_{version}_{language}.tex",
        general_information_titles.get(language, general_information_titles["en"]),
        "Conservation International",
        "manual",
    ),
]

# latex_elements = {
#     # The paper size ('letterpaper' or 'a4paper').
#     "papersize": "a4paper",
#     "preamble": u"""\\usepackage{fontspec}
#                     \\setmainfont{lmroman10-regular.otf}""",
# }

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "../resources/en/common/trends_earth_logo_bl_1200.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = True

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).

latex_engine = "xelatex"
latex_use_xindy = False
latex_elements = {"extraclassoptions": "openany,oneside"}
