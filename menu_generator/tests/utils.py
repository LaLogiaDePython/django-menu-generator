def is_user_happy(request):
    return request.user.is_auth and request.user.is_happy  # pragma: no cover


def is_paid_user(request):
    return request.user.is_auth and request.user.is_happy  # pragma: no cover


def is_main_site(request):
    """
    Non-User condition.
    """
    return True  # pragma: no covere


def validator_with_parameters(request, param1, param2):
    return True


class TestUser(object):
    """
    Test User Object.
    """
    is_auth = False
    is_staff = False
    is_superuser = False
    is_happy = False
    is_paid = False
    permissions = []

    def __init__(self, staff=False, superuser=False, authenticated=False, happy=False, paid=False):
        self.is_auth = authenticated
        self.is_staff = authenticated and staff
        self.is_superuser = authenticated and superuser
        self.is_happy = authenticated and happy
        self.is_paid = authenticated and paid
        self.permissions = []

    @property
    def is_authenticated(self):
        return self.is_auth

    def add_perm(self, permission):
        """
        Method for add a permission to test user
        :param permission: Permission to be added
        """
        self.permissions.append(permission)

    def has_perm(self, permission):
        """
        Method for checking if a test user has a permission
        :param permission: Permission to be checked
        :return: Boolean indicating if a test user has a permission or not
        """
        return permission in self.permissions
