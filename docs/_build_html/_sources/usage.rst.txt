Usage
=====

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
``menus.py`` files, see :doc:`menugeneration` for more.

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
