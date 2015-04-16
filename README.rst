Muffin-Jade
###########

.. _description:

Muffin-Jade -- Jade template engine for Muffin framework.

.. _badges:

.. image:: http://img.shields.io/travis/klen/muffin-jade.svg?style=flat-square
    :target: http://travis-ci.org/klen/muffin-jade
    :alt: Build Status

.. image:: http://img.shields.io/pypi/v/muffin-jade.svg?style=flat-square
    :target: https://pypi.python.org/pypi/muffin-jade

.. image:: http://img.shields.io/pypi/dm/muffin-jade.svg?style=flat-square
    :target: https://pypi.python.org/pypi/muffin-jade

.. image:: http://img.shields.io/gratipay/klen.svg?style=flat-square
    :target: https://www.gratipay.com/klen/
    :alt: Donate

.. _contents:

.. contents::

.. _requirements:

Requirements
=============

- python >= 3.3

.. _installation:

Installation
=============

**Muffin-Jade** should be installed using pip: ::

    pip install muffin-jade

.. _usage:

Usage
=====

Add **muffin_jade** to **PLUGINS** in your Muffin Application configuration.

Options
-------

**JADE_CACHE_SIZE** -- Cache size for compiled templates (100)

**JADE_ENCODING** -- Templates' encoding (UTF-8)

**JADE_PRETTY** -- Pretty output (True)

**JADE_TEMPLATE_FOLDERS** -- List of pathes to templates folder ([templates])

Views
-----

::

    # Register custom context provider
    # could be a function/coroutine
    @app.ps.jade.ctx_provider
    def custom_context():
        return { 'VAR': 'VALUE' }

    # Register a function into templates
    @app.ps.jade.register
    def sum(a, b):
        return a + b

    @app.register('/')
    def index(request):
        """ Check for user is admin. """
        local_context = {'key': 'value'}
        return app.ps.jade.render('index.jade', **local_context)


.. _bugtracker:

Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/klen/muffin-jade/issues

.. _contributing:

Contributing
============

Development of Muffin-Jade happens at: https://github.com/klen/muffin-jade


Contributors
=============

* klen_ (Kirill Klenov)

.. _license:

License
=======

Licensed under a `MIT license`_.

.. _links:


.. _klen: https://github.com/klen

.. _MIT license: http://opensource.org/licenses/MIT
