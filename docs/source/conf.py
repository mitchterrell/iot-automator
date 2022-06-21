# Configuration file for the Sphinx documentation builder.


# -- Project information -----------------------------------------------------

project     = 'iot-automator'
copyright   = '2022, Mitchell Terrell'
author      = 'Mitchell Terrell'
release     = '1.0_beta'


# -- General configuration ---------------------------------------------------

# Sphinx extensions to include in the project

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    
    # External stuff
    "sphinx_copybutton",
    "sphinx_design",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

#
# -- Options for TODOs -------------------------------------------------------
#
todo_include_todos = True

#
# -- Options for extlinks ----------------------------------------------------
#
extlinks = {
    "pypi": ("https://pypi.org/project/%s/", ""),
}

#
# -- Options for intersphinx -------------------------------------------------
#
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# If we add folders that we want excluded we add the realitive path here
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# Theme selection 
html_theme = "furo"

# This path contains a folder for statically linked files to the webpage (i.e. css + js files)
html_static_path    = ['_static']

html_css_files      = [
    'custom.css',
]

html_logo           = "_static/colored_logo_w_name.svg"

html_title          = "iot-automator"

html_favicon        = '_static/colored_logo.svg'

html_theme_options = {
    "sidebar_hide_name": True,
}
