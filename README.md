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
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

change the path to ../.. if you use source and build directory.

4. `sphinx-apidoc -o source ../`
5. `sphinx-apidoc -o source ../`
6. `sphinx-build -b html source/ build/`
7. if you add a new module, you need delete `source/module.rst` first and run commands above.



