# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from operator import truediv

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'How we develop MotionWise'
author = 'Sebastian Caban'
release = '1'
version = '1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # Sphinx's own extensions
    # "sphinx.ext.extlinks",
    # "sphinx.ext.intersphinx",
    # "sphinx.ext.mathjax",
    # "sphinx.ext.todo",
    # "sphinx.ext.viewcode",
    # External stuff
    "myst_parser",
    "sphinx_copybutton",
    # "sphinx_design",  # https://sphinx-design.readthedocs.io/en/latest/
    # "sphinx_inline_tabs",
    # "sphinx_togglebutton",
    #" sphinx_tippy",
    #"sphinx.ext.autodoc",
]

html_last_updated_fmt = '%B %d, %Y'
html_show_copyright = False
html_show_sphinx = False

html_theme_options = {
    "source_edit_link": "https://git.tttech.com/projects/CONTX/repos/prefect-bi-etl/browse/doc/{filename}",
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

smartquotes_action= 'bDe'
show_warning_types = True
suppress_warnings = ['epub.unknown_project_files']

# EPUB options
epub_theme = 'epub'
epub_theme_options = {"relbar1" : True, "footer": True}
epub_title = 'Title MotionWise'
epub_copyright = 'TTTech Auto'
epub_description = 'Desc MotionWise'
epub_cover = ('_static/cover.png', '')
epub_show_urls = 'no'



# epub_show_urls = 'footnote'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_theme_options = {}
html_title = "MotionWise"
html_short_title = "MotionWise"
html_static_path = ['_static']
