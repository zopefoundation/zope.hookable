Changes
-------

4.0.3 (2014-03-17)
##################

- Updated ``boostrap.py`` to version 2.2.

- Fixed extension compilation on Py3k.

4.0.2 (2012-12-31)
##################

- Fleshed out PyPI Trove classifiers.

4.0.1 (2012-11-21)
##################

- Added support for Python 3.3.

- Avoid building the C extension explicitly (use the "feature" indirection
  instead).  https://bugs.launchpad.net/zope.hookable/+bug/1025470

4.0.0 (2012-06-04)
##################

- Added support for PyPy.

- Added support for continuous integration using ``tox`` and ``jenkins``.

- Added a pure-Python reference implementation.

- Doctests moved to Sphinx documentation.

- 100% unit test coverage.

- Added 'setup.py docs' alias (installs ``Sphinx`` and dependencies).

- Added 'setup.py dev' alias (runs ``setup.py develop`` plus installs
  ``nose`` and ``coverage``).

- Dropped support for Python 2.4 / 2.5.

- Removed use of 'zope.testing.doctestunit' in favor of stdlib's 'doctest.

- Added Python 3 support.

3.4.1 (2009-04-05)
##################

- Updated tests for compatibility with Python 2.6 traceback formats.

- Use Jython-compatible ``bootstrap.py``.

3.4.0 (2007-07-20)
##################

- Initial release as a separate project.
