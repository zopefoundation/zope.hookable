Change log
==========

8.2 (2025-11-18)
----------------

- Move all supported package metadata into ``pyproject.toml``.


8.1 (2025-10-28)
----------------

- Remove unnecessary ``setuptools`` runtime dependency.

- Drop support for Python 3.9.

- Add support for Python 3.14.


8.0 (2025-09-12)
----------------

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.

- Drop support for Python 3.8.

- Add preliminary support for Python 3.14.


7.0 (2024-09-17)
----------------

- C extension now enables multi-phase module initialization (PEP 489).
  For CPython >= 3.11, the ``hookable`` type is now a heap-allocated
  type.  See:
  https://docs.python.org/3.13/howto/isolating-extensions.html

- Drop support for Python 3.7.

- Add support for Python 3.13.

- Build windows wheels on GHA.


6.0 (2023-10-05)
----------------

- Drop support for Python 2.7, 3.5, 3.6.

- Add support for Python 3.12.


5.4 (2022-11-17)
----------------

- Add support for building arm64 wheels on macOS.


5.3 (2022-11-03)
----------------

- Add support for the final release of Python 3.11.


5.2 (2022-09-13)
----------------

- Add support for Python 3.10 and 3.11 (as of 3.11.0rc1).

- Disable unsafe math optimizations in C code.  See `pull request 25
  <https://github.com/zopefoundation/zope.hookable/pull/25>`_.


5.1.0 (2021-07-20)
------------------

- Add support for Python 3.9.

- Create Linux aarch64 wheels.


5.0.1 (2020-03-10)
------------------

- Stop using the setuptools ``Feature`` class, allowing this
  project to be built from source with newer versions of setuptools
  that remove that functionality.


5.0.0 (2019-11-12)
------------------

- Add support for Python 3.7 and 3.8.

- Drop support for Python 3.4.


4.2.0 (2017-11-07)
------------------

- Expose the ``__doc__`` (and, where applicable, ``__bases__`` and
  ``__dict__``) of the hooked object. This lets Sphinx document them.
  See `issue 6 <https://github.com/zopefoundation/zope.hookable/issues/6>`_.

- Respect ``PURE_PYTHON`` at runtime. At build time, always try to
  build the C extensions on supported platforms, but allow it to fail.
  See `issue 7
  <https://github.com/zopefoundation/zope.hookable/issues/7>`_.


4.1.0 (2017-07-26)
------------------

- Drop support for Python 2.6, 3.2 and 3.3.

- Add support for Python 3.5 and 3.6.


4.0.4 (2014-03-19)
------------------

- Add support for Python 3.4.


4.0.3 (2014-03-17)
------------------

- Update ``boostrap.py`` to version 2.2.

- Fix extension compilation on Py3k.


4.0.2 (2012-12-31)
------------------

- Flesh out PyPI Trove classifiers.


4.0.1 (2012-11-21)
------------------

- Add support for Python 3.3.

- Avoid building the C extension explicitly (use the "feature" indirection
  instead).  https://bugs.launchpad.net/zope.hookable/+bug/1025470


4.0.0 (2012-06-04)
------------------

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
------------------

- Update for compatibility with Python 2.6 traceback formats.

- Use Jython-compatible ``bootstrap.py``.


3.4.0 (2007-07-20)
------------------

- Initial release as a separate project.
