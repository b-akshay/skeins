.. .. image:: logo/pomegranate-logo.png
.. 	:width: 300px

.. |

.. .. image:: https://readthedocs.org/projects/pomegranate/badge/?version=latest
..    :target: http://pomegranate.readthedocs.io/en/latest/?badge=latest

.. |


====================
skeins API reference
====================


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Getting Started
   :numbered:
   :name: start




Installation
============

The most recent release can be installed from `PyPI <https://pypi.org/project/skeins>`_:

.. code-block:: shell

    $ pip install skeins

To get the extras, install with:

.. code-block:: shell

    $ pip install skeins[viz]

The most recent code and data can be installed directly from GitHub with:

.. code-block:: shell

    $ pip install git+https://github.com//skeins.git

To install in development mode, use the following:

.. code-block:: shell

    $ git clone git+https://github.com//skeins.git
    $ cd skeins
    $ pip install -e .



Graphs
======

Graph calculus
>>>>>>>>>>>>>>

.. automodule:: skeins.graph_calculus
    :members:


Graph construction
>>>>>>>>>>>>>>>>>>

.. automodule:: skeins.graph_construction
    :members:

.. automodule:: skeins.graph_frequencies
    :members:

.. automodule:: skeins.graph_prediction
    :members:

.. automodule:: skeins.utils_graph
    :members:


Miscellaneous
=============

.. automodule:: skeins.visualization
    :members:

.. automodule:: skeins.datasets
    :members:

.. automodule:: skeins.utils_linear
    :members:




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



.. Thank You
.. =========

.. No good project is done alone, and so I'd like to thank all the previous contributors to YAHMM, all the current contributors to pomegranate, and the many graduate students whom I have pestered with ideas and questions. 

.. Contributions
.. =============

.. Contributions are eagerly accepted! If you would like to contribute a feature then fork the master branch and be sure to run the tests before changing any code. Let us know what you want to do on the issue tracker just in case we're already working on an implementation of something similar. Also, please don't forget to add tests for any new functions. Please review the `Code of Conduct <https://pomegranate.readthedocs.io/en/latest/CODE_OF_CONDUCT.html>`_ before contributing. 