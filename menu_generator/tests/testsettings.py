DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
SECRET_KEY = "r4dy"
INSTALLED_APPS = [
    'menu_generator',
    'menu_generator.tests.test_apps.app1.apps.MyAppConfig',
    'menu_generator.tests.test_apps.app2',
    'menu_generator.tests.test_apps.app3'
]
MIDDLEWARE_CLASSES = []
ROOT_URLCONF = 'menu_generator.tests.urls'

NAV_MENU = [
    {
        "name": "Main",
        "url": "/",
    },
    {
        "name": "Account",
        "url": "/account",
        "validators": ["menu_generator.validators.is_authenticated", ],
        "submenu": [
            {
                "name": "Profile",
                "url": '/account/profile/',
            },
        ],
    },
    {
        "name": "Create User",
        "url": "users:create"
    },
    {
        "name": "Update User",
        "url": {"viewname": "users:update", "kwargs": {'pk': 1}}
    }
]
