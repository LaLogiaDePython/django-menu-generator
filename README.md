Django Menuware
====================

**A menu generating application for Django**

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]

Overview
====================

Generates **Simple Navigation** for Django projects/apps, while keeping it **DRY**.

How to install
====================

    1. easy_install django-menuware
    2. pip install django-menuware
    3. git clone http://github.com/un33k/django-menuware
        a. cd django-menuware
        b. run python setup.py
    4. wget https://github.com/un33k/django-menuware/zipball/master
        a. unzip the downloaded file
        b. cd into django-menuware-* directory
        c. run python setup.py

How to use
====================
    1. Install `django-menuware` as per the above instructions.
    2. Add `menuware` to your `INSTALLED_APPS`.
    3. Add `{% load menuware %}` to templates that require it.

   ```python
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
            "validators": ["menuware.utils.is_anonymous"],
        },
        {
            "name": "Register",
            "url": "register_view_url",  # reversible
            "validators": ["menuware.utils.is_anonymous"],
        },
        {
            "name": "Account",
            "url": "/acount",
            "validators": ["menuware.utils.is_authenticated"],
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
                    "validators": ["menuware.utils.is_superuser"],
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
   ```

Then in your template, load the template tag to generate your menu.

   ```html
    <!-- base.html -->
    {% load menuware %}

    <!DOCTYPE html>
    <html>
        <head><title>Django Menuware</title></head>
        <body>
            <!-- NAV BAR Start -->
            {% get_menu "NAV_MENU_LEFT" as left_menu %}
            <div style="float:left;">
                {% for item in left_menu %}
                    <li class="{% if item.selected %} active {% endif %}">
                        <a href="{{item.url}}">{{item.name}}</a>
                    </li>
                    {% if item.submenu %}
                        <ul>
                        {% for menu in item.submenu %}
                            <li class="{% if menu.selected %} active {% endif %}">
                                <a href="{{menu.url}}">{{menu.name}}</a>
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
                        <a href="{{item.url}}">{{item.name}}</a>
                    </li>
                    {% if item.submenu %}
                        <ul>
                        {% for menu in item.submenu %}
                            <li class="{% if menu.selected %} active {% endif %}">
                                <a href="{{menu.url}}">{{menu.name}}</a>
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
   ```

Running the tests
====================

To run the tests against the current environment:

    python manage.py test


License
====================

Released under a ([MIT](LICENSE)) license.


Version
====================
X.Y.Z Version

    `MAJOR` version -- when you make incompatible API changes,
    `MINOR` version -- when you add functionality in a backwards-compatible manner, and
    `PATCH` version -- when you make backwards-compatible bug fixes.

[status-image]: https://secure.travis-ci.org/un33k/django-menuware.png?branch=master
[status-link]: http://travis-ci.org/un33k/django-menuware?branch=master

[version-image]: https://img.shields.io/pypi/v/django-menuware.svg
[version-link]: https://pypi.python.org/pypi/django-menuware

[coverage-image]: https://coveralls.io/repos/un33k/django-menuware/badge.svg
[coverage-link]: https://coveralls.io/r/un33k/django-menuware

[download-image]: https://img.shields.io/pypi/dm/django-menuware.svg
[download-link]: https://pypi.python.org/pypi/django-menuware
