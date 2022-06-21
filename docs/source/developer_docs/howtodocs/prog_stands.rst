

Programming Standards
========================

We want this library to be bullet proof to the best of our ability. 

Here are some initial thoughts on how to do this: 


Code Standards:
---------------

- Use Black python formatter to ensure that the code is well formatted
- Use Pylint to disallow unused imports
- Use MyPy for type checking

`Using Black + PyLint + MyPy w/ GitHub <https://composed.blog/python/github-actions>`_

Testing:
---------
We want automated unit tests for everything that we do and we want these to run as part 
of GitHub workflow. 

**How do we do this?** 

Documentation:
---------------

#. Sphinx + ReadTheDocs documentation for all major features
#. Automated API documentation generated from comment blocks
#. UML for the entire project workflow would be awesome... How can we do this?

