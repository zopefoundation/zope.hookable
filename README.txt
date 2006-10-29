zope.hookable Package Readme
==========================

Overview
--------

Hookable object support.

Support the efficient creation of hookable objects, which are callable objects
that are meant to be replaced by other callables, at least optionally.

The idea is you create a function that does some default thing and make it
hookable. Later, someone can modify what it does by calling its sethook method
and changing its implementation.  All users of the function, including those
that imported it, will see the change.


Changes
-------

See CHANGES.txt.

Installation
------------

See INSTALL.txt.


Developer Resources
-------------------

- Subversion browser:

  http://svn.zope.org/zope.hookable/

- Read-only Subversion checkout:

  $ svn co svn://svn.zope.org/repos/main/zope.hookable/trunk

- Writable Subversion checkout:

  $ svn co svn+ssh://userid@svn.zope.org/repos/main/zope.hookable/trunk

- Note that the 'src/zope/hookable package is acutally a 'svn:externals' link
  to the corresponding package in the Zope3 trunk (or to a specific tag, for
  released versions of the package).
