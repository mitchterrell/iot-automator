# Configuration file for the Sphinx documentation builder.


# -- Project information -----------------------------------------------------

project     = 'Internal Developer Docs'
copyright   = '2022, Mitch Terrell'
author      = 'Mitch Terrell'


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

# If we add folders that we want excluded we add the realitive path here
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# Theme selection 
html_theme          = "furo"

# This path contains a folder for statically linked files to the webpage (i.e. css + js files)

html_static_path    = ['_static']

html_css_files      = [
    'custom.css',
]

html_logo           = "../../docs/source/_static/colored_logo_w_name.svg"       ## Linking from primary documents

html_title          = "Internal Dev Docs"

html_favicon        = '../../docs/source/_static/colored_logo.svg'              ## Linking from primary documents

html_theme_options = {
    "sidebar_hide_name": True,
}