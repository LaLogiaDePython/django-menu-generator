# Django Menu Generator
> A menu generating application for Django

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]

A productivity tool that enables the generation of full featured menus through python dictionaries list, you only need to setup the HTML structure once for each menu you like to build and then use the dictionaries to generate menu items

## Features:

- Tested support to Python 2.7, 3.4, 3.5, 3.6
- Tested support to Django 1.8.18, 1.9.13, 1.10.7, 1.11
- No database
- Support unlimited menus
- Icons support
- Semi-Automatically identifies the selected item and his breadcrums
- Conditional menu items display through validators (Permissions, Authentications or whatever you want)

## Installation:

You can install it with one of these options:
- easy_install django-menu-generator
- pip install django-menu-generator
- git clone http://github.com/un33k/django-menu-generator
    a. cd django-menu-generator
    b. run python setup.py
- wget https://github.com/un33k/django-menu-generator/zipball/master
    a. unzip the downloaded file
    b. cd into django-menu-generator-* directory
    c. run python setup.py

## Usage:

1. Install 'django-menu-generator' as per the above instructions.
2. Add 'menu_generator' to your INSTALLED_APPS.
3. Add {% load menu_generator %} to templates that will handle the menus.

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
```

You can build the menu dictionaries list inside the project apps with ``menus.py`` files, see the docs for more.

Then in your template, load the template tag to generate your menu.

   ```html
    <!-- base.html -->
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
   ```

## Running the tests:

To run the tests against the current environment:

    python manage.py test


## License:

Released under a ([MIT](LICENSE)) license.

## Author and mantainers: 

[Milton Lenis](https://github.com/MiltonLn) - miltonln04@gmail.com

## Credits:

I'd like to thank [Val Kneeman][valkneeman-link], the original author of this project under the name 'menuware'
https://github.com/un33k/django-menuware



[status-image]: https://travis-ci.org/RADYConsultores/django-menu-generator.svg?branch=master
[status-link]: https://travis-ci.org/RADYConsultores/django-menu-generator?branch=master

[version-image]: https://img.shields.io/pypi/v/django-menu-generator.svg
[version-link]: https://pypi.python.org/pypi/django-menu-generator

[coverage-image]: https://coveralls.io/repos/github/RADYConsultores/django-menu-generator/badge.svg?branch=master
[coverage-link]: https://coveralls.io/github/RADYConsultores/django-menu-generator?branch=master

[download-image]: https://img.shields.io/pypi/dm/django-menu-generator.svg
[download-link]: https://pypi.python.org/pypi/django-menu-generator

[valkneeman-link]: https://github.com/un33k

