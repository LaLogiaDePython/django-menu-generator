URLs
====

You can pass the URL parameters to menu items in three ways.

Raw URLs
--------

A hard-coded url:

.. code:: python

    "url": '/some-path/to-feature'

Reversible URLs
---------------

An url that can be reversed with the `reverse` method:

.. code:: python

    "url": 'named_url'

URL with args or kwargs
-----------------------

e.g. If you have an url with kwargs like this:

.. code:: python

    url(r'^update/(?P<pk>\d+)/$', SomeView.as_view(), name='update'),

you can pass the url as follows:

.. code:: python

    "url": {"viewname": 'update', "kwargs": {"pk": 1}}

In fact, you can pass any of the parameters of the reverse method through the dictionary

For Django 1.10 the reverse method sign is: ``reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)``

