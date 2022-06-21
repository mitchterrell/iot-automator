

External Documentation
========================

How to build
--------------

In the ``docs`` folder or the ``internal_docs`` folder you can:

Clean Out the Build:
*********************

.. code:: none
	
	make.bat clean

Build HTML:
*************

.. code:: none
	
	make.bat html


After the html is build you can open up the files by opening:

.. code:: none

	docs/build/html/index.html


RST Reference
--------------

.. button-link:: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
    :color: warning
    :outline:

	Sphinx RST Primer

.. button-link:: https://docutils.sourceforge.io/docs/user/rst/quickref.html
    :color: warning
    :outline:

	Docutils RST Reference

.. button-link:: https://sphinx-design.readthedocs.io/en/furo-theme/index.html
    :color: warning
    :outline:

	Sphinx Design Reference

File Structure
----------------

docs or internal_docs folder:

- source:
	- Contains the source code the restructured text that is compiled by Sphinx into another form
- build:
	- Contains build artifacts after running make.bat 
	- *Note that this folder is ignored in the gitignore file*
- source/conf.py
	- This is the configuration python file that tells Sphinx how to build the source
- source/index.rst
	- This is the starting restructured text file. In the Toctree it will rerference all other docs
- source/_static
	- Folder that will contain static references for the html pages such as CSS and JS fils
- source/_template
	- Folder that will contain template files to format the html output of sphinx (not currently using this)
- source/*other folders*
	- Any other folders are expected to have an index.rst file in them and should be linked in by their parent index.rst in the toctree


Adding External Libraries
--------------------------

#. pip install <library you want>
#. Add that library reference to the ``extensions`` list in ``conf.py``