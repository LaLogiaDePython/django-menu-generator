Validators
==========

Django Menu Generator uses validators to allow the displaying of menu items.

A validator is a function that receives the request as arg and returns a boolean indicating if the check has passed

for Django Menu Generator the validators must always be a list containing at least one callable or python path to a callable.
If there is more than one validator, all of them will be evaluated using the AND connector.

Built-in validators
-------------------

Django Menu Generator has the following built-in validators:

- is_superuser:

    A validator to check if the authenticated user is a superuser

    Usage:

    .. code:: python

        "validators": ['menu_generator.validators.is_superuser']

- is_staff:

    A validator to check if the authenticated user is member of the staff

    Usage:

    .. code:: python

        "validators": ['menu_generator.validators.is_staff']

- is_authenticated:

    A validator to check if user is authenticated

    Usage:

    .. code:: python

        "validators": ['menu_generator.validators.is_authenticated']

- is_anonymous:

    A validator to check if the user is not authenticated

    Usage:

    .. code:: python

        "validators": ['menu_generator.validators.is_anonymous']

- user_has_permission:

    A validator to check if the user has the given permission

    Usage:

    .. code:: python

        "validators": [
            ('menu_generator.validators.user_has_permission', 'app_label.permission_codename')
        ]

- More than one validator:

    You can pass more than one validator to evaluate using the AND connector

    .. code:: python

        "validators": [
            'menu_generator.validators.is_staff',
            ('menu_generator.validators.user_has_permission', 'some_app.some_permission')
            ...
        ]

Custom validators
-----------------

You can build your own validators and use them with Django Menu Generator

Let's build a validator that checks if the user have more than one pet (dummy example) assuming the user has a
many to many relation called pets

Assuming we build the function inside ``your_project/app1`` on a ``menu_validators.py`` we have:

.. code:: python

    # Remember you always must to past the request as first parameter
    def has_more_than_one_pet(request):

        return request.user.pets.count() > 0

So we can use it as a validator

.. code:: python

    "validators": ['your_project.app1.menu_validators.has_more_than_one_pet']

Now let's build a validator that checks if the user's pet belongs to a specific type to illustrate the validators with
parameters.

Assuming we build the function inside the same path and the user have a foreign key called pet

.. code:: python

    def has_a_pet_of_type(request, type):

        return request.user.pet.type == type

So we use the validator like this:

.. code:: python

    "validators": [
        ('your_project.app1.menu_validators.has_a_pet_of_type', 'DOG')
    ]

As you can see, we use tuples to pass parameters to the validators, where the first position is the validator and the rest are
the function parameters