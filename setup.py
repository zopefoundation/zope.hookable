##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.hookable package
"""
import os
import platform

from distutils.errors import CCompilerError
from distutils.errors import DistutilsExecError
from distutils.errors import DistutilsPlatformError

from setuptools import setup
from setuptools import find_packages
from setuptools import Extension

from setuptools.command.build_ext import build_ext


class optional_build_ext(build_ext):
    """This class subclasses build_ext and allows
       the building of C extensions to fail.
    """

    def run(self):
        try:
            build_ext.run(self)
        except DistutilsPlatformError as e:
            self._unavailable(e)

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (CCompilerError, DistutilsExecError, OSError) as e:
            self._unavailable(e)

    def _unavailable(self, e):
        print('*' * 80)
        print("""WARNING:
        An optional code optimization (C extension) could not be compiled.
        Optimizations for this package will not be available!""")
        print()
        print(e)
        print('*' * 80)


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


codeoptimization = [
    Extension(
        "zope.hookable._zope_hookable",
        [os.path.join('src', 'zope', 'hookable', "_zope_hookable.c")],
    ),
]

is_pypy_or_jython = platform.python_implementation() in ('PyPy', 'Jython')

# Jython cannot build the C optimizations, while on PyPy they are
# anti-optimizations (the C extension compatibility layer is known-slow,
# and defeats JIT opportunities).
if is_pypy_or_jython:
    ext_modules = {}
else:
    ext_modules = codeoptimization

TESTS_REQUIRE = [
    'zope.testing',
    'zope.testrunner',
]

setup(name='zope.hookable',
      version='5.1.0',
      url='http://github.com/zopefoundation/zope.hookable',
      license='ZPL 2.1',
      description='Zope hookable',
      keywords='function hook replacement loose coupled',
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      long_description=(read('README.rst') + '\n\n' +
                        read('CHANGES.rst')),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: Zope Public License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Framework :: Zope :: 3",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      ext_modules=ext_modules,
      cmdclass={
          'build_ext': optional_build_ext,
      },
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope'],
      install_requires=[
          'setuptools',
      ],
      include_package_data=True,
      zip_safe=False,
      test_suite='zope.hookable.tests.test_hookable.test_suite',
      extras_require={
          'docs': ['Sphinx'],
          'testing': TESTS_REQUIRE + ['coverage'],
          'test': TESTS_REQUIRE,
      },
      python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
      )
