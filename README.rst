Django Menu Generator
=====================

    A menu generating application for Django

|status-image| |version-image| |coverage-image|

A productivity tool that enables the generation of full featured menus
through python dictionaries list, you only need to setup the HTML
structure once for each menu you like to build and then use the
dictionaries to generate menu items

Features:
---------

-  Tested support to Python 3.4, 3.5, 3.6
-  Tested support to Django 1.8, 1.9, 1.10, 1.11, 2.0
-  No database
-  Support unlimited menus
-  Icons support
-  Semi-Automatically identifies the selected item and his breadcrums
-  Conditional menu items display through validators (Permissions,
   Authentications or whatever you want)

Documentation:
--------------
The full documentation for Django Menu Generator is allowed here:

http://django-menu-generator.readthedocs.io/en/latest/index.html

Installation:
-------------

You can install it with one of these options:

- ``easy_install django-menu-generator``
- ``pip install django-menu-generator``
- ``git clone https://github.com/LaLogiaDePython/django-menu-generator``

  1. ``cd django-menu-generator``
  2. run python setup.py

- ``wget https://github.com/LaLogiaDePython/django-menu-generator/zipball/master``

  1. unzip the downloaded file
  2. cd into django-menu-generator-\* directory
  3. run python setup.py

Usage:
------

1. Once installed, add ``'menu_generator'`` to your INSTALLED\_APPS.
2. Add ``{% load menu_generator %}`` to templates that will handle the
   menus.
3. Add the list dictionaries containing the menu items to the settings

.. code:: python

    ####################################################################################
    Example: settings.py
    ####################################################################################

    NAV_MENU_LEFT = [
        {
            "name": "Home",
            "url": "/",
        },
        {
            "name": "About",
            "url": "/about",
        },
    ]

    NAV_MENU_RIGHT = [
        {
            "name": "Login",
            "url": "login_url_view",  # reversible
            "validators": ["menu_generator.validators.is_anonymous"],
        },
        {
            "name": "Register",
            "url": "register_view_url",  # reversible
            "validators": ["menu_generator.validators.is_anonymous"],
        },
        {
            "name": "Account",
            "url": "/acount",
            "validators": ["menu_generator.validators.is_authenticated"],
            "submenu": [
                {
                    "name": "Profile",
                    "url": "/account/profile",
                },
                {
                    "name": "Account Balance",
                    "url": "/account/balance",
                    "validators": ["myapp.profiles.is_paid_user"],
                },
                {
                    "name": "Account Secrets",
                    "url": "/account/secrets",
                    "validators": ["menu_generator.validators.is_superuser"],
                }
            ],
        },
    ]

    FOOTER_MENU_LEFT = [
        {
            "name": "Facebook",
            "url": "facebook.com/foobar",
        },
        {
            "name": "Contact US",
            "url": "/contact",
        },
    ]

    FOOTER_MENU_RIGHT = [
        {
            "name": "Address",
            "url": "/address",
        },
    ]

Or you can build the menu dictionaries list inside the project apps with
``menus.py`` files, see docs for more.

4. In your template, load the template tag to generate your menu.

::

    {% load menu_generator %}
    <!DOCTYPE html>
    <html>
        <head><title>Django Menu Generator</title></head>
        <body>
            <!-- NAV BAR Start -->
            {% get_menu "NAV_MENU_LEFT" as left_menu %}
            <div style="float:left;">
                {% for item in left_menu %}
                    <li class="{% if item.selected %} active {% endif %}">
                    <a href="{{ item.url }}"> <i class="{{ item.icon_class }}"></i> {{ item.name }}</a>
                    </li>
                    {% if item.submenu %}
                        <ul>
                        {% for menu in item.submenu %}
                            <li class="{% if menu.selected %} active {% endif %}">
                                <a href="{{ menu.url }}">{{ menu.name }}</a>
                            </li>
                        {% endfor %}
                        </ul>
                    {% endif %}
                {% endfor %}
            </div>

            {% get_menu "NAV_MENU_RIGHT" as right_menu %}
            <div style="float:right;">
                {% for item in right_menu %}
                    <li class="{% if item.selected %} active {% endif %}">
                        <a href="{{ item.url }}">{{ item.name }}</a>
                    </li>
                    {% if item.submenu %}
                        <ul>
                        {% for menu in item.submenu %}
                            <li class="{% if menu.selected %} active {% endif %}">
                                <a href="{{ menu.url }}">{{ menu.name }}</a>
                            </li>
                        {% endfor %}
                        </ul>
                    {% endif %}
                {% endfor %}
            </div>
            <!-- NAV BAR End -->

            <!-- Footer Start -->
            {% get_menu "FOOTER_MENU_LEFT" as left_footer_menu %}
            <div style="float:left;">
                <!-- loop through your left footer menus -->
            </div>

            {% get_menu "FOOTER_MENU_RIGHT" as right_footer_menu %}
            <div style="float:right;">
                <!-- loop through your right footer menus -->
            </div>
            <!-- Footer End -->
        </body>
    </html>

5. Now you must to see your menus generated when you run your project

Running the tests:
------------------

To run the tests against configured environments:

::

    tox

License:
--------

Released under a (`MIT <LICENSE>`__) license.

Author and mantainers:
----------------------

`Milton Lenis <https://github.com/MiltonLn>`__ - miltonln04@gmail.com

`Juan Diego García <https://github.com/yamijuan>`__ - juandgoc@gmail.com

Credits:
--------

We would like to thank `Val Kneeman <https://github.com/un33k>`__, the
original author of this project under the name 'menuware'
https://github.com/un33k/django-menuware

.. |status-image| image:: https://travis-ci.org/LaLogiaDePython/django-menu-generator.svg?branch=master
   :target: https://travis-ci.org/LaLogiaDePython/django-menu-generator?branch=master
.. |version-image| image:: https://img.shields.io/pypi/v/django-menu-generator.svg
   :target: https://pypi.python.org/pypi/django-menu-generator
.. |coverage-image| image:: https://coveralls.io/repos/github/LaLogiaDePython/django-menu-generator/badge.svg?branch=master
   :target: https://coveralls.io/github/LaLogiaDePython/django-menu-generator?branch=master