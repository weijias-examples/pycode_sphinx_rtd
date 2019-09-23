# A simple example to generate documents using sphinx

# Installation
```
>>> pip install sphinx
```

# steps
1. make a `docs` directory
2. enter `docs`, and run `sphinx-quickstart`. Seperating source and build
3. set autodoc to yes. If not, add in extensions.

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.doctest',
              ]

4. change conf.py. uncomment the lines

`import os`

`import sys`

`sys.path.insert(0, os.path.abspath('../..'))`

Add the below line to avoid `contents.rst not found`

`master_doc = 'index'`

By default, Sphinx expects the master doc to be contents. 
Read the Docs will set master doc to index instead (or whatever it is you have specified in your settings). 
Try adding this to your conf.py:

`master_doc = 'index'`



change the path to ../.. if you use source and build directory.

4. `sphinx-apidoc -o source ../`
5. `sphinx-apidoc -o source ../`
6. `sphinx-build -b html source/ build/`
7. if you add a new module, you need delete `source/module.rst` first and run commands above.

For detailed information of setting RTD, refer to [RTD](https://docs.readthedocs.io/en/latest/webhooks.html)


# link the github with RTD
see links for two ways.
1. https://docs.readthedocs.io/en/stable/webhooks.html
2. https://docs.readthedocs.io/en/stable/connected-accounts.html

