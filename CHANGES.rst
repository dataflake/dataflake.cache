Change log
==========

3.3 (unreleased)
----------------
- Add support for Python 3.14.

- Drop support for Python 3.7 and 3.8.


3.2 (2024-03-14)
----------------
- Add support for Python 3.13.

- Implement support for PEP 420 namespaces.


3.1 (2024-01-03)
----------------
- Add support for Python 3.12.


3.0 (2023-02-02)
----------------
- Add support for Python 3.11.

- Drop support for Python 2.7, 3.5, 3.6.


2.0 (2021-10-04)
----------------
- remove claimed support for Jython, testing is a pain in the rear.

- remove claimed support for outdated Python 3.4

- add support for Python 3.9 and 3.10

- reorganize package structure


1.12 (2019-11-24)
-----------------
- move from ``bootstrap.py`` to ``virtualenv`` and ``pip`` for bootstrapping

- update testing procedures


1.11 (2018-11-22)
-----------------
- switch to ``twine`` for egg uploads, otherwise ``project_urls`` in
  setup.py are not shown on PyPI


1.10.1 (2018-11-22)
-------------------
- set up URLs visible on pypi.org


1.9 (2018-06-29)
----------------
- test and declare support for Python 3.7


1.8 (2017-06-01)
----------------
- use pkgutil-style namespace declaration
- package cleanup (``.gitignore``, ``MANIFEST.in``, ``README.rst``)
- docs cleanup (``Makefile``, ``conf.py``)
- tests cleanup (``tox.ini``, ``.travis.yml``)
- remove unsupported documentation bits
- fix coverage tests to only test this package
- remove coveralls from the Travis CI configuration


1.7 (2017-05-29)
----------------
- added pypy3 to the tested tox environments
- added ``flake8`` PEP 8 testing to tox configuration
- PEP 8 code cleanup


1.6 (2017-05-21)
----------------
- move code and issue tracking to GitHub
- move documentation to readthedocs


1.5 (2017-03-15)
----------------
- Update bootstrap script and test with later Python versions


1.4 (2012-04-18)
----------------
- change test code to work under Python 2 and Python 3 in order 
  to drop any 2to3 dependency.
- moving from ``zope.interface.implements`` to the decorator 
  function ``zope.interface.implementer`` which is supported in 
  Python 3 without the need for the ``zope.fixers`` 2to3 
  plugin. The decorator syntax means dropping support for 
  Python 2.4 and 2.5, though.
- add Jython to the supported Python implementations


1.3 (2012-04-09)
----------------
- Add convenience scripts for documentation generation
- Add configuration file for the Tox test harness
- Declare any Python between 2.4 and 3.2 supported
- Move the repository to Git (See 
  https://git.dataflake.org/cgit/dataflake.cache/)


1.2 (2010-05-09)
----------------
- Python 3.1 compatibility
- Updated Sphinx Makefile and configuration to be closer
  to the latest Sphinx version
- Greatly expand installation and testing documentation using 
  ideas from Tres Seaver


1.1 (2010-04-15)
----------------
- Update all bug tracker links to point to the new Launchpad
  bug tracker at https://bugs.launchpad.net/dataflake.cache


1.0 (2010-01-18)
----------------
- Initial release based on caching code formerly residing inside 
  Productsv.LDAPUserFolder
