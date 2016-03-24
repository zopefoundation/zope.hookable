Changes
-------

4.1.0 (unreleased)
##################

- Drop support for Python 2.6 and 3.2.

- Add support for Python 3.5.

4.0.4 (2014-03-19)
##################

- Add support for Python 3.4.

4.0.3 (2014-03-17)
##################

- Update ``boostrap.py`` to version 2.2.

- Fix extension compilation on Py3k.

4.0.2 (2012-12-31)
##################

- Flesh out PyPI Trove classifiers.

4.0.1 (2012-11-21)
##################

- Add support for Python 3.3.

- Avoid building the C extension explicitly (use the "feature" indirection
  instead).  https://bugs.launchpad.net/zope.hookable/+bug/1025470

4.0.0 (2012-06-04)
##################

- Add support for PyPy.

- Add support for continuous integration using ``tox`` and ``jenkins``.

- Add a pure-Python reference implementation.

- Move doctests to Sphinx documentation.

- Bring unit test coverage to 100%.

- Add 'setup.py docs' alias (installs ``Sphinx`` and dependencies).

- Add 'setup.py dev' alias (runs ``setup.py develop`` plus installs
  ``nose`` and ``coverage``).

- Drop support for Python 2.4 / 2.5.

- Remove of 'zope.testing.doctestunit' in favor of stdlib's 'doctest.

- Add Python 3 support.

3.4.1 (2009-04-05)
##################

- Update for compatibility with Python 2.6 traceback formats.

- Use Jython-compatible ``bootstrap.py``.

3.4.0 (2007-07-20)
##################

- Initial release as a separate project.
