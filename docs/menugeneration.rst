Menu Generation
===============

Django Menu Generator uses python dictionaries to represent the menu items, usually a menu item is as follows:

.. code:: python

    {
        "name": 'some name',
        "icon_class": 'some icon class',
        "url": URL spec,
        "root": True | False,
        "related_urls": [ list of related URLs ],
        "validators": [ list of validators ],
        "submenu": Dictionary like this
    }

Where each key is as follows:

- ``name``: A string representing the label of the menu item. If you are using i18n here you can pass the name with the ``ugettext_lazy`` function

- ``icon_class``: A string representing the class of the icon you wish to show on the menu item, e.g you can use font-awesome

- ``url``: See :doc:`urls`

- ``related_urls``: If one of these URLs is part of the path on the currently opened page, the menu item will be marked as selected (format of URLs like described at :doc:`urls`)

- ``root``: A flag to indicate this item is the root of a path, with this you can correctly mark nested menus as selected.

- ``validators``: See :doc:`validators`

- ``submenu``: You can create infinite nested submenus passing here menu items like this

Django Menu Generator offers two ways to generate the menus, through the Django settings and through each of the Django
apps

Generating menus through settings
---------------------------------

You can add various list dictionaries representing each menu you have as explained in :doc:`usage`
We recommend to have a ``menus.py`` file with the menu list dictionaries and then import it to the settings file if you
go this way

Generating menus through apps
-----------------------------

Some people prefer to isolate all the aspects of a project between apps, so, we add this feature to allow the menus
live inside each app.

You need to add inside the app a ``menus.py`` file that contains a dictionary called ``MENUS``, each element of the
dictionary will be a menu list dictionary with all the configuration needed to display that menu, e.g:

.. code:: python

    MENUS = {
        'NAV_MENU_LEFT': [
            {
                "name": "App1 Feature",
                "url": "/app1-feature"
            }
        ],
        'NAV_MENU_TOP': [
            {
                "name": "Second Menu Feature",
                "url": "named_url"
            }
        ]
    }

So, as an example, for the ``'NAV_MENU_LEFT'``, Django Menu Generator will loop each app searching for the ``'NAV_MENU_LEFT'``
list dictionaries inside of the ``MENUS`` and build all the menu configuration to build the whole menu.

With this feature you can have a project structure like this::

    your_project/
    ├── config_folder/
    │   └── ...
    ├── app1
    │   └── models.py
    │       forms.py
    │       views.py
    │       menus.py
    │
    ├── app2
    │   └── models.py
    │       forms.py
    │       views.py
    │       menus.py
    │
     ...

You can have a mix of the two approaches if you wish
