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
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",  # https://sphinx-design.readthedocs.io/en/latest/
    # "sphinx_inline_tabs",
    "sphinx_togglebutton",
    # "sphinx_tippy",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

smartquotes_action= 'qDe'
show_warning_types = True
suppress_warnings = ['epub.unknown_project_files']

# EPUB options
epub_theme = 'epub'
epub_theme_options = {"relbar1" : True, "footer": True}
epub_title = 'Title MotionWise'
epub_copyright = 'TTTech Auto'
epub_description = 'Desc MotionWise'
epub_cover = ('_static/cover.jpg', '')
epub_show_urls = 'no'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"

html_title = "MotionWise"
html_short_title = "MotionWise"
html_static_path = ['_static']

html_last_updated_fmt = '%B %d, %Y'
html_show_copyright = False
html_show_sphinx = False

html_theme_options = {
    "source_edit_link": "https://git.tttech.com/projects/TRUNK/repos/0042-how-we-want-to-develop-motionwise/browse/doc/source/{filename}?useDefaultHandler=true",
    "source_view_link": "https://git.tttech.com/projects/TRUNK/repos/0042-how-we-want-to-develop-motionwise/raw/doc/source/{filename}",
}

html_css_files = ["custom.css"] # "tippy.css"
epub_css_files = ["custom_epub.css"]