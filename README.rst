===============
threedi_results
===============


.. image:: https://img.shields.io/pypi/v/threedi_results.svg
        :target: https://pypi.python.org/pypi/threedi_results

.. image:: https://img.shields.io/travis/larsclaussen/threedi_results.svg
        :target: https://travis-ci.org/larsclaussen/threedi_results

.. image:: https://readthedocs.org/projects/threedi-results/badge/?version=latest
        :target: https://threedi-results.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python Boilerplate contains all the boilerplate you need to create a Python package.


* Free software: BSD license
* Documentation: https://threedi-results.readthedocs.io.


Features
--------

Dev repo for a future threedi result API experiments.

Example calls::

    # Get node results for timesteps 1,2,3 for s1
    http://0.0.0.0:8000/results/nodes/1,2,3/s1

    # list node fields [testing list view really]
    http://0.0.0.0:8000/results/nodes

    # list line fields [testing list view really]
    http://0.0.0.0:8000/results/lines

    # Get line results for timesteps 3,8,26 for u1
    http://0.0.0.0:8000/results/lines/3,8,26/u1


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
